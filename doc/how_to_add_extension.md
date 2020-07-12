# Add an extension

This repository maintain a list of hyperspy extensions to help users find the
extension they need. The user facing information are written in the README.md
which is generated automatically.

To add an extension:
1. add the package name and a short description in `readme_source/1-readme_base.md`
2. add the name of the extension (name on pypi) to ``extension_list.txt``
3. create and activate the environment - see below
4. run ``python make_README.py`` to update the README.md file.

To collect the necessary information, it is necessary to install the librairies
in a dedicated python environment and generate the README.md from this environment.

## Setting up the environment
### Using pip

1. run ``python -m venv ext_list_env``
2. run ``source ext_list_env/bin/activate``  # on macOS and Linux
   run ``.\ext_list_env\Scripts\activate``   # on Windows
3. run ``pip install -r extension_list.txt``


### Using conda

1. run ``conda create - n ext_list_env python``
2. run ``conda activate ext_list_env``
3. run ``conda install --file extension_list.txt``
