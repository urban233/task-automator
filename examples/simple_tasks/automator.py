"""
#A* -------------------------------------------------------------------
#B* This file contains source code for the Py-Automator python package.
#-* Python module for an consumer example.
#-* -------------------------------------------------------------------
#C* Copyright 2025 by Martin Urban.
#D* -------------------------------------------------------------------
#E* It is unlawful to modify or remove this copyright notice.
#F* -------------------------------------------------------------------
#G* Please see the accompanying LICENSE file for further information.
#H* -------------------------------------------------------------------
#I* Additional authors of this source file include:
#-*
#-*
#-*
#Z* -------------------------------------------------------------------
"""

def setup_dev_env():
    print("Setting up dev environment...")


def build_win_package():
    print("Building Windows package...")


def clean_build_setup_exe():
    print("Cleaning build setup exe...")


def build_setup_exe():
    print("Building setup exe...")


def build_update_src_only_exe():
    print("Building update source only exe...")


AUTOMATION_TREE: dict = {
    "setup-dev-env": {
        "help": "Installs build dependencies",
        "func": setup_dev_env
    },
    "clean": {
        "help": "Cleans the inno setup build directory",
        "func": clean_build_setup_exe
    },
    "build": {
        "help": "Build components",
        "subcommands": {
            "win-package": {
                "help": "Build Windows ZIP package",
                "func": build_win_package
            },
            "setup-exe": {
                "help": "Build Inno Setup EXE",
                "func": build_setup_exe
            },
            "update-src-exe": {
                "help": "Build update source Inno Setup EXE",
                "func": build_update_src_only_exe
            },
            # ... other build subcommands ...
        }
    }
}


if __name__ == '__main__':
    from py_automator import automator
    automator.Automator(AUTOMATION_TREE).run()
