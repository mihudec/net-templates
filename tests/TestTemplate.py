import jinja2
import pathlib
import sys




def get_template_loader(vendor: str):
    print(sys.path)
    loader = jinja2.loaders.PackageLoader(package_name="net-templates", package_path="templates")
    loader = jinja2.loaders.FileSystemLoader(searchpath=pathlib.Path(__file__).parent.parent.joinpath("templates"))
    return loader

if __name__ == '__main__':
    loader = get_template_loader(vendor="ios")