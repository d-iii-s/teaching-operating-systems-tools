Name: mff-nswi004-gdb-mipsel-linux-gnu
Version: 8.2
Release: 1%{?dist}
Summary: Cross-build GDB for mipsel-linux-gnu.

License: GPL
URL: https://www.gnu.org/software/gdb/
Source: https://ftp.gnu.org/gnu/gdb/gdb-8.2.tar.gz

Requires: gmp
Requires: isl
Requires: libmpc
BuildRequires: gmp-devel
BuildRequires: isl-devel
BuildRequires: libmpc-devel
BuildRequires: gcc-c++
BuildRequires: texinfo

%description
Cross-build GDB for mipsel-linux-gnu.
Used at Charles University course NSWI004.


%global debug_package %{nil}

%prep
tar xzf $RPM_SOURCE_DIR/gdb-8.2.tar.gz

%build
cd gdb-8.2
./configure \
  --prefix=/opt/mff-nswi004/ \
  --target=mipsel-linux-gnu \
  --program-prefix=mipsel-linux-gnu- \
  --disable-werror \
  --enable-languages=c,c++ \
  --disable-multilib \
  --enable-interwork \
  --enable-static \
  --disable-nls \
  --disable-shared

%make_build all

%install
cd gdb-8.2
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/opt/mff-nswi004/share/info/
find $RPM_BUILD_ROOT

%files
/opt/mff-nswi004/*

%changelog
