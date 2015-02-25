#! /bin/bash

#docker run -i -v /shared:/opt/shared/ -t centos /bin/bash

yum install -y wget gcc-c++ make python-devel openssl-devel python-setuptools

wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
rpm -Uvh epel-release-7*.rpm


yum install -y git vim tar yum install rpm-build

mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SRPMS,SPECS}


git clone https://github.com/ttrifonov/Tools.git

cd Tools/spec-files

# Aerospike

wget https://pypi.python.org/packages/source/a/aerospike/aerospike-1.0.37.tar.gz

tar -xzvf aerospike-1.0.37.tar.gz

cd aerospike-1.0.37

make rpm

yes | cp ~/rpmbuild/RPMS/x86_64/python-aerospike-1.0.37-1.x86_64.rpm /opt/shared/

cd ..

# /Aerospike

# PSUtil

wget https://pypi.python.org/packages/source/p/psutil/psutil-2.2.1.tar.gz#md5=1a2b58cd9e3a53528bb6148f0c4d5244

tar -xzvf psutil-2.2.1.tar.gz

cd psutil-2.2.1

git checkout -- .

make rpm

yes | cp ~/rpmbuild/RPMS/x86_64/python-psutil-2.2.1-1.x86_64.rpm /opt/shared/

cd ..

# /PSUtil

# Pecan

wget https://pypi.python.org/packages/source/p/pecan/pecan-0.8.3.tar.gz#md5=e2b329c5088c2adb1510ac9d1af84bca
tar -xzvf pecan-0.8.3.tar.gz

cd pecan-0.8.3

make rpm

yes | cp ~/rpmbuild/RPMS/noarch/python-pecan-0.8.3-1.noarch.rpm /opt/shared/

cd ..

# /Pecan


# Webob

wget https://pypi.python.org/packages/source/W/WebOb/WebOb-1.4.tar.gz
tar -xzvf WebOb-1.4.tar.gz

cd WebOb-1.4

make rpm

yes | cp ~/rpmbuild/RPMS/noarch/python-webob-1.4-1.noarch.rpm /opt/shared/

cd ..

# /Webob


# Mako

wget https://pypi.python.org/packages/source/M/Mako/Mako-1.0.1.tar.gz
tar -xzvf Mako-1.0.1.tar.gz

cd Mako-1.0.1

sed -ie "s/'Mako'/'mako'/g" setup.py

make rpm

yes | cp ~/rpmbuild/RPMS/noarch/python-mako-1.0.1-1.noarch.rpm /opt/shared/

cd ..

# /Mako



# SingleDispatch

wget https://pypi.python.org/packages/source/s/singledispatch/singledispatch-3.4.0.3.tar.gz#md5=af2fc6a3d6cc5a02d0bf54d909785fcb
tar -xzvf singledispatch-3.4.0.3.tar.gz

cd singledispatch-3.4.0.3

sed -ie "s/'singledispatch'/'python-singledispatch'/g" setup.py

make rpm

yes | cp ~/rpmbuild/RPMS/noarch/python-singledispatch-3.4.0.3-1.noarch.rpm /opt/shared/

cd ..

# /SingleDispatch



# braintree

wget https://pypi.python.org/packages/source/b/braintree/braintree-3.10.0.tar.gz
tar -xzvf braintree-3.10.0.tar.gz

cd braintree-3.10.0

make rpm

yes | cp ~/rpmbuild/RPMS/noarch/python-braintree-3.10.0-1.noarch.rpm /opt/shared/

cd ..

# /braintree



# crontab

wget https://pypi.python.org/packages/source/p/python-crontab/python-crontab-1.9.2.tar.gz
tar -xzvf python-crontab-1.9.2.tar.gz

cd python-crontab-1.9.2

make rpm

yes | cp ~/rpmbuild/RPMS/noarch/python-crontab-1.9.2-1.noarch.rpm /opt/shared/

cd ..

# /crontab



# logutils

wget https://pypi.python.org/packages/source/l/logutils/logutils-0.3.3.tar.gz
tar -xzvf logutils-0.3.3.tar.gz

cd logutils-0.3.3

make rpm

yes | cp ~/rpmbuild/RPMS/noarch/python-logutils-0.3.3-1.noarch.rpm /opt/shared/

cd ..

# /logutils


# logutils

wget https://pypi.python.org/packages/source/a/alembic/alembic-0.7.4.tar.gz
tar -xzvf alembic-0.7.4.tar.gz

cd alembic-0.7.4

make rpm

yes | cp ~/rpmbuild/RPMS/noarch/python-alembic-0.7.4-1.noarch.rpm /opt/shared/

cd ..

# /logutils



# uwsgi

wget https://pypi.python.org/packages/source/u/uWSGI/uwsgi-2.0.9.tar.gz
tar -xzvf uwsgi-2.0.9.tar.gz

cd uwsgi-2.0.9
sed -ie "s/'uWSGI'/'uwsgi'/g" setup.py
sed -ie "s/py_modules=\['uwsgidecorators'\]/py_modules=['uwsgidecorators', 'uwsgiconfig']/g" setup.py

git checkout -- .

UWSGI_PROFILE=default make rpm

yes | cp ~/rpmbuild/RPMS/x86_64/python-uwsgi-2.0.9-1.x86_64.rpm /opt/shared/

cd ..

# /uwsgi

