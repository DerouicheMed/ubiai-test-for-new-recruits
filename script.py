import io
import logging
import os
import traceback


def this_function_is_in_main_branch():
    print("This function should be kept after merge")

def this_function_is_in_feature_branch_1_only():
    print("This function should be kept after merge with master but not with feature branch 2")

def this_function_is_in_feature_branch():
    print("This function should be kept after merge with master")

