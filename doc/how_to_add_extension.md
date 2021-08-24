# Add an extension

Only packages available in [pypi](https://pypi.org) and
[conda-forge](https://conda-forge.org/docs) can be added to this list.

To add an extension:

1. add the package name and a short description to the table in `readme_source/1-readme_base.md`
2. add the name of the extension (name on pypi) to ``extension_list.txt``
3. open a pull request to https://github.com/hyperspy/hyperspy-extensions-list

The `README.md` will be updated automatically by a Github workflow, after the
pull request is merged. In case github actions are enabled in the repository the
pull request is coming from, the workflow will run in the fork repository and
the branch (and therefore the pull request) will be updated when necessary.

Additionally, this workflow runs weekly to keep the `signal_type` list up to date.


## Running the `make_readme.py` script manually

To collect the necessary information, it is necessary to install all the packages
in a dedicated python environment and generate the ``README.md`` from it.

1. create and activate the environment - see below
2. run python make_README.py to update the README.md file

### Using pip

1. run ``python -m venv ext_list_env``
2. run ``source ext_list_env/bin/activate``  # on macOS and Linux
   run ``.\ext_list_env\Scripts\activate``   # on Windows
3. run ``pip install -r extension_list.txt``


### Using conda

1. run ``conda create -n ext_list_env python -c conda-forge  --file extension_list.txt``
2. run ``conda activate ext_list_env``

