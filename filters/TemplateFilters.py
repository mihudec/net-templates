import ipaddress
from typing import List, Union
from typing_extensions import Literal
import json
import jmespath

class FilterModule(object):

    def __init__(self):
        pass

    def filters(self):
        filters = {}
        return filters

class TemplateFilters(object):

    @staticmethod
    def to_vlan_range(vlans: Union[List[int], Literal["none", "all"]]) -> str:

        if isinstance(vlans, str):
            if vlans == "none":
                return "none"
            elif vlans == "all":
                return "all"
            else:
                raise ValueError(f"Invalid string value: {vlans}")
        min_diff = 1
        # Assume vlans is List[int]
        vlans = sorted(list(set(vlans)))
        parts = []
        current_entry = [None, None]
        for vlan in vlans:
            if current_entry[0] is None:
                current_entry[0] = vlan
            elif current_entry[1] is None:
                if current_entry[0] + 1 == vlan:
                    current_entry[1] = vlan
                else:
                    # Flush
                    parts.append(str(current_entry[0]))
                    current_entry = [vlan, None]
            else:
                if current_entry[1] + 1 == vlan:
                    current_entry[1] = vlan
                else:
                    # Flush
                    if (current_entry[1] - current_entry[0]) > min_diff:
                        parts.append(f"{current_entry[0]}-{current_entry[1]}")
                    else:
                        parts.extend(map(str, current_entry))
                    current_entry = [vlan, None]
        # Flush remainder
        if not any(current_entry):
            pass
        elif all(current_entry):
            if (current_entry[1] - current_entry[0]) > min_diff:
                parts.append(f"{current_entry[0]}-{current_entry[1]}")
            else:
                parts.extend(map(str, current_entry))
                current_entry = [None, None]
        else:
            parts.append(str(current_entry[0]))
        vlan_range = ",".join(parts)
        if vlan_range == "":
            return "none"
        elif vlan_range == "1-4096":
            return "all"

        return vlan_range

    @staticmethod
    def ipaddr(ip_address: Union[ipaddress.IPv4Address, ipaddress.IPv4Interface, ipaddress.IPv4Network, ipaddress.IPv6Address, ipaddress.IPv6Interface, ipaddress.IPv6Network], operation: str = None):
        address = None
        for func in [ipaddress.ip_address, ipaddress.ip_interface, ipaddress.ip_network]:
            if address is None:
                try:
                    address = func(ip_address)
                except Exception as e:
                    pass
        if operation is None:
            if address:
                return True
            else:
                return False
        if operation == "address":
            if isinstance(address, (ipaddress.IPv4Address, ipaddress.IPv6Address)):
                return address
        raise ValueError("Invalid IP Given")

    @staticmethod
    def json_query(data: Union[list, dict], query: str):
        return jmespath.search(query, data)

    @staticmethod
    def str_to_obj(string: str):
        return eval(string)

    @staticmethod
    def to_json(data: Union[list, dict]) -> str:
        return json.dumps(data)

    filters = {
        "to_vlan_range": to_vlan_range.__func__,
        "ipaddr": ipaddr.__func__,
        "json_query": json_query.__func__,
        "str_to_obj": str_to_obj.__func__,
        "to_json": to_json.__func__
    }
