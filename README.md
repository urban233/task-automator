# Py-Automator - Declarative CLI Automation Framework
[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

### Supported Platforms

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

[**Overview**](#overview)
| [**What is Py-Automator?**](#what-is-py-automator)
| [**Features**](#features)
| [**Installation**](#installation)
| [**Build**](#build)
| [**Defining Commands**](#defining-commands)
| [**License**](#license)

> [!IMPORTANT]
> 📣 **As of March 2025 Py-Automator is still in early development.** 📣
>
>
> Py-Automator is a best-effort open project library. This means that support is not
> guaranteed and how long the project will be maintained is unknown.

## What is Py-Automator?

> Py-Automator is a modern Python framework for building declarative command-line interfaces<br> 
> with nested subcommands, designed for automation workflows and build systems.

Py-Automator is implemented in pure Python that enables scripting of more 
complicated tasks.


## Features
- 🚀 **Declarative Command Tree** - Define CLI structure through simple nested dictionaries
- 🛠 **Zero Boilerplate** - Focus on business logic, not argument parsing
- 📚 **Automatic Help Generation** - Built-in help system with hierarchical documentation
- 🌳 **Hierarchical Commands** - Support for unlimited nested subcommands
- 🖥 **Cross-Platform** - Works on Windows, Linux, and macOS

## Installation

You can use pip to install Py-Automator
```shell
pip install py-automator
```

## Build

Py-Automator uses Poetry for its build process. To build the wheel file 
and source distribution run:
```shell
poetry build
```

## Defining Commands

Create your command structure in a Python module:

```python
...

def setup_dev_env():
    """Initialize development environment"""
    print("Installing dependencies...")

AUTOMATION_TREE = {
    "setup-dev-env": {
        "help": "Initialize development environment",
        "func": setup_dev_env
    },
    "build": {
        "help": "Build artifacts",
        "subcommands": {
            "win-package": {
                "help": "Create Windows deployment package",
                "func": build_windows_package
            },
            "setup-exe": {
                "help": "Generate installer executable",
                "func": create_installer
            }
        }
    }
}

if __name__ == "__main__":
  from py_automator import automator
  automator.Automator(AUTOMATION_TREE).run()
```

## License

This project is licensed under the BSD-3 License - see the [LICENSE](LICENSE) file for details.
