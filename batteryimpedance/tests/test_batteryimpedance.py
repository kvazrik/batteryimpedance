"""
Unit and regression test for data_proc.py
"""
import errno
import os
import sys
import unittest
from contextlib import contextmanager
from io import StringIO
import numpy as np
import logging
from matplotlib import pyplot as plt
from batteryimpedance.data_analyze import main

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
DISABLE_REMOVE = logger.isEnabledFor(logging.DEBUG)

CURRENT_DIR = os.path.dirname(__file__)
MAIN_DIR = os.path.join(CURRENT_DIR, '..')
PROJ_DIR = os.path.join(MAIN_DIR, 'batteryimpedance')
DATA_DIR = os.path.join(PROJ_DIR, 'data')
SAMPLE_DATA_FILE_LOC1 = os.path.join(PROJ_DIR, 'examplex.csv')
SAMPLE_DATA_FILE_LOC2= os.path.join(PROJ_DIR, 'exampley.csv')

# Assumes running tests from the main directory
DEF_CSV_OUT = os.path.join(MAIN_DIR, 'sample_data_stats.csv')
DEF_PNG_OUT = os.path.join(MAIN_DIR, 'sample_data_stats.png')


class TestMain(unittest.TestCase):

    def test_value_R(self):
        inp=['-csvx',SAMPLE_DATA_FILE_LOC1,'-csvy',SAMPLE_DATA_FILE_LOC2]
        R = main(inp)
        self.assertAlmostEqual(9438, int(R))
