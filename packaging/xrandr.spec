Name:           xrandr
Version:        1.4.0
Release:        0
Summary:        Primitive command line interface to RandR extension
License:        MIT
Group:          Graphics/X Window System
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1001: 	xrandr.manifest
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xrandr) >= 1.3
BuildRequires:  pkgconfig(xrender)

%description
Xrandr is used to set the size, orientation and/or reflection of
the outputs for a screen. It can also set the screen size.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_bindir}/xkeystone

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_bindir}/xrandr
%{_mandir}/man1/xrandr.1%{?ext_man}

%changelog
