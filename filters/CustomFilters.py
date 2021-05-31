from netcm.models import models_map
from pydantic.typing import Union, List, Literal
class FilterModule(object):

    def __init__(self):
        pass

    def filters(self):
        filters = {
            "to_vlan_range": self.to_vlan_range,
            "str_to_obj": self.str_to_obj
        }
        return filters

    def validate_data(self, data: dict, model: str) -> bool:
        result = False
        model_class = models_map.get(model)
        if model_class is None:
            result = False
            # raise ValueError(f"Unknown model: '{model}'. Current models are: '{models_map}'")
        else:
            try:
                model_object = model_class.parse_obj(data)
                result = True
            except Exception as e:
                result = False

        return result

    def to_vlan_range(self, vlans: Union[List[int], Literal["none", "all"]]) -> str:

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

    def str_to_obj(self, string: str):
        return eval(string)