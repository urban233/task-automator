"""
#A* -------------------------------------------------------------------
#B* This file contains source code for the Py-Automator python package.
#-* Python module for the automator class.
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
import argparse
from typing import Any
from typing import Dict
from typing import Optional


class Automator:
  """Core class for building the automation CLI."""

  def __init__(self, command_tree: Dict[str, Any]) -> None:
    """Constructor."""
    self.parser = argparse.ArgumentParser(description="Build automation tool")
    self.command_tree = command_tree
    self._configure_parser(self.parser, self.command_tree)

  def _configure_parser(self, parent, node: Dict[str, Any], path: Optional[list] = None) -> None:
    """Configures the automation tree parser."""
    path = path or []
    subparsers = parent.add_subparsers(
      title='subcommands',
      dest=' '.join(path)
    )

    for cmd_name, cmd_config in node.items():
      parser = subparsers.add_parser(cmd_name, help=cmd_config.get("help"))

      if "func" in cmd_config:
        # Wrap function to ignore arguments
        original_func = cmd_config["func"]
        parser.set_defaults(func=lambda _: original_func())

      if "subcommands" in cmd_config:
        self._configure_parser(
          parser,
          cmd_config["subcommands"],
          path + [cmd_name]
        )

  def run(self) -> None:
    """Run method that executes any given automation function."""
    args = self.parser.parse_args()
    if hasattr(args, 'func'):
      args.func(None)  # Pass dummy value that will be ignored
    else:
      self.parser.print_help()
