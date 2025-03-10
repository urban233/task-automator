from py_automator.examples.automations import *

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
