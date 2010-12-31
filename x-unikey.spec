Name:		x-unikey
Summary:	A Vietnamese keyboard input system
Version:	1.0.4
Release:	%{mkrel 3}
Group:		System/Internationalization
URL:		http://unikey.sourceforge.net/linux.php
Source0:	http://downloads.sourceforge.net/unikey/%{name}-%{version}.tar.bz2
# Fix build with GCC 4.3 (missing include) - AdamW 2008/12
Patch0:		x-unikey-1.0.4-gcc43.patch
Patch1:		x-unikey-1.0.4-gcc44.patch
Buildroot:	%{_tmppath}/%{name}-buildroot
License:	LGPLv2+
Requires:	locales-vi
BuildRequires:	libx11-devel

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

