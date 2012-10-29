Summary:	LZO - a real-time data compression library
Name:		lzo
Version:	2.06
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.oberhumer.com/opensource/lzo/download/%{name}-%{version}.tar.gz
# Source0-md5:	95380bd4081f85ef08c5209f4107e9f8
URL:		http://www.oberhumer.com/opensource/lzo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	nasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LZO is a portable lossless data compression library written in ANSI C.
It implements a number of algorithms with the following features:
- Decompression is simple and *very* fast.
- Requires no memory for decompression.
- Compression is pretty fast.
- Requires 64 kB of memory for compression.
- Allows you to dial up extra compression at a speed cost in the
  compressor. The speed of the decompressor is not reduced.
- Includes compression levels for generating pre-compressed data which
  achieve a quite competitive compression ratio.
- There is also a compression level which needs only 8 kB for
  compression.
- Supports overlapping compression and in-place decompression.
- Algorithm is thread safe.
- Algorithm is lossless.

%package devel
Summary:	LZO header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for LZO.

%package static
Summary:	LZO static library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static LZO library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--enable-asm		\
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS README THANKS doc/LZO.FAQ doc/LZO.TXT
%attr(755,root,root) %ghost %{_libdir}/liblzo2.so.2
%attr(755,root,root) %{_libdir}/liblzo2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/LZOAPI.TXT
%attr(755,root,root) %{_libdir}/liblzo2.so
%{_libdir}/liblzo2.la
%{_includedir}/lzo

%files static
%defattr(644,root,root,755)
%{_libdir}/liblzo2.a
