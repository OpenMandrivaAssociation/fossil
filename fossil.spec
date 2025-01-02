#define _disable_lto 1

Name: fossil
Version:	2.25
Release:	1
Source0: https://www.fossil-scm.org/home/tarball/8f798279d5f7c3288099915f2ea88c57b6d6039f3f05eac5e237897af33376dc/fossil-src-%{version}.tar.gz
Summary: The Fossil SCM system
URL: https://www.fossil-scm.org/
License: BSD
Group: Development/Tools
BuildRequires: pkgconfig(fuse)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(zlib)
BuildRequires: readline-devel

%description
Fossil is a simple, high-reliability, distributed software
configuration management system

%prep
%autosetup -p1 -n fossil-src-%{version}
# looks like autoconf but isn't
CC="%__cc" CFLAGS="%optflags" ./configure --prefix=%{_prefix} --libdir=%{_libdir} --json --with-zlib=%{_prefix}

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/*
