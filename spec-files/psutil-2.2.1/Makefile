__python=$(shell V=$$(python -V 2>&1 | awk '{ print $$2 }' | sed 's/\(.*\)\..*/\1/g'); if [[ "$$V" < '2.6' ]]; then echo 'python2.6'; else echo 'python$$PY'; fi)


.PHONY: all
all: clean
	$(__python) setup.py build


.PHONY: sdist
sdist: clean
		rm -rf dist/psutil*.tar.gz
		$(__python) setup.py sdist


.PHONY: rpm
rpm: sdist
	rm -rf ~/rpmbuild/SOURCES/psutil*.tar.gz
	rm -rf ~/rpmbuild/RPMS/noarch/python-psutil*.rpm
	rm -rf ~/rpmbuild/SRPMS/python-psutil*.src.rpm
	cp dist/psutil*.tar.gz ~/rpmbuild/SOURCES/

	rpmbuild -ba python-psutil.spec

.PHONY: clean
clean:
	##  $(__python) setup.py develop --uninstall --install-dir . -m
	echo "Remove other temporary files..."
	rm -rf easy_install* src/*.egg-info .coverage
	rm -rf build

