#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Serialization based on ast.literal_eval
Summary(pl.UTF-8):	Serializacja oparta na ast.literal_eval
Name:		python-serpent
# keep 1.2x here for python2 support
Version:	1.28
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/serpent/
Source0:	https://files.pythonhosted.org/packages/source/s/serpent/serpent-%{version}.tar.gz
# Source0-md5:	15ef8b67c76a6d19bac9c16731a1e62a
URL:		https://pypi.org/project/serpent/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-attrs
BuildRequires:	python-enum34
BuildRequires:	python-pytz
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-attrs
BuildRequires:	python3-pytz
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Serpent is a simple serialization library based on ast.literal_eval.

Because it only serializes literals and recreates the objects using
ast.literal_eval(), the serialized data is safe to transport to other
machines (over the network for instance) and de-serialize it there.

%description -l pl.UTF-8
Serpent to prosta biblioteka serializacji oparta na ast.literal_eval.

Ponieważ serializuje tylko ciągi znaków i tworzy obiekty przy użyciu
ast.literal_eval(), zserializowane dane są bezpieczne do przesyłania
na inne maszyny (np. po sieci) i deserializacji na nich.

%package -n python3-serpent
Summary:	Serialization based on ast.literal_eval
Summary(pl.UTF-8):	Serializacja oparta na ast.literal_eval
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-serpent
Serpent is a simple serialization library based on ast.literal_eval.

Because it only serializes literals and recreates the objects using
ast.literal_eval(), the serialized data is safe to transport to other
machines (over the network for instance) and de-serialize it there.

%description -n python3-serpent -l pl.UTF-8
Serpent to prosta biblioteka serializacji oparta na ast.literal_eval.

Ponieważ serializuje tylko ciągi znaków i tworzy obiekty przy użyciu
ast.literal_eval(), zserializowane dane są bezpieczne do przesyłania
na inne maszyny (np. po sieci) i deserializacji na nich.

%prep
%setup -q -n serpent-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/serpent.py[co]
%{py_sitescriptdir}/serpent-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-serpent
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/serpent.py
%{py3_sitescriptdir}/__pycache__/serpent.cpython-*.py[co]
%{py3_sitescriptdir}/serpent-%{version}-py*.egg-info
%endif
