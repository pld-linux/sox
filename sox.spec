Summary: A general purpose sound file conversion tool.
Name: sox
Version: 12.15
Release: 5
Copyright: distributable
Group: Applications/Multimedia
Source: http://home.sprynet.com/sprynet/cbagwell/sox-12.15.tar.gz
Url: http://home.sprynet.com/sprynet/cbagwell/
Patch0: sox-12.15-paths.patch
Patch1: sox-12.15-space.patch
Patch2: sox-play.patch 
BuildRoot: /var/tmp/sox-root

%description
SoX (Sound eXchange) is a sound file format converter for Linux,
UNIX and DOS PCs. The self-described 'Swiss Army knife of sound
tools,' SoX can convert between many different digitized sound
formats and perform simple sound manipulation functions,
including sound effects.

Install the sox package if you'd like to convert sound file formats
or manipulate some sounds.

%package -n  sox-devel
Summary: The SoX sound file format converter libraries.
Group: Development/Libraries

%description -n sox-devel 
This package contains the library needed for compiling applications
which will use the SoX sound file format converter.

Install sox-devel if you want to develop applications which will use
SoX.

%prep
%setup -q 
%patch0 -p1 -b .sox
%patch1 -p1 -b .space
%patch2 -p1 -b .play

%build
make PREFIX=/usr RPM_OPT_FLAGS="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT/usr/lib/
mkdir -p $RPM_BUILD_ROOT/usr/man/man1/
mkdir -p $RPM_BUILD_ROOT/usr/man/man3/

make PREFIX=$RPM_BUILD_ROOT/usr install INSTALL_DIR=$RPM_BUILD_ROOT 
make PREFIX=$RPM_BUILD_ROOT/usr install-lib 

echo "#!/bin/sh" > $RPM_BUILD_ROOT/usr/bin/soxplay
echo "" >> $RPM_BUILD_ROOT/usr/bin/soxplay
echo '/usr/bin/sox $1 -t .au - > /dev/audio' >> $RPM_BUILD_ROOT/usr/bin/soxplay
chmod 755 $RPM_BUILD_ROOT/usr/bin/soxplay

strip $RPM_BUILD_ROOT/usr/bin/sox

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changelog README TIPS TODO INSTALL CHEAT*
/usr/bin/sox
/usr/bin/play   
/usr/bin/rec  
/usr/bin/soxplay
/usr/man/man1/sox.1
%files -n sox-devel
%defattr(-,root,root)
/usr/lib/libst.a
