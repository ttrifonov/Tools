__python=$(shell V=$$(python -V 2>&1 | awk '{ print $$2 }' | sed 's/\(.*\)\..*/\1/g'); if [[ "$$V" < '2.6' ]]; then echo 'python2.6'; else echo 'python$$PY'; fi)


.PHONY: all
all: clean
	$(__python) setup.py build


.PHONY: sdist
sdist: clean
	rm -rf dist/aerospike*.tar.gz
	$(__python) setup.py sdist


.PHONY: rpm
rpm: sdist
	rm -rf ~/rpmbuild/SOURCES/aerospike*.tar.gz
	rm -rf ~/rpmbuild/RPMS/noarch/python-aerospike*.rpm
	rm -rf ~/rpmbuild/SRPMS/python-aerospike*.src.rpm
	cp dist/aerospike*.tar.gz ~/rpmbuild/SOURCES/

	rpmbuild -ba python-aerospike.spec

.PHONY: clean
clean:
	echo "Remove other temporary files..."
	rm -rf easy_install* src/*.egg-info .coverage
	rm -rf build


