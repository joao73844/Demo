# Script to clean all ".pyc" files from the project
# also removes coverage report data
echo "Deleting '.pyc' files"
find . -name \*.pyc -type f
find . -name \*.pyc -type f -delete
echo "Deleting coverage data"
coverage erase