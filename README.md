# Rosetta - Python

## About

This GitHub repo accompanies a [blog post]() which describes the tooling ecosystem for Python. This repo provides the technical details in a concise form to accompany the more discussive blog post.

## Python interpreter

On Windows Python can be downloaded from [here](https://www.python.org/downloads/).

## Python Package Management

Python package management is typically done using the `pip` package manager, installed with Python.

A Python package is configured using the `pyproject.toml` file, this project includes a minimal `pyproject.toml` file.

Typically Python is run in a virtual environment which can be created, as described below. This very nearly became mandatory, see [PEP-0704](https://peps.python.org/pep-0704/).



## Virtual Environments

Virtual environments can be created using the built-in `venv` library:

```shell
python -m venv {environment_name}
```

It is then activated (on my Windows machine in Git Bash) with:

```shell
source {environment_name}/Scripts/activate
```

I suspect this is a slightly unusual way of invoking since Linux machines will put the activate command in the `bin` subdirectory of the environment.

The built-in `venv` will use the global Python version, (3.11.3 in this case) whilst other virtual environment managers allow per environment Python versions.

## Project Layout

The `pyproject.toml` file sits in the root of the project. Typically there will be the following directories:

- `src` - to contain project source Python files
- `tests` - to contain project test TypeScript files
- `docs` - to contain generated HTML documentation files from TypeDoc.
- `venv` - to contain virtual environment files.

The root of the project also contains configuration files for other tools used in the project. These tools can be configured in multiple ways, here it is done with separate `ini` format files although in many cases they can be added to the `pyproject.toml` file, with the notable exception of `flake8`.

## Testing

Testing in this project is using the built-in `unittest` library. Tests can be run with:

```shell
python -m unittest -v
```

## Static analysis and formatting tools

This project uses [flake8](https://flake8.pycqa.org/en/latest/) and [pylint](https://github.com/pylint-dev/pylint) for static analysis
 and [black](https://github.com/psf/black) for formatting. These packages can be installed with:

```shell
pip install black
pip install flake8
pip install pylint
```

Linting and formatting is run using

```shell
black . --check
flake8 src/ tests/
pylint src/ tests/ || true
```

Typically I use `black` integrated into Visual Studio Code and format on save. `flake8` issues I will always address (even if it is to ignore a rule)
`pylint` messages I will normally consider but necessarily act on.

## Documentation Generation

Documentation for this project is by [TypeDoc](https://typedoc.org/) which is installed with:

```shell
npm install typedoc --save-dev
```

It is invoked with the following which is defined by the "scripts" entry

```shell
npm run make-docs
```

## Visual Studio Code

As a personal choice, I use Visual Studio Code. For this project I installed the [eslint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) extension, the [jest](https://marketplace.visualstudio.com/items?itemName=Orta.vscode-jest) extension, and the [prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) extension.
The TypeScipt support is built in to Visual Studio Code. The configuration for Code is found in the `.vscode` directory of this repo.


# Mypackage

A demonstration Python package layout to go with this blog post.

https://ianhopkinson.org.uk/2022/02/understanding-setup-py-setup-cfg-and-pyproject-toml-in-python/

To install clone this repo, create a virtual environment. Using conda this would be 

`conda create -n tmp python=3.9`

Then activate it:

`conda activate tmp`

The run:

`pip install -e .`