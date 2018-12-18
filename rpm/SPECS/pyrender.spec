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

%install
make install DISTDIR=%{buildroot} BINDIR=%{_bindir} LIBDIR=%{_libdir}

%clean
rm -rf %{buildroot}

%files
%attr(0755,root,root) %dir %{_libdir}/pyrender
%attr(0755,root,root) %{_bindir}/pyrender

%changelog
* Thu Dec 18 2018 KAWAI Shun <shun@osstech.co.jp> - 1.0.0
- Initial release
