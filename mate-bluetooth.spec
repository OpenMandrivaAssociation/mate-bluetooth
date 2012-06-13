%define	major	8
%define	gir_maj	1.0
%define	libname	%mklibname %{name} %{major}
%define	girname	%mklibname %{name}-gir %{gir_maj}
%define	devname	%mklibname -d %{name}

Summary:	MATE Bluetooth Subsystem
Name:		mate-bluetooth
Version:	1.2.1
Release:	2
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd412-xml
BuildRequires:	intltool
BuildRequires:	gtk-doc
BuildRequires:	mate-conf
BuildRequires:	mate-common
BuildRequires:	pkgconfig(caja-sendto)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libmatenotify)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(mate-doc-utils)
BuildRequires:	pkgconfig(unique-1.0)

Requires:	gvfs-obexftp
Requires:	bluez
Requires:	obexd

%description
The mate-bluetooth package contains graphical utilities to setup,
monitor and use Bluetooth devices.

%package -n	%{libname}
Group:		System/Libraries
Summary:	MATE bluetooth library

%description -n	%{libname}
Library from MATE-Bluetooth.

%package -n	%{girname}
Group:		System/Libraries
Summary:	GObject Introspection interface for %{name}

%description -n	%{girname}
GObject Introspection interface for %{name}.

%package -n	%{devname}
Group:		Development/C
Summary:	Development libraries and header files from %{name}
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
Development libraries and header files from %{name}

%package -n	caja-sendto-bluetooth
Summary:	Send files from caja to bluetooth
Group:		Graphical desktop/GNOME
Requires:	caja-sendto
Requires:	%{name} = %{version}

%description -n caja-sendto-bluetooth
This application provides integration between caja and bluetooth.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the bluetooth device which you want to send the
file/files.

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--enable-shared \
	--disable-static \
	--disable-desktop-update \
	--disable-icon-update

%make
%install
%makeinstall_std
%find_lang %{name} --all-name --with-gnome

%files -f %{name}.lang
%doc README AUTHORS
%{_sysconfdir}/xdg/autostart/mate-bluetooth-applet.desktop
%{_bindir}/*
%{_libdir}/%{name}/plugins/libgbtgeoclue.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_datadir}/applications/mate-bluetooth-properties.desktop
%{_datadir}/glib-2.0/schemas/org.mate.Bluetooth.gschema.xml
%{_datadir}/MateConf/gsettings/mate-bluetooth
%{_datadir}/%{name}
%{_iconsdir}/mate/*/*/*.*
%{_mandir}/man1/*
# mate help files
%{_datadir}/mate/help

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/MateBluetooth-%{gir_maj}.typelib

%files -n %{devname}
%{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/MateBluetooth-1.0.gir

%files -n caja-sendto-bluetooth
%{_libdir}/caja-sendto/plugins/libnstbluetooth.so
%{_datadir}/MateConf/gsettings/mate-bluetooth-nst
%{_datadir}/glib-2.0/schemas/org.mate.Bluetooth.nst.gschema.xml

