# Databricks notebook source
# MAGIC %pip install pytest 

# COMMAND ----------

import pytest
import sys
import os
import test_func

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

# changing directory 
#os.chdir("/Workspace/Repos/awsdatabricks00@gmail.com/bundles/test_folder")
# Run pytest.
retcode = pytest.main([".", "-v", "-p", "no:cacheprovider"])

# Fail the cell execution if there are any test failures.
assert retcode == 0, "The pytest invocation failed. See the log for details."


# COMMAND ----------

import importlib
import glob
import sys

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

# Find test files matching patterns
test_files = glob.glob('./test_*.py') + glob.glob('./*_test.py')

for test_file in test_files:
    # Extract module name (remove path and extension)
    module_name = test_file[2:-3].replace('/', '.')
    
    # Import the module dynamically using importlib
    module = importlib.import_module(module_name)

# Run pytest on the imported test files.
retcode = pytest.main([".", "-v", "-p", "no:cacheprovider"])

# Fail the cell execution if there are any test failures.
assert retcode == 0, "The pytest invocation failed. See the log for details."
    


# COMMAND ----------

import os
print(os.getcwd())


# COMMAND ----------

import importlib
import glob

# Find test files matching patterns
test_files = glob.glob('./test_*.py') + glob.glob('./*_test.py')

for test_file in test_files:
    # Extract module name (remove path and extension)
    module_name = test_file[2:-3].replace('/', '.')

    # Import the module dynamically using importlib
    module = importlib.import_module(module_name)

    # Now you can access the module's attributes and functions
    for name in dir(module):
        if not name.startswith('_'):  # Exclude private attributes
            attr = getattr(module, name)
            print(f"Imported {name}: {attr}")

# COMMAND ----------


