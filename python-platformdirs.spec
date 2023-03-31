Name:		python-platformdirs
Version:	2.5.2
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/p/platformdirs/platformdirs-%{version}.tar.gz
Summary:	A small Python module for determining appropriate platform-specific dirs, e.g. a user data dir.
URL:		https://pypi.org/project/platformdirs/
License:	GPL
Group:		Development/Python
BuildRequires:	python3dist(build)
BuildRequires:	python3dist(hatchling)
BuildRequires:	python3dist(hatch-vcs)
BuildRequires:	python-pip
BuildArch:	noarch

%description
A small Python module for determining appropriate platform-specific dirs, e.g. a "user data dir".

%prep
%autosetup -p1 -n platformdirs-%{version}

%build
python -m build --wheel --no-isolation

%install
pip install --root=%{buildroot} --no-deps --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links dist dist/*.whl

%files
%{py_puresitedir}/platformdirs
%{py_puresitedir}/platformdirs*info
