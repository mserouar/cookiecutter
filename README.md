# Cookiecutter Python CLI Module template

Cookiecutter template for a Python CLI module.

## Features

* installable single package
* automatic command wrapper creation
* [setuptools_scm][1]: automatic module versioning with Git tags
* [Sphinx][2] docs: documentation ready for generation
* [Docker][3] image: Dockerfile with Makefile ready to encapsulate the module
* [Jenkins][4]: Jenkinsfile ready to build and deploy the module
* [Git][5] (*optional*): Local Git repository initialization
* Virtual environment (*optional*): Virtual environment initialization with [Conda][6], [venv][7]
	or [virtualenvwrapper][8] ([virtualenvwrapper-win][9] for Windows)

## Quickstart

Install the latest Cookiecutter in your global Python distribution if you haven't installed it yet:

```
pip install -U --user cookiecutter
```

**On Windows**, make sure to install [Git for Windows][10] with the option for **CMD.exe enabled**
if you haven't installed it yet. If you are on Linux, simply install Git with your package manager.

Generate a Python CLI module project in the current directory:

```
cookiecutter https://github.com/CAPTEteam/arvalis_toolbox
```

You will be prompted to enter a few configuration variables to initialize the project. The values
between square brackets ``[]`` are the default values that will be used if you don't enter anything.

| Variable | Description |
| --- | --- |
| **python_version** | Choose a Python version for the project. Make sure you have it installed first. |
| **trait_or_name** | Name of the trait or module, e.g. ``Plant Height``. |
| **vector** | Choose a type of vector compatible with this module, e.g. ``Phenomobile``. Choose ``Multi`` if the module is not dependent on a type of vector. |
| **module_name** | Complete name of the module in human-readable form. It will be used to reference the project in the documentation. *A sane default value will be generated*. |
| **module_slug** | Name suitable for the module command and Docker image name (**lowercase** and words separated by "**-**" only). *A sane default value will be generated*. |
| **package_name** | Name suitable for the Python package (**short**, **lowercase** without separation between words). *A sane default value will be generated*. |
| **short_description** | Description of the module's purpose (single paragraph). It will be used in the documentation and as docstring for the package. |
| **init_git_repository** | Initialize a new local Git repository, make an initial commit and tag it as "0.0.0". Disabled if you enter any value but "**y**". *The Git command must be available in the terminal*. |
| **init_virtual_env** | Initialize a new Python virtual environment and install the module in development mode. Disabled if you enter any value but "**y**". |
| **virtual_env** | Choose the virtual environment tool to use. Make sure you have it installed first. *You can leave the default if the virtual environment is disabled*. |

Once the project is generated:

* add modules to the source package
* add the dependencies in the ``install_requires`` of the ``setup.cfg`` file
* add a specific version of the dependencies in the ``requirements.txt`` file
* adapt the source ``cli.main()`` function and add arguments in the parser in ``cli.create_parser()``
* update the ``README.md``
* update the Sphinx documentation in ``docs/source/``

[1]: https://github.com/pypa/setuptools_scm
[2]: http://sphinx-doc.org/
[3]: https://www.docker.com/
[4]: https://jenkins.io/
[5]: https://git-scm.com/
[6]: https://docs.conda.io/projects/conda/en/latest/
[7]: https://docs.python.org/3/library/venv.html
[8]: https://pypi.org/project/virtualenvwrapper/
[9]: https://pypi.org/project/virtualenvwrapper-win/
[10]: https://gitforwindows.org/
