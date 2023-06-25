#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	XMP Lite module player library
Summary(pl.UTF-8):	Biblioteka odtwarzacza modułów XMP Lite
Name:		libxmp-lite
Version:	4.6.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://downloads.sourceforge.net/xmp/%{name}-%{version}.tar.gz
# Source0-md5:	cb0ad6481e02a18bddaeb3ecb9e07595
URL:		https://xmp.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libxmp-lite is a lean and lightweight subset of Libxmp that plays MOD,
S3M, XM, and IT modules and retains full compatibility with the
original API. It's intended for games and small or embedded
applications where module format diversity and file depacking are not
required.

%description -l pl.UTF-8
Libxmp-lite to odchudzony, lekki podzbiór kodu Libxmp, odtwarzający
moduły MOD, S3M, XM oraz IT, zachowujący pełną zgodność z oryginalnym
API. Jest przeznaczony do gier oraz małych lub wbudowanych aplikacji,
gdzie szeroki wybór formatów ani dekompresja plików nie są wymagane.

%package devel
Summary:	Header files for XMP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XMP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for XMP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki XMP.

%package static
Summary:	Static XMP library
Summary(pl.UTF-8):	Statyczna biblioteka XMP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XMP library.

%description static -l pl.UTF-8
Statyczna biblioteka XMP.

%prep
%setup -q

%build
%configure \
	%{?with_static_libs:--enable-static}
%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_libdir}/libxmp-lite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmp-lite.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmp-lite.so
%{_includedir}/libxmp-lite
%{_pkgconfigdir}/libxmp-lite.pc
%{_libdir}/cmake/libxmp-lite

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxmp-lite.a
%endif
