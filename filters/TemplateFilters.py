from typing import List, Union
from typing_extensions import Literal

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


    filters = {
        "to_vlan_range": to_vlan_range.__func__
    }
