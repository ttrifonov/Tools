%define name logutils
%define version 0.3.3
%define unmangled_version 0.3.3
%define release 1

Summary: Logging utilities
Name: python-logutils
Version: %{version}
Release: %{release}%{?dist}
Source0: logutils-%{unmangled_version}.tar.gz
License: Copyright (C) 2010-2013 by Vinay Sajip. All Rights Reserved. See LICENSE.txt for license.
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Vinay Sajip <vinay_sajip@red-dove.com>
Url: http://code.google.com/p/logutils/

%description
The logutils package provides a set of handlers for the Python standard
library's logging package.

Some of these handlers are out-of-scope for the standard library, and
so they are packaged here. Others are updated versions which have
appeared in recent Python releases, but are usable with older versions
of Python and so are packaged here.

The latest version of logutils can be found at:

  http://code.google.com/p/logutils/



%prep
%setup -n logutils-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
