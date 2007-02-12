#
# Conditional build:
%bcond_without	alsa	# without ALSA support
#
Summary:	A general purpose sound file conversion tool
Summary(de.UTF-8):   Mehrzweck-Sounddatei-Konvertierungs-Tool
Summary(es.UTF-8):   Herramienta para conversión de archivos de sonido
Summary(fr.UTF-8):   outil général de conversion de fichiers son
Summary(pl.UTF-8):   Program do konwersji plików dźwiękowych
Summary(pt_BR.UTF-8):   Ferramenta para conversão de arquivos de som
Summary(ru.UTF-8):   Утилита общего назначения для работы со звуковыми файлами
Summary(tr.UTF-8):   Genel amaçlı ses dosyası çevirme aracı
Summary(uk.UTF-8):   Утиліта загального призначення для роботи із звуковими файлами
Name:		sox
Version:	12.18.2
Release:	1
License:	distributable
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/sox/%{name}-%{version}.tar.gz
# Source0-md5:	ba25e512a6c824d6e56d76767a18af99
Patch0:		%{name}-install.patch
Patch1:		%{name}-gsm.patch
URL:		http://sox.sourceforge.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lame-libs-devel
BuildRequires:	libgsm-devel
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

%description -l es.UTF-8
sox se autodenomina "navaja suiza de las herramientas de sonido".
Entiende varios formatos de sonidos digitalizados, pudiendo hacer
conversiones entre estos formatos y desempeñar funciones sencillas de
manejo de sonido.

%description -l pl.UTF-8
SoX (Sound eXchange) jest konwerterem formatów plików dźwiękowych dla
Linuksa, Uniksa i Dosa. SoX może wykonywać konwersję między wieloma
formatami cyfrowego dźwięku. Może także dokonywać prostych manipulacji
na dźwięku, wliczając w to różne efekty dźwiękowe.

%description -l ru.UTF-8
Как говорится в документации, "швейцарский армейский нож звуковых
утилит", sox умеет конвертировать звуковые файлы самых разнообразных
форматов и производить несложную их обработку. С прилагаемым скриптом
также может быть использован для проигрывания звуковых файлов.

%description -l pt_BR.UTF-8
O sox se autodenomina "canivete suíço das ferramentas de som". Ele
entende vários formatos de sons digitalizados, podendo fazer
conversões entre esses formatos e desempenhar funções simples de
manipulação de som.

%description -l uk.UTF-8
В документації цей пакет названо "швейцарським армійським ножиком
звукових утиліт". Він вміє конвертувати звукові файли
найрізноманітніших форматів та виконувати нескладну їх обробку. В
пакет входить скрипт, який можна використовувати для програвання
звукових файлів.

%package devel
Summary:	The SoX sound file format converter libraries
Summary(pl.UTF-8):   Biblioteka SoX do konwertowania plików dźwiękowych
Group:		Development/Libraries

%description devel
This package contains the library needed for compiling applications
which will use the SoX sound file format converter.

Install sox-devel if you want to develop applications which will use
SoX.

%description devel -l es.UTF-8
Bibliotecas que pueden ser usadas para compilar aplicaciones que usen
las bibliotecas del sox.

%description devel -l pl.UTF-8
Ten pakiet zawiera biblioteki potrzebne do kompilacji aplikacji, które
będą wykorzystywały konwerter formatów plików dźwiękowych SoX.

%description devel -l pt_BR.UTF-8
Bibliotecas que podem ser usadas para compilar aplicações que usem as
bibliotecas do sox.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%{__autoheader}
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
