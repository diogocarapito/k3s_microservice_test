install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest -vv --cov=app tests/test_*.py

format:
	black . *.py

lint:
	pylint --disable=R,C app/*.py tests/*.py


all: install lint test format