import pathlib
import dataclasses
import jinja2
from pydantic import BaseModel
from pydantic.typing import Literal, Union, Dict, List

from net_templates.definitions import TEMPLATES_DIR
from net_templates.filters import NetFilters

supported_device_types = Literal['ios']


class ConfigDefaultsBase(BaseModel):
    INCLUDE_DEFAULTS: bool = None
    PLATFORM_CDP_DEFAULT_ON: bool = None
    INTERFACES_DEFAULT_NO_SHUTDOWN: bool = None
    INTERFACE_DEFAULT_MODE: Literal['switched', 'routed'] = None


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
            undefined=jinja2.runtime.StrictUndefined,
        )

        net_filters = NetFilters().filters()
        env.filters.update(net_filters)
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

