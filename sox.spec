Summary:	A general purpose sound file conversion tool.
Name:		sox
Version:	12.15
Release:	5
Copyright:	distributable
Group:		Applications/Multimedia
Source:		http://home.sprynet.com/sprynet/cbagwell/%{name}-%{version}.tar.gz
Url:		http://home.sprynet.com/sprynet/cbagwell/
Patch0:		sox-12.15-paths.patch
Patch1:		sox-12.15-space.patch
Patch2:		sox-play.patch 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SoX (Sound eXchange) is a sound file format converter for Linux,
UNIX and DOS PCs. The self-described 'Swiss Army knife of sound
tools,' SoX can convert between many different digitized sound
formats and perform simple sound manipulation functions,
including sound effects.

Install the sox package if you'd like to convert sound file formats
or manipulate some sounds.

%package devel
Summary:	The SoX sound file format converter libraries.
Group:		Development/Libraries

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
%{__make} PREFIX=%{_prefix} RPM_OPT_FLAGS="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man{1,3}}

%{__make} install install-lib \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	INSTALL_DIR=$RPM_BUILD_ROOT 

echo "#!/bin/sh" > $RPM_BUILD_ROOT%{_bindir}/soxplay
echo "" >> $RPM_BUILD_ROOT%{_bindir}/soxplay
echo '%{_bindir}/sox $1 -t .au - > /dev/audio' >> $RPM_BUILD_ROOT%{_bindir}/soxplay

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/sox

gzip -9nf Changelog README TIPS TODO CHEAT* \
	$RPM_BUILD_ROOT%{_mandir}/man*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changelog,README,TIPS,TODO,CHEAT*}.gz
%attr(755,root,root) %{_bindir}/sox
%attr(755,root,root) %{_bindir}/play   
%attr(755,root,root) %{_bindir}/rec  
%attr(755,root,root) %{_bindir}/soxplay
%{_mandir}/man1/*.1.gz

%files devel
%defattr(644,root,root,755)
%{_libdir}/libst.a
%{_mandir}/man3/*.3.gz
