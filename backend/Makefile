install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest -vv --cov=main  tests/test_*.py

format:
	black . main.py tests/*.py

lint:
	pylint --disable=R,C main.py tests/*.py

#container-lint:
#	docker run -rm -i hadolint/hadolint < Dockerfile

refactor:
	format lint

deploy:
	echo "deploy not implemented"

all: install lint test format