%define dist_name	pyrender
%define dist_var	%(cut -d . -f 1-2 version)
%define dist_rel	%(cut -d . -f 3 version)

Summary: simple render script used jinja2
Name: %{?name_prefix}%{dist_name}
Version: %{dist_var}
Release: %{dist_rel}
License: MIT
Group: Application/Other
URL: https://www.osstech.co.jp
BuildRoot: %{_tmppath}/%{name}-%{version}.%{release}-root
Source0: %{name}-%{version}.%{release}.tar.gz

%description
%(cat README.md)

%prep
rm -rf %{buildroot}
%setup -n %{name}-%{version}.%{release}

%build
python3 -m venv sandbox
source ./sandbox/bin/activate
pip install --upgrade pip setuptools wheel
python setup.py build
deactivate

%install
python3 -m venv sandbox
source ./sandbox/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
python setup.py install \
    -O1 \
    --single-version-externally-managed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    --install-scripts=%{_sbindir} \
    --install-lib=%{_libdir}
deactivate

%clean
rm -rf %{buildroot}

%files

%changelog
* Thu Dec 18 2018 KAWAI Shun <shun@osstech.co.jp> - 1.0.0
- Initial release
