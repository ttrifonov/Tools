%define name uwsgi
%define version 2.0.9
%define unmangled_version 2.0.9
%define unmangled_version 2.0.9
%define release 1

Summary: The uWSGI server
Name: python-uwsgi
Version: %{version}
Release: %{release}%{?dist}
Source0: uwsgi-%{unmangled_version}.tar.gz
License: GPL2
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
Vendor: Unbit <info@unbit.it>

%description
UNKNOWN

%prep
%setup -n uwsgi-%{unmangled_version} -n uwsgi-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%{_bindir}/uwsgi

%exclude /usr/lib/debug/**/**/*.*
%exclude /usr/src/debug/**/*.*

