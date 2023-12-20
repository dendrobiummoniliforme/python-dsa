# Use this file to create a local venv, activate it, and install requirements.
# Add utility as needed.

# Commands will run as one shell.
.ONESHELL:

# Set env to bash.
SHELL := /bin/bash

# Since this needs to be called per line.
ACTIVATE_CHECK := . .venv/bin/activate && which python3
ENV_CHECK := source .env/.env

# See https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
all: venv install

# Activate venv and install 
install: venv
	 $(ACTIVATE_CHECK) && pip3 install -r requirements.txt

# Create venv if it doesn't exist
# test -d venv || virtualenv -p python3 --no-site-packages venv
venv:
	test -d venv || python3 -m venv .venv

# Requires that tests in a directory have an empty `__init__.py` file.
# See https://stackoverflow.com/a/43733357
test:
	$(ACTIVATE_CHECK) && python3 -m unittest

clean:
	rm -rf venv
	find -iname "*.pyc" -delete

update-requirements:
	$(ACTIVATE_CHECK) && pip3 freeze > requirements.txt

execute:
	# EXECUTE="solution_m/solution_m.py"
	$(ACTIVATE_CHECK) && python3 $(EXECUTE)
