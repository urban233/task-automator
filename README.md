# Py-Automator - Declarative CLI Automation Framework
[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-BSD-blue.svg)](https://opensource.org/licenses/MIT)

A modern Python framework for building declarative command-line interfaces with nested subcommands, designed for automation workflows and build systems.

## Features

- 🚀 **Declarative Command Tree** - Define CLI structure through simple nested dictionaries
- 🛠 **Zero Boilerplate** - Focus on business logic, not argument parsing
- 📚 **Automatic Help Generation** - Built-in help system with hierarchical documentation
- 🌳 **Hierarchical Commands** - Support for unlimited nested subcommands
- 🖥 **Cross-Platform** - Works on Windows, Linux, and macOS

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
