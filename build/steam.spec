%global debug_package %{nil}

Name:		steam
Version:	1.0.0.34
Release:	1%{?dist}.1
Summary:	Installer for the Beta of the Steam software distribution service
License:	Steam License Agreement	
URL:		http://www.steampowered.com/
Source0:	http://repo.steampowered.com/steam/archive/precise/steam_%{version}.tar.gz
# Needed to clean the Unity out of the desktop file.
Patch0:		steam-1.0.0.34-fedora.patch
# Add support for Fedora to steamdeps
Patch1:		steam-1.0.0.34-fedora-steamdeps.patch
Patch2:		steam-1.0.0.34-fedora-rpmnames.patch
Patch3:		steam-1.0.0.34-korora-steamdeps.patch

BuildRequires:	desktop-file-utils
BuildRequires:	dos2unix
Requires:	libjpeg-turbo(x86-32)
Requires:	libcurl(x86-32) >= 7.16.2-1
Requires:	libogg(x86-32) >= 1.0
Requires:	pixman(x86-32) >= 0.24.4
Requires:	SDL(x86-32) >= 1.2.10
Requires:	libtheora(x86-32) >= 1.0
Requires:	libvorbis(x86-32) >= 1.1.2
Requires:	alsa-lib(x86-32) >= 1.0.23
Requires:	glibc(x86-32) >= 2.15
Requires:	cairo(x86-32) >= 1.6.0
Requires:	cups-libs(x86-32) >= 1.4.0
Requires:	dbus-libs(x86-32) >= 1.2.14
Requires:	fontconfig(x86-32) >= 2.8.0
Requires:	freetype(x86-32) >= 2.3.9
Requires:	libgcc(x86-32) >= 4.1.1
Requires:	libgcrypt(x86-32) >= 1.4.5
Requires:	gdk-pixbuf2(x86-32) >= 2.22.0
Requires:	glib2(x86-32) >= 2.14.0
Requires:	gtk2(x86-32) >= 2.24.0
Requires:	nspr(x86-32) >= 1.8.0.10
Requires:	nss(x86-32) >= 3.12.3
Requires:	openal-soft(x86-32) >= 1.13
Requires:	pango(x86-32) >= 1.22.0
%if 0%{?fedora} >= 18
Requires:	libpng12(x86-32) >= 1.2.13
%endif
%if 0%{?fedora} == 17
Requires:	libpng-compat(x86-32) >= 1.2.13
%endif
%if 0%{?fedora} <= 16
Requires:	libpng >= 1.2.13
%endif
Requires:	pulseaudio-libs(x86-32) >= 0.99.1
Requires:	libstdc++(x86-32) >= 4.6
Requires:	libX11(x86-32) >= 1.4.99.1
Requires:	libXdmcp(x86-32)
Requires:	libXext(x86-32)
Requires:	libXfixes(x86-32)
Requires:	libXi(x86-32) >= 1.2.99.4
Requires:	libXinerama(x86-32)
Requires:	libXrandr(x86-32) >= 1.2.99.3
Requires:	libXrender(x86-32)
Requires:	zlib(x86-32) >= 1.2.3.3
Requires:	mesa-dri-drivers(x86-32)
Requires:	mesa-libGL(x86-32)

# Derived from the actual libraries downloaded later
# Some of these might be pulled in as dependencies for the above items.
# But eh, better safe than sorry.
# Generated via:
# cd ~/Steam/ubuntu12_32/
# for i in `ldd *.so | cut -f 2 |cut -d " " -f 1 | sed 's|:||g' |sort -n | uniq | grep "\.so."`; do printf "[$i]: " && repoquery -q --whatprovides "$i"; done
Requires:       libasyncns(x86-32)
Requires:       atk(x86-32)
Requires:	avahi-libs(x86-32)
Requires:	libcom_err(x86-32)
Requires:       libdrm(x86-32)
Requires:       mesa-libEGL(x86-32)
Requires:       expat(x86-32)
Requires:	libffi(x86-32)
%if 0%{?fedora} >= 19
Requires:	flac-libs(x86-32)
%else
Requires:       flac(x86-32)
%endif
# I don't think this thing will work on Fedora < 17.
# This is just one reason.
%if 0%{?fedora} >= 17
Requires:	mesa-libgbm(x86-32)
Requires:	mesa-libglapi(x86-32)
%endif
Requires:	libgcrypt(x86-32)
Requires:	gnutls(x86-32)
Requires:	libgpg-error(x86-32)
Requires:	gsm(x86-32)
Requires:	krb5-libs(x86-32)
Requires:	harfbuzz(x86-32)
Requires:	libICE(x86-32)
Requires:	libicu(x86-32)
Requires:	json-c(x86-32)
Requires:	keyutils-libs(x86-32)
Requires:	p11-kit(x86-32)
Requires:	pcre(x86-32)
Requires:	libselinux(x86-32)
Requires:	libSM(x86-32)
Requires:	libsndfile(x86-32)
Requires:	libtasn1(x86-32)
# This is for udev.
%if 0%{?fedora} >= 18
Requires:	systemd-libs(x86-32)
%else
Requires:	libudev(x86-32)
%endif
Requires:	libuuid(x86-32)
%if 0%{?fedora} >= 17
Requires:	libwayland-client(x86-32)
Requires:	libwayland-server(x86-32)
%endif
Requires:	tcp_wrappers-libs(x86-32)
Requires:	libXau(x86-32)
Requires:	libxcb(x86-32)
Requires:	libXcomposite(x86-32)
Requires:	libXcursor(x86-32)
Requires:	libXdamage(x86-32)
Requires:	libXtst(x86-32)
Requires:	libXxf86vm(x86-32)
# Technically, this is "gnome-terminal" or "xterm", but I don't want to pull in gnome unnecessarily.
Requires:	xterm
Requires:	xz

# For the patched steamdeps
Requires:	rpm-python

# This is not in Fedora, but I made a package for it.
Requires:	SDL2(x86-32)

# S3TC texture support
Requires:	libtxc_dxtn(x86-32)

BuildArch:	i686

%description
Installer for the Beta of the Steam software distribution service
Steam is a software distribution service with an online store, automated
installation, automatic updates, achievements, SteamCloud synchronized
savegame and screenshot functionality, and many social features.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
dos2unix %{name}.desktop

%build
# Nothing to build

%install
# mkdir -p %{buildroot}
# cp -a usr %{buildroot}/
make DESTDIR=%{buildroot} install

desktop-file-validate %{buildroot}/%{_datadir}/applications/steam.desktop

%files
%doc COPYING README steam_install_agreement.txt
%{_bindir}/steam
%{_bindir}/steamdeps
%{_libdir}/steam/
%{_datadir}/pixmaps/steam.png
%{_datadir}/pixmaps/steam_tray.png
%{_datadir}/applications/steam.desktop
%{_datadir}/icons/hicolor/*/apps/steam.png
%{_defaultdocdir}/steam/
%{_mandir}/man6/steam.*
# %%ghost %attr(0755,root,root) %{_libdir}/libjpeg.so.8
%post
if [ ! -f /usr/lib/libjpeg.so.8 ]; then
  # Ubuntu has a different soname for this library.
  ln -s /usr/lib/libjpeg.so.62 /usr/lib/libjpeg.so.8
fi
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%changelog
* Thu Feb 28 2013 Tom Callaway <spot@fedoraproject.org> - 1.0.0.22-3
- fix xz name mapping, add as a dependency (thanks to Bob Arendt)

* Thu Feb  7 2013 Tom Callaway <spot@fedoraproject.org> - 1.0.0.22-2
- fix steamdeps to translate deb names to rpm names
- add Requires: xterm

* Thu Jan 31 2013 Tom Callaway <spot@fedoraproject.org> - 1.0.0.22-1
- update to 1.0.0.22
- use the .deb file (thanks to Bob Arendt)

* Tue Jan 8 2013 Tom Callaway <spot@fedoraproject.org> - 1.0.0.18-1
- update to 1.0.0.18

* Wed Nov 7 2012 Tom Callaway <spot@fedoraproject.org> - 1.0.0.14-3
- add more Requires (from downloaded bits, not packaged bits)

* Tue Nov 6 2012 Tom Callaway <spot@fedoraproject.org> - 1.0.0.14-2
- fedora specific libpng conditionalization

* Tue Nov 6 2012 Tom Callaway <spot@fedoraproject.org> - 1.0.0.14-1
- initial Fedora RPM packaging
