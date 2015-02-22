__python=$(shell V=$$(python -V 2>&1 | awk '{ print $$2 }' | sed 's/\(.*\)\..*/\1/g'); if [[ "$$V" < '2.6' ]]; then echo 'python2.6'; else echo 'python$$PY'; fi)


.PHONY: all
all: clean
	$(__python) setup.py build


.PHONY: sdist
sdist: clean
		rm -rf dist/pecan*.tar.gz
		$(__python) setup.py sdist


.PHONY: rpm
rpm: sdist
	rm -rf ~/rpmbuild/SOURCES/pecan*.tar.gz
	rm -rf ~/rpmbuild/RPMS/noarch/python-pecan*.rpm
	rm -rf ~/rpmbuild/SRPMS/python-pecan*.src.rpm
	cp dist/pecan*.tar.gz ~/rpmbuild/SOURCES/

	rpmbuild -ba python-pecan.spec

.PHONY: clean
clean:
	##  $(__python) setup.py develop --uninstall --install-dir . -m
	echo "Remove other temporary files..."
	rm -rf easy_install* src/*.egg-info .coverage
	rm -rf build

