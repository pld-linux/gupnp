#
# Conditional build:
%bcond_without	apidocs	# gtk-doc based API documentation
%bcond_without	vala	# Vala API

Summary:	UPnP library based on GObject and libsoup
Summary(pl.UTF-8):	Biblioteka UPnP oparta na bibliotekach GObject i libsoup
Name:		gupnp
# note: 1.4.x is stable libsoup 2.x based version; for libsoup3 based 1.6+ see gupnp1.6.spec
Version:	1.4.4
Release:	4
License:	LGPL v2+
Group:		Libraries
Source0:	https://download.gnome.org/sources/gupnp/1.4/%{name}-%{version}.tar.xz
# Source0-md5:	f73c965454a5a37c1b18ca8a11bebbbf
Patch0:		meson.patch
URL:		https://wiki.gnome.org/Projects/GUPnP
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd44-xml
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	glib2-devel >= 1:2.66
BuildRequires:	gobject-introspection-devel >= 1.36.0
BuildRequires:	gssdp-devel >= 1.3.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.14}
BuildRequires:	libsoup-devel >= 2.48.0
BuildRequires:	libuuid-devel >= 1.36
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 2:0.20}
%{?with_vala:BuildRequires:	vala-gssdp >= 1.3.0}
BuildRequires:	xz
Requires:	glib2 >= 1:2.66
Requires:	gssdp >= 1.3.0
Requires:	libsoup >= 2.48.0
Requires:	libuuid >= 1.36
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
Requires:	glib2-devel >= 1:2.66
Requires:	gssdp-devel >= 1.3.0
Requires:	libsoup-devel >= 2.48.0
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
BuildArch:	noarch

%description apidocs
gupnp API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gupnp.

%package -n vala-gupnp
Summary:	Vala API for gupnp library
Summary(pl.UTF-8):	API języka Vala dla biblioteki gupnp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.20
Requires:	vala-gssdp >= 1.3.0
BuildArch:	noarch

%description -n vala-gupnp
Vala API for gupnp library.

%description -n vala-gupnp -l pl.UTF-8
API języka Vala dla biblioteki gupnp.

%prep
%setup -q
%patch -P0 -p1

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' tools/gupnp-binding-tool-1.2

%build
%meson \
	-Dcontext_manager=network-manager \
	%{?with_apidocs:-Dgtk_doc=true}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/gupnp-binding-tool-1.2
%attr(755,root,root) %{_libdir}/libgupnp-1.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgupnp-1.2.so.1
%{_libdir}/girepository-1.0/GUPnP-1.2.typelib
%{_mandir}/man1/gupnp-binding-tool-1.2.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgupnp-1.2.so
%{_datadir}/gir-1.0/GUPnP-1.2.gir
%{_includedir}/gupnp-1.2
%{_pkgconfigdir}/gupnp-1.2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgupnp-1.2.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gupnp
%endif

%if %{with vala}
%files -n vala-gupnp
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gupnp-1.2.deps
%{_datadir}/vala/vapi/gupnp-1.2.vapi
%endif
