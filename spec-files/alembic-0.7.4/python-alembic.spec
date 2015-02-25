%define version 0.7.4
%define unmangled_version 0.7.4
%define unmangled_version 0.7.4
%define release 1

Summary: A database migration tool for SQLAlchemy.
Name: python-alembic
Version: %{version}
Release: %{release}%{?dist}
Source0: alembic-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/alembic-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mike Bayer <mike@zzzcomputing.com>
Url: http://bitbucket.org/zzzeek/alembic

%description
Alembic is a new database migrations tool, written by the author
of `SQLAlchemy <http://www.sqlalchemy.org>`_.  A migrations tool
offers the following functionality:

* Can emit ALTER statements to a database in order to change
  the structure of tables and other constructs
* Provides a system whereby "migration scripts" may be constructed;
  each script indicates a particular series of steps that can "upgrade" a
  target database to a new version, and optionally a series of steps that can
  "downgrade" similarly, doing the same steps in reverse.
* Allows the scripts to execute in some sequential manner.

Documentation and status of Alembic is at http://readthedocs.org/docs/alembic/.



%prep
%setup -n alembic-%{unmangled_version} -n alembic-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
