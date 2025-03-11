#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Serialization based on ast.literal_eval
Summary(pl.UTF-8):	Serializacja oparta na ast.literal_eval
Name:		python3-serpent
Version:	1.41
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/serpent/
Source0:	https://files.pythonhosted.org/packages/source/s/serpent/serpent-%{version}.tar.gz
# Source0-md5:	c0ddaba7d2625631968bec8553ab95b1
URL:		https://pypi.org/project/serpent/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytz
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
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

%prep
%setup -q -n serpent-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/serpent.py
%{py3_sitescriptdir}/__pycache__/serpent.cpython-*.py[co]
%{py3_sitescriptdir}/serpent-%{version}-py*.egg-info
