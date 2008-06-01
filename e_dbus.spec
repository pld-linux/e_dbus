#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
%define		ecore_ver	0.9.9.043

Summary:	Ecore DBus Library
Summary(pl.UTF-8):	Biblioteka Ecore DBus
Name:		e_dbus
Version:	0.5.0.043
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://download.enlightenment.org/snapshots/2008-05-19/%{name}-%{version}.tar.bz2
# Source0-md5:	68a80552d85b800079387e1008166db4
URL:		http://enlightenment.org/p.php?p=about/libs/eet
BuildRequires:	autoconf
BuildRequires:	automake >= 1.4
BuildRequires:	dbus-devel >= 0.62
BuildRequires:	ecore-devel >= %{ecore_ver}
#BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
#BuildRequires:	zlib-devel
Obsoletes:	ecore-dbus
#Conflicts:	ecore-libs ??
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
Ecore DBus Library.

% description -l pl.UTF-8
Biblioteka Ecore DBus.

%package devel
Summary:	Header files for e_dbus library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki e_dbus
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
#Requires:	libjpeg-devel
#Requires:	zlib-devel

%description devel
Header files for e_dbus library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki e_dbus.

%package static
Summary:	Static Eet library
Summary(pl.UTF-8):	Statyczna biblioteka Eet
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static e_dbus library.

%description static -l pl.UTF-8
Statyczna biblioteka e_dbus.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/e*
%attr(755,root,root) %{_libdir}/libe*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/libe*.la
%{_pkgconfigdir}/e*.pc
%{_includedir}/E_*.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
