>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For Python 2.7
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

to run tests: execute 'run_tests.sh'
to clear garbadge files: execute 'clean.sh'

>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>	Using the Command Line
>>>>>>>>>>>>>>>>>>>>>>>>>>

./run_tests.sh
./clean.sh

>>> IMPORTANT <<<
All test modules names must start with "test_" and should be followed with the
name of the module in test.

To run all tests, execute:

	python -m unittest discover -v

To run each test module individually:

	python -m unittest -v MODULE_NAME

>>> IMPORTANT <<<
do NOT write 'MODULE_NAME.py' the '.py' messes everything up


If you want to check code coverage install 'coverage'
>>> pip install coverage

then you can execute (from the 'tests' folder):

	coverage run -a --source TARGET_MODULE unittest discover -v && coverage report