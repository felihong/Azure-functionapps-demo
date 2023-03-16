import os
from os.path import dirname
from typing import List
import logging


def main(rootDirectory: str) -> List[str]:
    all_file_paths = []
    # Walk through the file system
    for path, _, files in os.walk(rootDirectory):
        # For each file, add their full-path to the list
        for name in files:
            if name == 'function.json' or name == '__init__.py':
                file_path = os.path.join(path, name)
                all_file_paths.append(file_path)

    logging.info(all_file_paths)
    return all_file_paths