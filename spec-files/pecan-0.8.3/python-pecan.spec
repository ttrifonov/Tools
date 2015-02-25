%define name pecan
%define version 0.8.3
%define unmangled_version 0.8.3
%define unmangled_version 0.8.3
%define release 1

Summary: A WSGI object-dispatching web framework, designed to be lean and fast, with few dependancies.
Name: python-pecan
Version: %{version}
Release: %{release}%{?dist}
Source0: pecan-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/pecan-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jonathan LaCour <info@pecanpy.org>
Url: http://github.com/stackforge/pecan

Requires:    python-webob >= 1.3
Requires:    python-mako
Requires:    python-webtest
Requires:    python-logutils
Requires:    python-six
Requires:    python-singledispatch

%description
UNKNOWN

%prep
%setup -n pecan-%{unmangled_version} -n pecan-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
