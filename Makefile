init:
	pip install -r requirements.txt
build:
	pyinstaller -F -w --argv-emulation -n ics-cleaner ics-cleaner/core.py