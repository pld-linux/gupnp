Summary:	UPnP library
Summary(pl.UTF-8):	Biblioteka UPnP
Name:		gupnp
Version:	0.13.4
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.gupnp.org/sources/gupnp/%{name}-%{version}.tar.gz
# Source0-md5:	0d562f5f02534c70c3743b2c514db8ba
URL:		http://gupnp.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.76
BuildRequires:	gir-repository-devel
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gobject-introspection-devel >= 0.6.4
BuildRequires:	gssdp-devel >= 0.7.1
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libsoup-devel >= 2.4.1
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libuuid-devel >= 1.36
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

%description -l pl.UTF-8
GUPnp to zorientowany obiektowo, mający otwarte źródła szkielet do
tworzenia urządzeń i punktów sterujących UPnP, napisany w C z użyciem
bibliotek GObject i libsoup. API GUPnp ma być łatwe w użyciu, wydajne
i elastyczne.

%package devel
Summary:	Header files for gupnp
Summary(pl.UTF-8):	Pliki nagłówkowe gupnp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.18.0
Requires:	gssdp-devel >= 0.7.1
Requires:	libsoup-devel >= 2.4.1
Requires:	libuuid-devel >= 1.36
Requires:	libxml2-devel >= 1:2.6.30

%description devel
This package contains header files for the Linux SDK for UPnP Devices
(gupnp).

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe dla linuksowego pakietu
programistycznego do urządzeń UPnP (gupnp).

%package static
Summary:	Static gupnp libraries
Summary(pl.UTF-8):	Statyczne biblioteki gupnp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gupnp libraries.

%description static -l pl.UTF-8
Statyczne biblioteki gupnp.

%package apidocs
Summary:	gupnp API documentation
Summary(pl.UTF-8):	Dokumentacja API gupnp
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gupnp API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gupnp.

%prep
%setup -q

%build
mkdir m4
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--with-context-manager=network-manager \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gupnp-binding-tool
%attr(755,root,root) %{_libdir}/libgupnp-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgupnp-1.0.so.3
%{_libdir}/girepository-1.0/GUPnP-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgupnp-1.0.so
%{_libdir}/libgupnp-1.0.la
%{_datadir}/gir-1.0/GUPnP-1.0.gir
%{_includedir}/gupnp-1.0
%{_pkgconfigdir}/gupnp-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgupnp-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gupnp
