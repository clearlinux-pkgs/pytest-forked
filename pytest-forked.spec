#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-forked
Version  : 1.3.0
Release  : 20
URL      : https://files.pythonhosted.org/packages/62/92/2d418d7b0c9d68a2e885b66d7f6805f9678ce56ad2b3a77669437b2d139a/pytest-forked-1.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/62/92/2d418d7b0c9d68a2e885b66d7f6805f9678ce56ad2b3a77669437b2d139a/pytest-forked-1.3.0.tar.gz
Summary  : run tests in isolated forked subprocesses
Group    : Development/Tools
License  : MIT
Requires: pytest-forked-license = %{version}-%{release}
Requires: pytest-forked-python = %{version}-%{release}
Requires: pytest-forked-python3 = %{version}-%{release}
Requires: py
Requires: pytest
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
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
Provides: pypi(pytest_forked)
Requires: pypi(py)
Requires: pypi(pytest)

%description python3
python3 components for the pytest-forked package.


%prep
%setup -q -n pytest-forked-1.3.0
cd %{_builddir}/pytest-forked-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595896510
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
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-forked
cp %{_builddir}/pytest-forked-1.3.0/LICENSE %{buildroot}/usr/share/package-licenses/pytest-forked/cf3eaf29116a37a7d9ba773e776104c067c8e5fc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest-forked/cf3eaf29116a37a7d9ba773e776104c067c8e5fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
