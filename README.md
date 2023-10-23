# Rosetta - Python

## About

This GitHub repo accompanies a [blog post]() which describes the tooling ecosystem for Python. This repo provides the technical details in a concise form to accompany the more discussive blog post.

## Python interpreter

On Windows Python can be downloaded from [here](https://www.python.org/downloads/).

Typically I invoke Python scripts using a command line in Git Bash like:

```shell
./my_script.py
```

This works because I start all of my Python scripts with:

```shell
#!/usr/bin/env python
```
More generally Python scripts are invoked like:
```shell
python my_script.py
```

## Python Package Management

Python package management is typically done using the `pip` package manager, installed with Python.

A Python package is configured using the `pyproject.toml` file, this project includes a minimal `pyproject.toml` file.

Typically Python is run in a virtual environment which can be created, as described below.

New packages are installed with:

```shell
pip install pytest
```

And a so-called `editable` package can be installed in the local project using:

```shell
pip install -e .
```

This installs the local project so it is available to other projects, and updates when the code is changed.


## Virtual Environments

Virtual environments can be created using the built-in `venv` library:

```shell
python -m venv {environment_name}
```

It is then activated (on my Windows machine in Git Bash) with:

```shell
source {environment_name}/Scripts/activate
```

I suspect this is a slightly unusual way of invoking since Linux machines will put the activate command in the `bin` subdirectory of the environment. Interestingly the shell script `deactivate` command is not available on a Windows installation.

The built-in `venv` will use the global Python version, (3.11.3 in this case) whilst other virtual environment managers allow per environment Python versions.

## Project Layout

The `pyproject.toml` file sits in the root of the project. Typically there will be the following directories:

- `src` - to contain project source Python files
- `tests` - to contain project test Python files
- `docs` - to contain generated HTML documentation files from Sphinx.
- `{environment_name}` - generated by venv to contain virtual environment files.

The root of the project also contains configuration files for other tools used in the project. These tools can be configured in multiple ways, here it is done with separate `ini` format files although in many cases they can be added to the `pyproject.toml` file, with the notable exception of `flake8`.

I discuss this in more detail in [this blog post](https://ianhopkinson.org.uk/2022/02/understanding-setup-py-setup-cfg-and-pyproject-toml-in-python/).

## Testing

Testing in this project is using the built-in `unittest` library. Tests can be run with:

```shell
python -m unittest -v
```

Visual Studio Code supports Python testing using unittest and pytest.

## Static analysis and formatting tools

This project uses [flake8](https://flake8.pycqa.org/en/latest/) and [pylint](https://github.com/pylint-dev/pylint) for static analysis
 and [black](https://github.com/psf/black) for formatting. These packages can be installed with:

```shell
pip install black flake8 pylint
```

`black` encourages zero configuration on the uses part. If configuration is required it is added as a section to the `pyproject.toml` file, for example:
```ini
[tool.black]
line-length = 100
target-version = ['py311']
include = '\.pyi?$'
extend-exclude = '''
# A regex preceded with ^/ will apply only to files and directories
# in the root of the project.
^/foo.py  # exclude a file named foo.py in the root of the project (in addition to the defaults)
'''
```

`flake8` is unusual in not supporting configuration in `pyproject.toml`, the configuration file for this project looks like this:

```ini
[flake8]
max-line-length = 100
ignore = E203,E501,W503
per-file-ignores = __init__.py:F401
```

`pylint` can be configured either by adding sections to `pyproject.toml` or in a separate configuration file (`.pylintrc`). Examples of configuration these configuration files can be generated using the following commands:

```shell
pylint --generate-toml-config
```

or

```shell
pylint --generate-rcfile
```

This generates a complete set of default configuration options, in practice it is better to simply put changes from default into the configuration file.


Linting and formatting are run using:

```shell
black . --check
flake8 src/ tests/
pylint src/ tests/
```

Typically I use `black` integrated into Visual Studio Code and format on save. `flake8` issues I will always address (even if it is to ignore a rule)
`pylint` messages I will normally consider but necessarily act on.

## Documentation Generation

Documentation for this project is by [sphinx](https://www.sphinx-doc.org/en/master/), the required libraries are installed with:

A `docs` directory is created in the top-level of the project and the following command is run in it to setup sphinx:

```shell
sphinx-quickstart
```

This asks a bunch of questions about the project, the only one where the default response is not good is "Separate source and build directories", it is best to answer "yes" to this.

The configuration for sphinx goes in a Python file `docs/source/conf.py` which is more concise than it used to be. For this project it is modified:

```python
extensions = [
'sphinx.ext.autodoc',
'sphinx_autodoc_typehints',
]
html_theme = "sphinx_rtd_theme"
```

The sphinx documentation is initialised by running the following in the project root:

```shell
sphinx-apidoc -o docs/source/ src
```

And then HTML files are generated with the following, run in the `docs` directory

```shell
make html
```

## Git Bash

A `Makefile` is included in this repository which has targets for installing the package, running tests, running the linters and 
building the documentation. For Git Bash I needed to install `make` using the chocolatey package manager (`choco install make`).


## Visual Studio Code
As a personal choice, I use Visual Studio Code for software development. 

The configuration used for this project for Code is found in the `.vscode` directory of this repo.
