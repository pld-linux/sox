#
# Conditional build:	
# bcond_off_alsa - without ALSA support
#
Summary:	A general purpose sound file conversion tool
Name:		sox
Version:	12.17
Release:	1
LIcense:	Distributable
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://home.sprynet.com/sprynet/cbagwell/%{name}-%{version}.tar.gz
Url:		http://home.sprynet.com/sprynet/cbagwell/
Patch0:		%{name}-12.15-paths.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-play.patch
BuildRequires:	libgsm-devel
%{!?bcond_off_alsa:BuildRequires:	alsa-driver-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SoX (Sound eXchange) is a sound file format converter for Linux, UNIX
and DOS PCs. The self-described 'Swiss Army knife of sound tools,' SoX
can convert between many different digitized sound formats and perform
simple sound manipulation functions, including sound effects.

Install the sox package if you'd like to convert sound file formats or
manipulate some sounds.

%package devel
Summary:	The SoX sound file format converter libraries.
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description devel 
This package contains the library needed for compiling applications
which will use the SoX sound file format converter.

Install sox-devel if you want to develop applications which will use
SoX.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure --with-oss-dsp \
	%{!?bcond_off_alsa:--with-alsa-dsp}

%{__make} PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man{1,3}}

%{__make} install install-lib \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	INCDIR=$RPM_BUILD_ROOT%{_includedir} \
	INSTALL_DIR=$RPM_BUILD_ROOT 

echo "#!/bin/sh" > $RPM_BUILD_ROOT%{_bindir}/soxplay
echo "" >> $RPM_BUILD_ROOT%{_bindir}/soxplay
echo '%{_bindir}/sox $1 -t .au - > /dev/audio' >> $RPM_BUILD_ROOT%{_bindir}/soxplay

echo .so play.1 >$RPM_BUILD_ROOT%{_mandir}/man1/rec.1

gzip -9nf Changelog README TODO INSTALL

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz monkey.*
%attr(755,root,root) %{_bindir}/sox
%attr(755,root,root) %{_bindir}/play   
%attr(755,root,root) %{_bindir}/rec  
%attr(755,root,root) %{_bindir}/soxplay
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libst.a
%{_includedir}/st.h
%{_mandir}/man3/*
