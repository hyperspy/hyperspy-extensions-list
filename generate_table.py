import yaml
import hyperspy.api as hs
from shutil import copyfile

# html = print_html(hs.print_known_signal_types())
copyfile("readme_base.md", "README.md")

from hyperspy.ui_registry import ALL_EXTENSIONS
from prettytable import PrettyTable
from hyperspy.misc.utils import print_html
table = PrettyTable()
table.field_names = [
    "signal_type",
    "aliases",
    "class name",
    "package"]
for sclass, sdict in ALL_EXTENSIONS["signals"].items():
    # skip lazy signals and non-data-type specific signals
    if sdict["lazy"] or not sdict["signal_type"]:
        continue
    aliases = (", ".join(sdict["signal_type_aliases"])
               if "signal_type_aliases" in sdict
               else "")
    package = sdict["module"].split(".")[0]
    table.add_row([sdict["signal_type"], aliases, sclass, package])
    table.sortby = "class name"


with open("README.md", "a") as file:
    file.write(table.get_html_string())



# with open("README.md", "w") as readme:
#     file.write(table.get_html_string())
