"""
#A* -------------------------------------------------------------------
#B* This file contains source code for the Task-Automator python package.
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
import tasks

AUTOMATION_TREE: dict = {
    "build": {
        "help": "Build components",
        "subcommands": {
            "win-package": {
                "help": "Build Windows ZIP package",
                "func": tasks.build_win_package
            },
            "setup-exe": {
                "help": "Build Inno Setup EXE",
                "func": tasks.build_setup_exe
            },
            "update-src-exe": {
                "help": "Build update source Inno Setup EXE",
                "func": tasks.build_update_src_only_exe
            },
            # ... other build subcommands ...
        }
    }
}


if __name__ == '__main__':
    from task_automator import automator
    automator.Automator(AUTOMATION_TREE).run()
