#define _disable_lto 1

Name: fossil
Version: 2.10
Release: 1
Source0: https://www.fossil-scm.org/home/uv/%{name}-src-%{version}.tar.gz
Summary: The Fossil SCM system
URL: http://www.fossil-scm.org/
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
%setup -q
# looks like autoconf but isn't
CC="%__cc" CFLAGS="%optflags" ./configure --prefix=%{_prefix} --libdir=%{_libdir} --json --with-zlib=%{_prefix}

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/*
