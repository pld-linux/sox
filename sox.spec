#
# Conditional build:
%bcond_without	alsa	# without ALSA support
#
Summary:	A general purpose sound file conversion tool
Summary(de.UTF-8):	Mehrzweck-Sounddatei-Konvertierungs-Tool
Summary(es.UTF-8):	Herramienta para conversión de archivos de sonido
Summary(fr.UTF-8):	outil général de conversion de fichiers son
Summary(pl.UTF-8):	Program do konwersji plików dźwiękowych
Summary(pt_BR.UTF-8):	Ferramenta para conversão de arquivos de som
Summary(ru.UTF-8):	Утилита общего назначения для работы со звуковыми файлами
Summary(tr.UTF-8):	Genel amaçlı ses dosyası çevirme aracı
Summary(uk.UTF-8):	Утиліта загального призначення для роботи із звуковими файлами
Name:		sox
Version:	13.0.0
Release:	1
License:	distributable
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/sox/%{name}-%{version}.tar.gz
# Source0-md5:	0243d62895caee558b5294d5b78cfbcb
Patch0:		%{name}-gsm.patch
URL:		http://sox.sourceforge.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
#BuildRequires:	flac-devel < 1.1.3
BuildRequires:	lame-libs-devel
BuildRequires:	libgsm-devel
BuildRequires:	libmad-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
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
Summary:	Header files for the SoX sound file format converter library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SoX do konwertowania plików dźwiękowych
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files needed for compiling
applications which will use the SoX sound file format converter.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilacji aplikacji,
wykorzystujących konwerter formatów plików dźwiękowych SoX.

%package static
Summary:	Static SoX sound file format converter library
Summary(pl.UTF-8):	Biblioteka statyczna SoX do konwertowania plików dźwiękowych
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SoX sound file format converter library.

%description static -l pl.UTF-8
Biblioteka statyczna SoX do konwertowania plików dźwiękowych.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_alsa:--disable-alsa-dsp}

%{__make}
#	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo "#!/bin/sh" > $RPM_BUILD_ROOT%{_bindir}/soxplay
echo "" >> $RPM_BUILD_ROOT%{_bindir}/soxplay
echo '%{_bindir}/sox $1 -t .au - > /dev/audio' >> $RPM_BUILD_ROOT%{_bindir}/soxplay

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{play,rec}.1
echo '.so sox.1' > $RPM_BUILD_ROOT%{_mandir}/man1/play.1
echo '.so sox.1' > $RPM_BUILD_ROOT%{_mandir}/man1/rec.1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains only notes, not GPL/LGPL texts
%doc AUTHORS COPYING ChangeLog README src/monkey.*
%attr(755,root,root) %{_bindir}/play
%attr(755,root,root) %{_bindir}/rec
%attr(755,root,root) %{_bindir}/sox
%attr(755,root,root) %{_bindir}/soxplay
%attr(755,root,root) %{_libdir}/libst.so.*.*.*
%{_mandir}/man1/play.1*
%{_mandir}/man1/rec.1*
%{_mandir}/man1/sox.1*
%{_mandir}/man7/soxexam.7*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libst-config
%attr(755,root,root) %{_libdir}/libst.so
%{_libdir}/libst.la
%{_includedir}/st*.h
%{_mandir}/man3/libst.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libst.a
