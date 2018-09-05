# encoding: utf-8

from pathlib import Path
import logging

from .creator import Creator
from .definition import Definition

logging.getLogger(__name__).addHandler(logging.NullHandler())

this_dir = Path(__file__)
MODULE_DIR = this_dir.parent
SCRIPT_DIR = MODULE_DIR.parent
EXAMPLES_DIR = SCRIPT_DIR / 'examples'