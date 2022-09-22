Name: mff-nswi004-gcc-mipsel-linux-gnu
Version: 12.2.0
Release: 1%{?dist}
Summary: Cross-build GCC for mipsel-linux-gnu.

License: GPL
URL: http://gcc.gnu.org
Source: https://ftpmirror.gnu.org/gcc/gcc-12.2.0/gcc-12.2.0.tar.gz

Requires: gmp
Requires: isl
Requires: libmpc
BuildRequires: gmp-devel
BuildRequires: isl-devel
BuildRequires: libmpc-devel
BuildRequires: gcc-c++

%description
Cross-build GCC for mipsel-linux-gnu.
Used at Charles University course NSWI004.


%global debug_package %{nil}

%prep
tar xzf $RPM_SOURCE_DIR/gcc-12.2.0.tar.gz

%build
mkdir build
cd build

# Bypass issues with format-security warnings
fixed_cflags=`echo %{optflags} | sed -e 's/-Werror=format-security/-Wformat-security/g'`

CFLAGS="$fixed_cflags" CXXFLAGS="$fixed_cflags" ../gcc-12.2.0/configure \
    --prefix=/opt/mff-nswi004/ \
    --target=mipsel-linux-gnu \
    --program-prefix=mipsel-linux-gnu- \
    --with-gnu-as \
    --with-gnu-ld \
    --disable-nls \
    --enable-languages=c,c++ \
    --enable-lto \
    --disable-werror \
    --enable-static \
    --disable-shared \
    --without-headers

%make_build all-gcc

%install
cd build
rm -rf $RPM_BUILD_ROOT
make install-gcc DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/opt/mff-nswi004/share/info/
find $RPM_BUILD_ROOT/

%files
/opt/mff-nswi004/*

%changelog
