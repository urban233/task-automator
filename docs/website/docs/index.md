# Task-Automator - Declarative CLI Automation Framework
[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

### Supported Platforms

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

[**Overview**](#overview)
| [**What is Task-Automator?**](#what-is-task-automator)
| [**Features**](#features)
| [**Installation**](#installation)
| [**Build**](#build)
| [**Defining Commands**](#defining-commands)
| [**License**](#license)

> [!IMPORTANT]
> 📣 **As of March 2025 Task-Automator is still in early development.** 📣
>
>
> Task-Automator is a best-effort open project library. This means that support is not
> guaranteed and how long the project will be maintained is unknown.

## What is Task-Automator?

> Task-Automator is a modern Python framework for building declarative command-line interfaces<br>
> with nested subcommands, designed for automation workflows and build systems.

Task-Automator is implemented in pure Python that enables scripting of more
complicated tasks.


## Features
- 🚀 **Declarative Command Tree** - Define CLI structure through simple nested dictionaries
- 🛠 **Zero Boilerplate** - Focus on business logic, not argument parsing
- 📚 **Automatic Help Generation** - Built-in help system with hierarchical documentation
- 🌳 **Hierarchical Commands** - Support for unlimited nested subcommands
- 🖥 **Cross-Platform** - Works on Windows, Linux, and macOS
- 📚 **Filesystem & Web utils**: Utility functions for filesystem operations and web

## Installation

You can use pip to install Task-Automator
```shell
pip install task-automator
```

## Build

Task-Automator uses Poetry for its build process. To build the wheel file
and source distribution run:
```shell
poetry build
```

## Defining Commands

Create your automation structure in a Python module (like `my_automator.py`):

```python
...
import build_macos_wheel
import build_macos_exe
import build_macos_so
import run_pytest
import dev_env


AUTOMATION_TREE = {
  "setup": {
    "help": "Setup automations",
    "subcommands": {
      "dev-env": {
        "help": "Sets up the development environment",
        "func": dev_env.setup_dev_env
      }
    }
  },
  "build": {
    "help": "Build targets",
    "subcommands": {
      "wheel": {
        "help": "Builds the Python wheel file",
        "func": build_macos_wheel.build_wheel
      },
      "exe": {
        "help": "Creates a frozen Python application",
        "func": build_macos_exe.build
      },
      "so": {
        "help": "Compiles the _cmd module from source",
        "func": build_macos_so.build_cmd_module
      }
    }
  },
  "test": {
    "help": "Runs all tests under the tests/ directory using pytest.",
    "func": run_pytest.run_pytest_suite
  }
}


if __name__ == "__main__":
  from task_automator import automator
  automator.Automator(AUTOMATION_TREE).run()
```

### Important Note
If you connect your automation functions in the tree using the `func` key,
you **must NOT** add parenthesis after the function name! Otherwise, it will
sequentially execute your tree and ignore all passed arguments.

## License

This project is licensed under the BSD-3 License - see the [LICENSE](LICENSE) file for details.
