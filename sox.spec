#
# Conditional build:
%bcond_without	alsa	# without ALSA support
#
Summary:	A general purpose sound file conversion tool
Summary(de):	Mehrzweck-Sounddatei-Konvertierungs-Tool
Summary(es):	Herramienta para conversión de archivos de sonido
Summary(fr):	outil général de conversion de fichiers son
Summary(pl):	Program do konwersji plików d¼wiêkowych
Summary(pt_BR):	Ferramenta para conversão de arquivos de som
Summary(ru):	õÔÉÌÉÔÁ ÏÂÝÅÇÏ ÎÁÚÎÁÞÅÎÉÑ ÄÌÑ ÒÁÂÏÔÙ ÓÏ Ú×ÕËÏ×ÙÍÉ ÆÁÊÌÁÍÉ
Summary(tr):	Genel amaçlý ses dosyasý çevirme aracý
Summary(uk):	õÔÉÌ¦ÔÁ ÚÁÇÁÌØÎÏÇÏ ÐÒÉÚÎÁÞÅÎÎÑ ÄÌÑ ÒÏÂÏÔÉ ¦Ú Ú×ÕËÏ×ÉÍÉ ÆÁÊÌÁÍÉ
Name:		sox
Version:	12.17.9
Release:	1
License:	distributable
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/sox/%{name}-%{version}.tar.gz
# Source0-md5:	a463ef9ff2ec00007a3a42ced9572b03
Patch0:		%{name}-install.patch
URL:		http://sox.sourceforge.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	automake
BuildRequires:	lame-libs-devel
BuildRequires:	libmad-devel
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SoX (Sound eXchange) is a sound file format converter for Linux, UNIX
and DOS PCs. The self-described 'Swiss Army knife of sound tools,' SoX
can convert between many different digitized sound formats and perform
simple sound manipulation functions, including sound effects.

Install the sox package if you'd like to convert sound file formats or
manipulate some sounds.

%description -l es
sox se autodenomina "navaja suiza de las herramientas de sonido".
Entiende varios formatos de sonidos digitalizados, pudiendo hacer
conversiones entre estos formatos y desempeñar funciones sencillas de
manejo de sonido.

%description -l pl
SoX (Sound eXchange) jest konwerterem formatów plików d¼wiêkowych dla
Linuksa, Uniksa i Dosa. SoX mo¿e wykonywaæ konwersjê miêdzy wieloma
formatami cyfrowego d¼wiêku. Mo¿e tak¿e dokonywaæ prostych manipulacji
na d¼wiêku, wliczaj±c w to ró¿ne efekty d¼wiêkowe.

%description -l ru
ëÁË ÇÏ×ÏÒÉÔÓÑ × ÄÏËÕÍÅÎÔÁÃÉÉ, "Û×ÅÊÃÁÒÓËÉÊ ÁÒÍÅÊÓËÉÊ ÎÏÖ Ú×ÕËÏ×ÙÈ
ÕÔÉÌÉÔ", sox ÕÍÅÅÔ ËÏÎ×ÅÒÔÉÒÏ×ÁÔØ Ú×ÕËÏ×ÙÅ ÆÁÊÌÙ ÓÁÍÙÈ ÒÁÚÎÏÏÂÒÁÚÎÙÈ
ÆÏÒÍÁÔÏ× É ÐÒÏÉÚ×ÏÄÉÔØ ÎÅÓÌÏÖÎÕÀ ÉÈ ÏÂÒÁÂÏÔËÕ. ó ÐÒÉÌÁÇÁÅÍÙÍ ÓËÒÉÐÔÏÍ
ÔÁËÖÅ ÍÏÖÅÔ ÂÙÔØ ÉÓÐÏÌØÚÏ×ÁÎ ÄÌÑ ÐÒÏÉÇÒÙ×ÁÎÉÑ Ú×ÕËÏ×ÙÈ ÆÁÊÌÏ×.

%description -l pt_BR
O sox se autodenomina "canivete suíço das ferramentas de som". Ele
entende vários formatos de sons digitalizados, podendo fazer
conversões entre esses formatos e desempenhar funções simples de
manipulação de som.

%description -l uk
÷ ÄÏËÕÍÅÎÔÁÃ¦§ ÃÅÊ ÐÁËÅÔ ÎÁÚ×ÁÎÏ "Û×ÅÊÃÁÒÓØËÉÍ ÁÒÍ¦ÊÓØËÉÍ ÎÏÖÉËÏÍ
Ú×ÕËÏ×ÉÈ ÕÔÉÌ¦Ô". ÷¦Î ×Í¦¤ ËÏÎ×ÅÒÔÕ×ÁÔÉ Ú×ÕËÏ×¦ ÆÁÊÌÉ
ÎÁÊÒ¦ÚÎÏÍÁÎ¦ÔÎ¦ÛÉÈ ÆÏÒÍÁÔ¦× ÔÁ ×ÉËÏÎÕ×ÁÔÉ ÎÅÓËÌÁÄÎÕ §È ÏÂÒÏÂËÕ. ÷
ÐÁËÅÔ ×ÈÏÄÉÔØ ÓËÒÉÐÔ, ÑËÉÊ ÍÏÖÎÁ ×ÉËÏÒÉÓÔÏ×Õ×ÁÔÉ ÄÌÑ ÐÒÏÇÒÁ×ÁÎÎÑ
Ú×ÕËÏ×ÉÈ ÆÁÊÌ¦×.

%package devel
Summary:	The SoX sound file format converter libraries
Summary(pl):	Biblioteka SoX do konwertowania plików d¼wiêkowych
Group:		Development/Libraries

%description devel
This package contains the library needed for compiling applications
which will use the SoX sound file format converter.

Install sox-devel if you want to develop applications which will use
SoX.

%description devel -l es
Bibliotecas que pueden ser usadas para compilar aplicaciones que usen
las bibliotecas del sox.

%description devel -l pl
Ten pakiet zawiera biblioteki potrzebne do kompilacji aplikacji, które
bêd± wykorzystywa³y konwerter formatów plików d¼wiêkowych SoX.

%description devel -l pt_BR
Bibliotecas que podem ser usadas para compilar aplicações que usem as
bibliotecas do sox.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure \
	%{!?with_alsa:--disable-alsa-dsp}

%{__make} \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-lib \
	DESTDIR=$RPM_BUILD_ROOT

echo "#!/bin/sh" > $RPM_BUILD_ROOT%{_bindir}/soxplay
echo "" >> $RPM_BUILD_ROOT%{_bindir}/soxplay
echo '%{_bindir}/sox $1 -t .au - > /dev/audio' >> $RPM_BUILD_ROOT%{_bindir}/soxplay

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/monkey.* Changelog README TODO
%attr(755,root,root) %{_bindir}/[!l]*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libst-config
%{_libdir}/libst.a
%{_includedir}/*.h
%{_mandir}/man3/*
