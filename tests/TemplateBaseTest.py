import unittest
import jinja2
import pathlib
from typing_extensions import Literal
from net_templates.filters import AnsibleFilters, CustomFilters


class BaseTemplateTest(unittest.TestCase):

    VENDOR = ''
    TEMPLATE_NAME = ''


    @classmethod
    def get_vendor_environment(cls, vendor: Literal["ios"]) -> jinja2.environment.Environment:
        env = jinja2.environment.Environment(
            loader=jinja2.loaders.FileSystemLoader(
                searchpath=pathlib.Path(__file__).parent.parent.joinpath("templates").joinpath(vendor)
            ),
            autoescape=True,
            trim_blocks=True,
            lstrip_blocks=True,
            undefined=jinja2.ChainableUndefined,
        )

        ansible_filters = AnsibleFilters().filters()
        custom_filters = CustomFilters().filters()
        env.filters.update(ansible_filters)
        env.filters.update(custom_filters)
        return env
