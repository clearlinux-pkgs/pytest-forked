#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-forked
Version  : 1.0.2
Release  : 6
URL      : https://files.pythonhosted.org/packages/30/be/cb5dc4f0fa5ba121943305f4f235dc1a30fae53daac20094ab89f4618578/pytest-forked-1.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/30/be/cb5dc4f0fa5ba121943305f4f235dc1a30fae53daac20094ab89f4618578/pytest-forked-1.0.2.tar.gz
Summary  : run tests in isolated forked subprocesses
Group    : Development/Tools
License  : MIT
Requires: pytest-forked-license = %{version}-%{release}
Requires: pytest-forked-python = %{version}-%{release}
Requires: pytest-forked-python3 = %{version}-%{release}
Requires: pytest
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
pytest-forked: run each test in a forked subprocess
====================================================

%package license
Summary: license components for the pytest-forked package.
Group: Default

%description license
license components for the pytest-forked package.


%package python
Summary: python components for the pytest-forked package.
Group: Default
Requires: pytest-forked-python3 = %{version}-%{release}

%description python
python components for the pytest-forked package.


%package python3
Summary: python3 components for the pytest-forked package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pytest-forked package.


%prep
%setup -q -n pytest-forked-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550201135
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-forked
cp LICENSE %{buildroot}/usr/share/package-licenses/pytest-forked/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest-forked/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
