Name: mff-nswi004-binutils-mipsel-linux-gnu
Version: 2.30
Release: 1%{?dist}
Summary: Cross-build binary utilities for mipsel-linux-gnu.

License: GPL
URL: https://sourceware.org/binutils
Source: https://ftp.gnu.org/gnu/binutils/binutils-2.30.tar.bz2

Requires: gmp
Requires: isl
Requires: libmpc
BuildRequires: gmp-devel
BuildRequires: isl-devel
BuildRequires: libmpc-devel
BuildRequires: gcc-c++

%description
Cross-build binary utilities for mipsel-linux-gnu.
Used at Charles University course NSWI004.


%global debug_package %{nil}

%prep
tar xjf $RPM_SOURCE_DIR/binutils-2.30.tar.bz2

%build
cd binutils-2.30
./configure \
  --prefix=/opt/mff-nswi004/ \
  --target=mipsel-linux-gnu \
  --program-prefix=mipsel-linux-gnu- \
  --disable-nls \
  --disable-werror \
  --disable-gdb \
  --enable-gold \
  --enable-deterministic-archives \
  --enable-static \
  --with-sysroot \
  --disable-shared

%make_build all

%install
cd binutils-2.30
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT

%files
/opt/mff-nswi004/*

%changelog
