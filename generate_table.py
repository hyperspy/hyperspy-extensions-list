import os

import hyperspy.api as hs


readme_source_folder = 'readme_source'

from hyperspy.ui_registry import ALL_EXTENSIONS
from prettytable import PrettyTable

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


with open(os.path.join(readme_source_folder, '2-extension_table.md'), "w") as f:
    f.write(table.get_html_string())

source_file_list = os.listdir(readme_source_folder)

with open("README.md", "w") as readme_file:
    for filename in source_file_list:
        with open(os.path.join(readme_source_folder, filename), "r") as file:
            readme_file.write(file.read())
            readme_file.write('\n\n')
