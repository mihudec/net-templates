import pathlib

import jinja2
from pydantic.typing import Literal, Union, Dict, List

from net_templates.definitions import TEMPLATES_DIR
from net_templates.filters import AnsibleFilters, CustomFilters

supported_device_types = Literal['ios']


class TemplarBase:

    @classmethod
    def get_device_type_environment(cls, device_type: supported_device_types) -> jinja2.Environment:
        env = jinja2.environment.Environment(
            loader=jinja2.loaders.FileSystemLoader(
                searchpath=TEMPLATES_DIR.joinpath(device_type)
            ),
            autoescape=True,
            trim_blocks=True,
            lstrip_blocks=True,
            # undefined=jinja2.runtime.ChainableUndefined,
            undefined=jinja2.runtime.StrictUndefined
        )

        ansible_filters = AnsibleFilters().filters()
        custom_filters = CustomFilters().filters()
        env.filters.update(ansible_filters)
        env.filters.update(custom_filters)
        return env

    @classmethod
    def extend_searchpath(cls, env: jinja2.Environment, path: pathlib.Path):
        if not isinstance(env.loader, jinja2.loaders.FileSystemLoader):
            raise TypeError("Given environment does not use 'FileSystemLoader'")
        env.loader.searchpath.append(str(path))

    @classmethod
    def render_template(cls, template_name: str, data: dict, device_type: supported_device_types = 'ios') -> str:
        env = cls.get_device_type_environment(device_type=device_type)
        template = None
        try:
            template = env.get_template(name=template_name)
        except Exception as e:
            raise
        if template is None:
            return None
        result = template.render(**data)
        return result


def get_template_dir(device_type: supported_device_types = 'ios'):
    env = TemplarBase.get_device_type_environment(device_type=device_type)
    return pathlib.Path(env.loader.searchpath[0])
