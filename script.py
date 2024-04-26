
import traceback
import io
import os
import logging


def this_function_is_in_main_branch():
    print("This function should be kept after merge")


def this_function_is_in_feature_branch_2():
    print("This function should be kept after merge with master")