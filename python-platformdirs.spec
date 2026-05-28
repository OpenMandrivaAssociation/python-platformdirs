%define module platformdirs

Name:		python-platformdirs
Summary:	Module for determining appropriate platform-specific dirs
Version:	4.10.0
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/platformdirs/
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(build)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
A small Python module for determining appropriate
platform-specific dirs, e.g. a "user data dir".

%files
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info
