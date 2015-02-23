__python=$(shell V=$$(python -V 2>&1 | awk '{ print $$2 }' | sed 's/\(.*\)\..*/\1/g'); if [[ "$$V" < '2.6' ]]; then echo 'python2.6'; else echo 'python$$PY'; fi)


.PHONY: all
all: clean
	$(__python) setup.py build


.PHONY: sdist
sdist: clean
		rm -rf dist/uwsgi*.tar.gz
		$(__python) setup.py sdist


.PHONY: rpm
rpm: sdist
	rm -rf ~/rpmbuild/SOURCES/uwsgi*.tar.gz
	rm -rf ~/rpmbuild/RPMS/noarch/python-uwsgi*.rpm
	rm -rf ~/rpmbuild/SRPMS/python-uwsgi*.src.rpm
	cp dist/uwsgi*.tar.gz ~/rpmbuild/SOURCES/

	rpmbuild -ba python-uwsgi.spec

.PHONY: clean
clean:
	##  $(__python) setup.py develop --uninstall --install-dir . -m
	echo "Remove other temporary files..."
	rm -rf easy_install* src/*.egg-info .coverage
	rm -rf build

