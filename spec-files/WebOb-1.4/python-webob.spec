%define version 1.4
%define unmangled_version 1.4
%define unmangled_version 1.4
%define release 1

Summary: WSGI request and response object
Name: python-webob
Version: %{version}
Release: %{release}
Source0: WebOb-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/WebOb-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Pylons Project <ianb@colorstudy.com>
Url: http://webob.org/

%description
WebOb provides wrappers around the WSGI request environment, and an
object to help create WSGI responses.

The objects map much of the specified behavior of HTTP, including
header parsing and accessors for other standard parts of the
environment.

You may install the `in-development version of WebOb
<https://github.com/Pylons/webob/zipball/master#egg=WebOb-dev>`_ with
``pip install WebOb==dev`` (or ``easy_install WebOb==dev``).

* `WebOb reference <http://docs.webob.org/en/latest/reference.html>`_
* `Bug tracker <https://github.com/Pylons/webob/issues>`_
* `Browse source code <https://github.com/Pylons/webob>`_
* `Mailing list <http://bit.ly/paste-users>`_
* `Release news <http://docs.webob.org/en/latest/news.html>`_
* `Detailed changelog <https://github.com/Pylons/webob/commits/master>`_


%prep
%setup -n WebOb-%{unmangled_version} -n WebOb-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
