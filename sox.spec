#
# Conditional build:
%bcond_without	alsa		# ALSA support
%bcond_without	gomp		# OpenMP support
%bcond_without	pulseaudio	# PulseAudio support
%bcond_without	amr		# AMR codecs (AMR-NB and AMR-WB) support
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
Version:	14.4.2
Release:	2
License:	GPL v2+ (sox), LGPL v2+ (libsox)
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/sox/%{name}-%{version}.tar.bz2
# Source0-md5:	ba804bb1ce5c71dd484a102a5b27d0dd
Patch0:		%{name}-system-lpc10.patch
Patch1:		%{name}-dyn.patch
Patch2:		%{name}-link.patch
URL:		http://sox.sourceforge.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
BuildRequires:	flac-devel >= 1.1.3
%{?with_gomp:BuildRequires:	gcc >= 6:4.2}
BuildRequires:	ladspa-devel
BuildRequires:	lame-libs-devel >= 3.98
BuildRequires:	libao-devel
%{?with_gomp:BuildRequires:	libgomp-devel}
BuildRequires:	libgsm-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libltdl-devel
BuildRequires:	libmad-devel
BuildRequires:	libmagic-devel
BuildRequires:	libpng-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel >= 1.0.12
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	lpc10-devel
%{?with_amr:BuildRequires:	opencore-amr-devel}
BuildRequires:	opusfile-devel
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel}
BuildRequires:	pkgconfig
BuildRequires:	twolame-devel
BuildRequires:	wavpack-devel
Suggests:	ffmpeg
Obsoletes:	sox-fmt-ffmpeg
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

%package fmt-amr
Summary:	SoX modules with AMR-NB and AMR-WB format support
Summary(pl.UTF-8):	Moduły SoX obsługujące formaty AMR-NB i AMR-WB
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description fmt-amr
SoX modules with AMR-NB and AMR-WB format support.

%description fmt-amr -l pl.UTF-8
Moduły SoX obsługujące formaty AMR-NB i AMR-WB.

%package fmt-lpc10
Summary:	SoX module with LPC10 format support
Summary(pl.UTF-8):	Moduł SoX obsługujący format LPC10
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description fmt-lpc10
SoX module with LPC10 format support.

%description fmt-lpc10 -l pl.UTF-8
Moduł SoX obsługujący format LPC10.

%package fmt-mp3
Summary:	SoX module with MP3 format support
Summary(pl.UTF-8):	Moduł SoX obsługujący format MP3
# libmad is GPLed, libmp3lame can contain GPL parts (and in PLD it does)
License:	GPL v2+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description fmt-mp3
SoX module with MP3 format support. It uses libmad for decoding and
LAME for encoding.

%description fmt-mp3 -l pl.UTF-8
Moduł SoX obsługujący format MP3. Wykorzystuje do dekodowania
bibliotekę libmad, a do kodowania - LAME.

%package fmt-opus
Summary:	SoX module with Ogg Opus format support
Summary(pl.UTF-8):	Moduł SoX obsługujący format Ogg Opus
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description fmt-opus
SoX module with Ogg Opus format support. It uses opusfile library
for decoding.

%description fmt-opus -l pl.UTF-8
Moduł SoX obsługujący format Ogg Opus. Wykorzystuje do dekodowania
bibliotekę opusfile.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_gomp:--disable-gomp} \
	--disable-silent-rules \
	--with-distro='PLD Linux Distribution' \
	--with-dyn-default \
	%{!?with_alsa:--without-alsa} \
	%{!?with_amr:--without-amrnb --without-amrwb} \
	%{!?with_pulseaudio:--without-pulseaudio}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo "#!/bin/sh" > $RPM_BUILD_ROOT%{_bindir}/soxplay
echo "" >> $RPM_BUILD_ROOT%{_bindir}/soxplay
echo '%{_bindir}/sox $1 -t .au - > /dev/audio' >> $RPM_BUILD_ROOT%{_bindir}/soxplay

%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/{play,rec}.1
echo '.so sox.1' > $RPM_BUILD_ROOT%{_mandir}/man1/play.1
echo '.so sox.1' > $RPM_BUILD_ROOT%{_mandir}/man1/rec.1

%{__rm} $RPM_BUILD_ROOT%{_libdir}/sox/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains only notes, not GPL/LGPL texts
%doc AUTHORS COPYING ChangeLog NEWS README src/monkey.*
%attr(755,root,root) %{_bindir}/play
%attr(755,root,root) %{_bindir}/rec
%attr(755,root,root) %{_bindir}/sox
%attr(755,root,root) %{_bindir}/soxi
%attr(755,root,root) %{_bindir}/soxplay
%attr(755,root,root) %{_libdir}/libsox.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsox.so.3
%dir %{_libdir}/sox
%if %{with alsa}
# R: alsa-lib
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_alsa.so
%endif
# R: libao
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_ao.so
# R: flac
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_flac.so
# R: libgsm
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_gsm.so
%if %{with pulseaudio}
# R: pulseaudio-libs
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_pulseaudio.so
%endif
# R: libsndfile (+submodules)
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_sndfile.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_caf.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_fap.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_mat4.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_mat5.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_oss.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_paf.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_pvf.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_sd2.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_w64.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_xi.so
# R: libogg libvorbis
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_vorbis.so
# R: wavpack
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_wavpack.so
%{_mandir}/man1/play.1*
%{_mandir}/man1/rec.1*
%{_mandir}/man1/sox.1*
%{_mandir}/man1/soxi.1*
%{_mandir}/man7/soxeffect.7*
%{_mandir}/man7/soxformat.7*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsox.so
%{_includedir}/sox.h
%{_pkgconfigdir}/sox.pc
%{_mandir}/man3/libsox.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsox.a
%{_libdir}/libsox.la

%if %{with amr}
%files fmt-amr
%defattr(644,root,root,755)
# R: amr-nb
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_amr_nb.so
# R: amr-wb
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_amr_wb.so
%endif

%files fmt-lpc10
%defattr(644,root,root,755)
# R: lpc10
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_lpc10.so

%files fmt-mp3
%defattr(644,root,root,755)
# R: lame-libs libmad
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_mp3.so

%files fmt-opus
%defattr(644,root,root,755)
# R: opusfile
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_opus.so
