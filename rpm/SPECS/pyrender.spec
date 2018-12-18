%define dist_name	pyrender
%define dist_var	%(cut -d . -f 1-2 version)
%define dist_rel	%(cut -d . -f 3 version)

%define __python python3

Summary: simple render script used jinja2
Name: %{?name_prefix}%{dist_name}
Version: %{dist_var}
Release: %{dist_rel}
License: MIT
Group: Application/Other
URL: https://www.osstech.co.jp
BuildRoot: %{_tmppath}/%{name}-%{version}
Requires: python34
Source0: %{name}-%{version}.%{release}.tar.gz

%description
%(cat README.md)

%prep
rm -rf %{buildroot}
%setup -n %{name}-%{version}.%{release}

%build

%install
make install DISTDIR=%{buildroot} BINDIR=%{_bindir} LIBDIR=%{_libdir} VENV=pyrenderenv
BUILD_VENV_DIR=%{buildroot}%{_libdir}/pyrender/pyrenderenv
# コード内に${buildroot}のフルパスが入っていると/usr/lib/rpm/check-buildrootでエラーになるので
# %{_libdir}等に置き換えている
sed -i -e 's|^VIRTUAL_ENV=.*|VIRTUAL_ENV="%{_libdir}/venv/"|' $BUILD_VENV_DIR/bin/activate
sed -i -e 's|^#!.*$|#!%{_libdir}/pyrender/pyrenderenv/bin/python|' %{buildroot}%{_bindir}/pyrender
sed -i -e 's|^#!.*$|#!%{_libdir}/pyrender/pyrenderenv/bin/python3|' $BUILD_VENV_DIR/bin/*
rm -rf $BUILD_VENV_DIR/bin/activate.csh
rm -rf $BUILD_VENV_DIR/bin/activate.fish
rm -rf $BUILD_VENV_DIR/lib64

%clean
rm -rf %{buildroot}

%files
%attr(0755,root,root) %{_libdir}/pyrender/pyrenderenv/*
%attr(0755,root,root) %{_libdir}/pyrender/requirements.txt
%attr(0755,root,root) %{_bindir}/pyrender

%changelog
* Thu Dec 18 2018 KAWAI Shun <shun@osstech.co.jp> - 1.0.0
- Initial release
