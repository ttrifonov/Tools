%define version 1.0.0
%define unmangled_version 1.0.0
%define unmangled_version 1.0.0
%define release 1

Summary: A super-fast templating language that borrows the  best ideas from the existing templating languages.
Name: python-mako
Version: %{version}
Release: %{release}
Source0: mako-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/mako-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mike Bayer <mike@zzzcomputing.com>
Url: http://www.makotemplates.org/

Requires:       python-markupsafe >= 0.9.2

%description
=========================
Mako Templates for Python
=========================

Mako is a template library written in Python. It provides a familiar, non-XML 
syntax which compiles into Python modules for maximum performance. Mako's 
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded 
Python (i.e. Python Server Page) language, which refines the familiar ideas
of componentized layout and inheritance to produce one of the most 
straightforward and flexible models available, while also maintaining close 
ties to Python calling and scoping semantics.

Nutshell
========

::

    <%inherit file="base.html"/>
    <%
        rows = [[v for v in range(0,10)] for row in range(0,10)]
    %>
    <table>
        % for row in rows:
            ${makerow(row)}
        % endfor
    </table>

    <%def name="makerow(row)">
        <tr>
        % for name in row:
            <td>${name}</td>\
        % endfor
        </tr>
    </%def>

Philosophy
===========

Python is a great scripting language. Don't reinvent the wheel...your templates can handle it !

Documentation
==============

See documentation for Mako at http://www.makotemplates.org/docs/

License
========

Mako is licensed under an MIT-style license (see LICENSE).
Other incorporated projects may be licensed under different licenses.
All licenses allow for non-commercial and commercial use.


%prep
%setup -n mako-%{unmangled_version} -n mako-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
