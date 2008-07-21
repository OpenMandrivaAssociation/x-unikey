%define name x-unikey
%define version 1.0.4
%define release %mkrel 3

Name: %{name}
Summary: A Vietnamese keyboard input for X-Window
Version: %{version}
Release: %{release}
Group: System/Internationalization
URL: http://unikey.sf.net/linux.php
Source: http://prdownloads.sourceforge.net/unikey/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
License: GPL
Requires: locales-vi
BuildRequires:	X11-devel

%description
X-Unikey is Unikey ported to Linux and FreeBSD.
X-Unikey lets you type Vietnamese in X Window environment. It has been tested
with many popular programs, such as OpenOffice, emacs, vim, QT applications,
GTK applications...
X-Unikey has all the features of the Windows version, except that its GUI is
still too simplified. All options are set through configuration file or
keyboard shortcuts.

%prep
%setup -q

%build
#configure --with-unikey-gtk (default: excluded)
CFLAGS="$RPM_OPT_FLAGS -fPIC" %configure 
# (tv) fix build:
ln -fs /bin/true src/xim/install.sh
%make 

%install
rm -rf $RPM_BUILD_ROOT
[[ -d doc/CVS ]] && rm -fr doc/CVS
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%{_bindir}/unikey
%{_bindir}/ukxim
%doc AUTHORS CREDITS ChangeLog README* COPYING NEWS INSTALL doc/*


