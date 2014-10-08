Summary:	Portable lossless data compression library
Name:		lzo
Version:	2.08
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.oberhumer.com/opensource/lzo/download/%{name}-%{version}.tar.gz
# Source0-md5:	fcec64c26a0f4f4901468f360029678f
URL:		http://www.oberhumer.com/opensource/lzo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	nasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LZO is a portable lossless data compression library written in ANSI C.

%package devel
Summary:	LZO header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for LZO.

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

