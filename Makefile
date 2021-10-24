format:
	black ./
test:
	flake8 \
		--max-line-length 88 \
		--extend-ignore E203 && \
	python -m pytest \
		--cov=src