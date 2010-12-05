#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
%define		ecore_ver	1.0.0
%define		evas_ver	1.0.0

Summary:	EFL wrapper for DBus
Summary(pl.UTF-8):	Obudowanie EFL dla systemu DBus
Name:		e_dbus
%define	subver	beta3
Version:	1.0.0
Release:	0.%{subver}.1
License:	BSD
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.%{subver}.tar.bz2
# Source0-md5:	db71600a48b7cd96bebe4eb29b0004aa
URL:		http://enlightenment.org/p.php?p=about/efl
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	dbus-devel >= 0.62
BuildRequires:	ecore-devel >= %{ecore_ver}
BuildRequires:	evas-devel >= %{ecore_ver}
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	dbus-libs >= 0.62
Requires:	ecore-devel >= %{ecore_ver}
Requires:	evas >= %{evas_ver}
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
Requires:	dbus-devel >= 0.62
Requires:	ecore-devel >= %{ecore_ver}
Requires:	evas-devel >= %{evas_ver}

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
%setup -q -n %{name}-%{version}.%{subver}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
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
%attr(755,root,root) %{_bindir}/e_dbus_bluez_test
%attr(755,root,root) %{_bindir}/e_dbus_connman_test
%attr(755,root,root) %{_bindir}/e_dbus_notification_daemon
%attr(755,root,root) %{_bindir}/e_dbus_notify
%attr(755,root,root) %{_bindir}/e_dbus_ofono_test
%attr(755,root,root) %{_bindir}/e_dbus_test
%attr(755,root,root) %{_bindir}/e_dbus_test_client
%attr(755,root,root) %{_bindir}/e_dbus_ukit_test
%attr(755,root,root) %{_libdir}/libebluez.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libebluez.so.1
%attr(755,root,root) %{_libdir}/libeconnman.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libeconnman.so.1
%attr(755,root,root) %{_libdir}/libedbus.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libedbus.so.1
%attr(755,root,root) %{_libdir}/libehal.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libehal.so.1
%attr(755,root,root) %{_libdir}/libenotify.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libenotify.so.1
%attr(755,root,root) %{_libdir}/libeofono.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libeofono.so.1
%attr(755,root,root) %{_libdir}/libeukit.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libeukit.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libebluez.so
%attr(755,root,root) %{_libdir}/libeconnman.so
%attr(755,root,root) %{_libdir}/libedbus.so
%attr(755,root,root) %{_libdir}/libehal.so
%attr(755,root,root) %{_libdir}/libenotify.so
%attr(755,root,root) %{_libdir}/libeofono.so
%attr(755,root,root) %{_libdir}/libeukit.so
%{_libdir}/libebluez.la
%{_libdir}/libeconnman.la
%{_libdir}/libedbus.la
%{_libdir}/libehal.la
%{_libdir}/libeofono.la
%{_libdir}/libeukit.la
%{_libdir}/libenotify.la
%{_includedir}/e_dbus-1
%{_pkgconfigdir}/ebluez.pc
%{_pkgconfigdir}/econnman.pc
%{_pkgconfigdir}/edbus.pc
%{_pkgconfigdir}/ehal.pc
%{_pkgconfigdir}/enotify.pc
%{_pkgconfigdir}/eofono.pc
%{_pkgconfigdir}/eukit.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libebluez.a
%{_libdir}/libeconnman.a
%{_libdir}/libedbus.a
%{_libdir}/libehal.a
%{_libdir}/libenotify.a
%{_libdir}/libeofono.a
%{_libdir}/libeukit.a
%endif
