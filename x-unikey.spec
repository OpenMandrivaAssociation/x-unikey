Name:		x-unikey
Summary:	A Vietnamese keyboard input system
Version:	1.0.4
Release:	13
Group:		System/Internationalization
URL:		http://unikey.sourceforge.net/linux.php
Source0:	http://downloads.sourceforge.net/unikey/%{name}-%{version}.tar.bz2
# Fix build with GCC 4.3 (missing include) - AdamW 2008/12
Patch0:		x-unikey-1.0.4-gcc43.patch
Patch1:		x-unikey-1.0.4-gcc44.patch
License:	LGPLv2+
Requires:	locales-vi
BuildRequires:	pkgconfig(x11)

%description
X-Unikey is Unikey ported to Linux and FreeBSD.
X-Unikey lets you type Vietnamese in X Window environment. It has been tested
with many popular programs, such as OpenOffice, emacs, vim, Qt applications,
GTK applications...
X-Unikey has all the features of the Windows version, except that its GUI is
still too simplified. All options are set through configuration file or
keyboard shortcuts.

%prep
%setup -q
%patch0 -p1 -b .gcc43
%patch1 -p1 -b .gcc44

%build
#configure --with-unikey-gtk (default: excluded)
export CFLAGS="%{optflags} -fPIC"
%configure2_5x
# (tv) fix build:
ln -fs /bin/true src/xim/install.sh
%make 

%install
rm -rf %{buildroot}
[[ -d doc/CVS ]] && rm -fr doc/CVS
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc AUTHORS CREDITS ChangeLog README* NEWS INSTALL doc/*
%{_bindir}/unikey
%{_bindir}/ukxim



%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-4mdv2011.0
+ Revision: 671121
- mass rebuild

  + Funda Wang <fwang@mandriva.org>
    - tighten BR

* Mon Aug 24 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.4-3mdv2011.0
+ Revision: 420300
- o fix compilation with gcc 4.4
  o fix libtool issues

* Wed Dec 24 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.4-2mdv2009.1
+ Revision: 318227
- rebuild
- add gcc43.patch: fix build with gcc 4.3 (missing include)
- clean spec

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2008.1
+ Revision: 130602
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel


* Sat Nov 25 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.0.4-1mdv2007.0
+ Revision: 87143
- Import x-unikey

* Fri Nov 24 2006 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.4-1mdv2007.1
- new release
- fix build

* Wed Sep 14 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.0.2-1mdk
- new release
- kill patch 0

* Sat Aug 07 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9.2-2mdk
- stop updating /etc/profile in %%post (Larry Nguyen)

* Thu Aug 05 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9.2-1mdk
- patch 0: fix installing
- fix CVS files in %%doc
- Initial build for Mandrakelinux 10.1 (Larry Nguyen <larry@vnlinux.org>)

