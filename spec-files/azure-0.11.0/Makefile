__python=$(shell V=$$(python -V 2>&1 | awk '{ print $$2 }' | sed 's/\(.*\)\..*/\1/g'); if [[ "$$V" < '2.6' ]]; then echo 'python2.6'; else echo 'python$$PY'; fi)


.PHONY: all
all: clean
	$(__python) setup.py build


.PHONY: sdist
sdist: clean
	rm -rf dist/azure*.tar.gz
	$(__python) setup.py sdist


.PHONY: rpm
rpm: sdist
	rm -rf ~/rpmbuild/SOURCES/azure*.tar.gz
	rm -rf ~/rpmbuild/RPMS/noarch/python-azure*.rpm
	rm -rf ~/rpmbuild/SRPMS/python-azure*.src.rpm
	cp dist/azure*.tar.gz ~/rpmbuild/SOURCES/

	rpmbuild -ba python-azure.spec

.PHONY: clean
clean:
	##  $(__python) setup.py develop --uninstall --install-dir . -m
	echo "Remove other temporary files..."
	rm -rf easy_install* src/*.egg-info .coverage
	rm -rf build

