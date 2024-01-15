install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	pylint --disable=R,C s3-list-buckets
test:
	pytest -vv --cov-report term-missing --cov=app test_*.py
format:
	black *.py
