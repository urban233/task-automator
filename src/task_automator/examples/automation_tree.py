"""
#A* -------------------------------------------------------------------
#B* This file contains source code for the Task-Automator python package.
#-* Python module for an example automation tree.
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
from task_automator.examples.automations import *

# Command structure definition
AUTOMATION_TREE = {
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
