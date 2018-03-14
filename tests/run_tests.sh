# Script to run all tests in the project and produce a coverage report
coverage run -a --source demo -m unittest discover -v && coverage report