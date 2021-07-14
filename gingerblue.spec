%define devname		%mklibname %{name} -d

Name:		gingerblue
Version:	1.0.0
Release:	1
Summary:	Free Music Software for GNOME
License:	GPLv3
Group:		Sound
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gingerblue/0.4/%{name}-%{version}.tar.xz
URL:		https://wiki.gnome.org/Apps/Gingerblue
  
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	gettext
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(geocode-glib-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
#BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:	pkgconfig(champlain-0.12)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig

Requires:	geocode-glib
Requires:	glib2
Requires:	gstreamer1.0-plugins-bad
Requires:	gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-good
Requires:	gtk+3
Requires: gtk4
Requires:	hicolor-icon-theme
#Requires:	libchamplain >= 0.12.10
Requires:	pango

%description
Gingerblue is Free Software in development for musicians who want to
compose, record and share original music to the Internet from the
GNOME Desktop.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development
Requires:	%{name} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This package contains the files needed for developing applications with %{name}.

%prep
%autosetup -p1

%build
# Compile with Clang ends with error: error: non-void function 'gb_file_parse_volume' should return a value [-Wreturn-type]
export CC=gcc
export CXX=g++
%configure
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/gingerblue
%{_datadir}/metainfo/gingerblue.appdata.xml
%{_datadir}/applications/gingerblue.desktop
%{_iconsdir}/hicolor/*x*/apps/gingerblue.png

%files -n %{devname}
%{_includedir}/%{name}
