#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
%define		_snap	20080813
%define		ecore_ver	0.9.9.044

Summary:	EFL wrapper for DBus
Summary(pl.UTF-8):	Obudowanie EFL dla systemu DBus
Name:		e_dbus
Version:	0.5.0.044
Release:	0.%{_snap}.1
License:	BSD
Group:		Libraries
Source0:	%{name}-%{version}-%{_snap}.tar.bz2
# Source0-md5:	0032035e32600672febe16d000b4e2ca
URL:		http://enlightenment.org/p.php?p=about/efl
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	dbus-devel >= 0.62
BuildRequires:	ecore-devel >= %{ecore_ver}
BuildRequires:	libtool
BuildRequires:	pkgconfig
Obsoletes:	ecore-dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
EFL wrapper for DBus.

%description -l pl.UTF-8
Obudowanie EFL dla systemu DBus.

%package devel
Summary:	Header files for e_dbus library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki e_dbus
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for e_dbus library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki e_dbus.

%package static
Summary:	Static e_dbus library
Summary(pl.UTF-8):	Statyczna biblioteka e_dbus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static e_dbus library.

%description static -l pl.UTF-8
Statyczna biblioteka e_dbus.

%prep
%setup -q -n %{name}-%{version}-%{_snap}

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
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/e-notify-send
%attr(755,root,root) %{_bindir}/e_dbus_hal
%attr(755,root,root) %{_bindir}/e_dbus_nm
%attr(755,root,root) %{_bindir}/e_dbus_notification_daemon
%attr(755,root,root) %{_bindir}/e_dbus_notify
%attr(755,root,root) %{_bindir}/e_dbus_test
%attr(755,root,root) %{_bindir}/e_dbus_test_client
%attr(755,root,root) %{_libdir}/libedbus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libedbus.so.0
%attr(755,root,root) %{_libdir}/libehal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libehal.so.0
%attr(755,root,root) %{_libdir}/libenm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libenm.so.0
%attr(755,root,root) %{_libdir}/libenotify.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libenotify.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libedbus.so
%attr(755,root,root) %{_libdir}/libehal.so
%attr(755,root,root) %{_libdir}/libenm.so
%attr(755,root,root) %{_libdir}/libenotify.so
%{_libdir}/libedbus.la
%{_libdir}/libehal.la
%{_libdir}/libenm.la
%{_libdir}/libenotify.la
%{_includedir}/E_DBus.h
%{_includedir}/E_Hal.h
%{_includedir}/E_Nm.h
%{_includedir}/E_Notification_Daemon.h
%{_includedir}/E_Notify.h
%{_pkgconfigdir}/edbus.pc
%{_pkgconfigdir}/ehal.pc
%{_pkgconfigdir}/enm.pc
%{_pkgconfigdir}/enotify.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libedbus.a
%{_libdir}/libehal.a
%{_libdir}/libenm.a
%{_libdir}/libenotify.a
%endif
