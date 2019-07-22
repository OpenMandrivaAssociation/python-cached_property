%global pypi_name cached-property

Name:           python-%{pypi_name}
Version:        1.5.1
Release:        %mkrel 1
Summary:        A decorator for caching properties in classes

License:        MIT
URL:            https://pypi.org/project/cached-property
Source0:        http://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%version.tar.gz
BuildArch:      noarch
Group:          Development/Python

BuildRequires:  pkgconfig(python2)
BuildRequires:  python2-setuptools
BuildRequires:  pkgconfig(python3)
BuildRequires:	python-setuptools

%description
A decorator for caching properties in classes

%package -n python2-%{pypi_name}
Summary:	A decorator for caching properties in classes
Group:		Development/Python

%description -n python2-%{pypi_name}
A decorator for caching properties in classes

%prep
%setup -q -n %{pypi_name}-%{version}
cp -a . %{py3dir}

%build
%py2_build

pushd %{py3dir}
%py3_build
popd

%install
pushd %{py3dir} 
%py3_install
popd

%py2_install

%files
%{python3_sitelib}/cached_property.*
%{python3_sitelib}/cached_property-%{version}-py?.?.egg-info/*
%{python3_sitelib}/__pycache__/cached_property*

%files -n python2-%{pypi_name}
%{python2_sitelib}/cached_property.*
%{python2_sitelib}/cached_property-%{version}-py?.?.egg-info/*
