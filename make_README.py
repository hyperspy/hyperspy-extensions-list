import contextlib
import io
import os

import hyperspy.api as hs


readme_source_folder = 'readme_source'

# Get the information from hyperspy
f = io.StringIO()
with contextlib.redirect_stdout(f):
    hs.print_known_signal_types()
table_ascii = f.getvalue()

with open(os.path.join(readme_source_folder, '2-extension_table.md'), "w") as f:
    f.write(table_ascii)

# Make the README.md by concatenation
source_file_list = sorted(os.listdir(readme_source_folder))

with open("README.md", "w") as readme_file:
    for filename in source_file_list:
        with open(os.path.join(readme_source_folder, filename), "r") as file:
            readme_file.write(file.read())
            readme_file.write('\n\n')
