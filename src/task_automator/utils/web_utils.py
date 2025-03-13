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
from typing import Union

import requests


def download_file(an_url: str, a_filepath: Union[pathlib.Path, str]) -> bool:
  """Downloads a file from the given URL and saves it to the specified filepath.

  Args:
    an_url: The URL to download.
    a_filepath: The path to the file to download.

  Returns:
    True if the download was successful, False otherwise.
  """
  try:
    response = requests.get(str(an_url), stream=True)
    response.raise_for_status()
    with open(a_filepath, 'wb') as file:
      for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)
    return True
  except requests.RequestException as e:
    print(f"Failed to download file: {e}")
    return False
