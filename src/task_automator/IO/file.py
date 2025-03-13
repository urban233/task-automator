"""
#A* -------------------------------------------------------------------
#B* This file contains source code for the Task-Automator python package.
#-* Python module for github helper functions.
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
import os
import pathlib
import shutil


class File:
  """Container for common filesystem file-based operations."""

  @staticmethod
  def copy(a_source_file_name: str | pathlib.Path, a_dest_file_name: str | pathlib.Path, overwrite: bool = False) -> bool:
    """Copies a file to a new location.

    Args:
      a_source_file_name: The path of the file to copy.
      a_dest_file_name: The destination path of the file to copy.
      overwrite: A boolean indicating whether the file should be overwritten.

    Returns:
      A boolean indicating the success of the operation.
    """
    # <editor-fold desc="Checks">
    if a_source_file_name is None or a_source_file_name == "":
      return False
    if a_dest_file_name is None or a_dest_file_name == "":
      return False
    if overwrite is None:
      return False

    # </editor-fold>
    try:
      if overwrite:
        if pathlib.Path(a_dest_file_name).exists():
          os.remove(a_dest_file_name)
      shutil.copy(a_source_file_name, pathlib.Path(a_dest_file_name))
    except Exception as e:
      return False
    return True

  @staticmethod
  def delete(a_filepath: str | pathlib.Path) -> bool:
    """Deletes a file.

    Args:
      a_filepath: The path of the file to delete.

    Returns:
      A boolean indicating the success of the operation.
    """
    # <editor-fold desc="Checks">
    if a_filepath is None or a_filepath == "":
      return False

    # </editor-fold>
    try:
      os.remove(a_filepath)
    except Exception as e:
      print(e)
      return False
    return True
