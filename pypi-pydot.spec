#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDB4E8AD69A0414CD (peter.nowee@aiba.nl)
#
Name     : pypi-pydot
Version  : 1.4.2
Release  : 44
URL      : https://files.pythonhosted.org/packages/13/6e/916cdf94f9b38ae0777b254c75c3bdddee49a54cc4014aac1460a7a172b3/pydot-1.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/13/6e/916cdf94f9b38ae0777b254c75c3bdddee49a54cc4014aac1460a7a172b3/pydot-1.4.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/13/6e/916cdf94f9b38ae0777b254c75c3bdddee49a54cc4014aac1460a7a172b3/pydot-1.4.2.tar.gz.asc
Summary  : Python interface to Graphviz's Dot
Group    : Development/Tools
License  : MIT
Requires: pypi-pydot-license = %{version}-%{release}
Requires: pypi-pydot-python = %{version}-%{release}
Requires: pypi-pydot-python3 = %{version}-%{release}
Requires: graphviz
BuildRequires : buildreq-distutils3
BuildRequires : pypi(chardet)
BuildRequires : pypi(pyparsing)

%description
[![Build Status](https://www.travis-ci.com/pydot/pydot.svg?branch=master)](https://www.travis-ci.com/pydot/pydot)
[![PyPI](https://img.shields.io/pypi/v/pydot.svg)](https://pypi.org/project/pydot/)

%package license
Summary: license components for the pypi-pydot package.
Group: Default

%description license
license components for the pypi-pydot package.


%package python
Summary: python components for the pypi-pydot package.
Group: Default
Requires: pypi-pydot-python3 = %{version}-%{release}

%description python
python components for the pypi-pydot package.


%package python3
Summary: python3 components for the pypi-pydot package.
Group: Default
Requires: python3-core
Provides: pypi(pydot)
Requires: pypi(chardet)
Requires: pypi(pyparsing)

%description python3
python3 components for the pypi-pydot package.


%prep
%setup -q -n pydot-1.4.2
cd %{_builddir}/pydot-1.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651169797
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pydot
cp %{_builddir}/pydot-1.4.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pydot/6e4a5a00ff44cac512af0e2fcdf8a275b41ff8e2
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pydot/6e4a5a00ff44cac512af0e2fcdf8a275b41ff8e2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
