Summary:	Keyboard handling library using XKB data
Name:		libxkbcommon
Version:	0.4.0
Release:	1
License:	other
Group:		Libraries
Source0:	http://xkbcommon.org/download/%{name}-%{version}.tar.xz
# Source0-md5:	bb782f1700e45b4f57c84ef513e3cf85
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Keyboard handling library using XKB data.

%package devel
Summary:	Header files for xkbcommon library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for xkbcommon library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %ghost %{_libdir}/libxkbcommon*.so.0
%attr(755,root,root) %{_libdir}/libxkbcommon*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxkbcommon*.so
%{_includedir}/xkbcommon
%{_pkgconfigdir}/*.pc

