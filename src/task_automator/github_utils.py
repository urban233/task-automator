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
import pathlib
import subprocess
from typing import Optional


def git_clone(an_url: str, a_local_repository_path: Optional[pathlib.Path]):
  """Wrapper function for a typical git clone command.

  Args:
    an_url: The GitHub URL of the repository to clone
    a_local_repository_path (Optional): The path to the local directory the contents of the repository will be downloaded in
  """
  # <editor-fold desc="Checks">
  if an_url.find(".git") == -1:
    raise ValueError("an_url is not a valid GitHub URL.")
  # </editor-fold>
  if a_local_repository_path is None:
    subprocess.run(["git", "clone", an_url])
  else:
    subprocess.run(["git", "clone", an_url, a_local_repository_path])


def git_checkout(a_commit_hash: str, a_local_repository_path: pathlib.Path):
  """Wrapper function for a typical git checkout command.

  Args:
    a_commit_hash: The GitHub commit hash
    a_local_repository_path: The path to the local directory of the repository to run the checkout in
  """
  subprocess.run(["git", "checkout", a_commit_hash], cwd=a_local_repository_path)
