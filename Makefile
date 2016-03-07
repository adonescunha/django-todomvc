export DJANGO_SETTINGS_MODULE=tests.dummy_site.settings
export PYTHONPATH=.

.PHONY: test

test:
	flake8 todomvc --ignore=E124,E501,E127,E128
	coverage run --branch --source=todomvc `which django-admin.py` test tests
	coverage report


clean:
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm -f {} \;
