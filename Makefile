# Use this file to
# 	create a local venv, 
#	activate local venv, 
# 	install requirements,
# 	test python files in local venv,
# 	run python files in local venv,
# 	and, update the requirements.
# Add utility as needed.
# It is expected that you use the Makefile for each of these. However,
# if you would rather activate and use the python code through other means,
# please do so.

# Commands will run as one shell.
.ONESHELL:

SHELL := /bin/bash
ACTIVATE := . .venv/bin/activate && which python3
ENV := source .env/.env

# See https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
ALL: venv install

# Activate venv and install 
INSTALL: venv
	 $(ACTIVATE) && pip3 install -r requirements.txt

# Create venv if it doesn't exist
# test -d venv || virtualenv -p python3 --no-site-packages venv
VENV:
	test -d venv || python3 -m venv .venv

# Requires that tests in a directory have an empty `__init__.py` file.
# See https://stackoverflow.com/a/43733357
TESTS:
	$(ACTIVATE) && python3 -m unittest -v

CLEAN:
	rm -rf venv
	find -iname "*.pyc" -delete

REQUIREMENTS:
	$(ACTIVATE) && pip3 freeze > requirements.txt

# EXECUTE="solution_m/solution_m.py"
EXECUTE:
	$(ACTIVATE) && python3 $(PATH)
