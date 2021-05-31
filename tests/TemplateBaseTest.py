import unittest
import jinja2
import pathlib
from typing_extensions import Literal

from filters import FilterModule, TemplateFilters

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
        env.filters.update(TemplateFilters.filters)
        filter_plugin = FilterModule()
        env.filters.update(filter_plugin.filters())
        return env
