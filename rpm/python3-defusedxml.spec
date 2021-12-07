# Adapted for SailfishOS
# + Disable check by default
# + Remove redundant python-defusedxml

%define pypi_name    defusedxml
%global base_version 0.7.1
#global prerel       ...
%global upstream_version %{base_version}%{?prerel}
Name:           python3-%{pypi_name}
Version:        0.7.1
Release:        1
Summary:        XML bomb protection for Python stdlib modules
License:        Python
URL:            https://github.com/tiran/defusedxml
Source0:        %{name}-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description
The defusedxml package contains several Python-only workarounds and fixes for
denial of service and other vulnerabilities in Python's XML libraries. In order
to benefit from the protection you just have to import and use the listed
functions / classes from the right defusedxml module instead of the original
module.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%py3_build

%install
%py3_install

%check
%if %{with check}
%{python3} tests.py
%endif

%files -n python3-%{pypi_name}
%doc README.txt CHANGES.txt
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{upstream_version}-py%{python3_version}.egg-info/
