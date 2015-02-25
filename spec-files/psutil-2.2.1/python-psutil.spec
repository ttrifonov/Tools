%define version 2.2.1
%define unmangled_version 2.2.1
%define unmangled_version 2.2.1
%define release 1

Summary: psutil is a cross-platform library for retrieving information onrunning processes and system utilization (CPU, memory, disks, network)in Python.
Name: python-psutil
Version: %{version}
Release: %{release}%{?dist}
Source0: psutil-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/psutil-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Giampaolo Rodola <g.rodola <at> gmail <dot> com>
Url: https://github.com/giampaolo/psutil

%description

===========
Quick links
===========

- `Home page <https://github.com/giampaolo/psutil>`_
- `Documentation <http://pythonhosted.org/psutil/>`_
- `Download <https://pypi.python.org/pypi?:action=display&name=psutil#downloads>`_
- `Forum <http://groups.google.com/group/psutil/topics>`_
- `Blog <http://grodola.blogspot.com/search/label/psutil>`_
- `What's new <https://github.com/giampaolo/psutil/blob/master/HISTORY.rst>`_

=======
Summary
=======

psutil (python system and process utilities) is a cross-platform library for
retrieving information on **running processes** and **system utilization**
(CPU, memory, disks, network) in Python. It is useful mainly for **system
monitoring**, **profiling and limiting process resources** and **management of
running processes**. It implements many functionalities offered by command line
tools such as: ps, top, lsof, netstat, ifconfig, who, df, kill, free, nice,
ionice, iostat, iotop, uptime, pidof, tty, taskset, pmap. It currently supports
**Linux, Windows, OSX, FreeBSD** and **Sun Solaris**, both **32-bit** and
**64-bit** architectures, with Python versions from **2.4 to 3.4**. Pypi is
also known to work.


%prep
%setup -n psutil-%{unmangled_version} -n psutil-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

