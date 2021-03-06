# Add an extension

Only packages available in [pypi](https://pypi.org) can be added to this list.
The package must be available in [conda-forge](https://conda-forge.org/docs) if
you prefer using ``conda`` to create the environment as explained below.

To add an extension:

1. add the package name and a short description to the table in `readme_source/1-readme_base.md`
2. add the name of the extension (name on pypi) to ``extension_list.txt``
3. create and activate the environment - see below
4. run ``python make_README.py`` to update the README.md file
5. Commit the changes and send a pull request to this repository.

## Setting up the environment

To collect the necessary information, it is necessary to install all the packages
in a dedicated python environment and generate the ``README.md`` from it.


### Using pip

1. run ``python -m venv ext_list_env``
2. run ``source ext_list_env/bin/activate``  # on macOS and Linux
   run ``.\ext_list_env\Scripts\activate``   # on Windows
3. run ``pip install -r extension_list.txt``


### Using conda

1. run ``conda create -n ext_list_env python -c conda-forge  --file extension_list.txt``
2. run ``conda activate ext_list_env``
