clean:
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

release:
	check-manifest -u -v
	git tag $(shell python setup.py -q version)
	git push origin $(shell python setup.py -q version)
	python setup.py sdist upload
