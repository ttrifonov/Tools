%define name braintree
%define version 3.10.0
%define unmangled_version 3.10.0
%define release 1

Summary: Braintree Python Library
Name: python-braintree
Version: %{version}
Release: %{release}%{?dist}
Source0: braintree-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Braintree <support@braintreepayments.com>
Url: https://www.braintreepayments.com/docs/python

%description
UNKNOWN

%prep
%setup -n braintree-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
