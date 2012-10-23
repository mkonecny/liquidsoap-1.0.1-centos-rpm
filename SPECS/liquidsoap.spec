Name:     liquidsoap 
Version:  1.0.1
Release:  1
Summary:  Liquidsoap by Savonet
License:  GPLv2
URL:      http://savonet.sourceforge.net/
Source0:  http://downloads.sourceforge.net/project/savonet/liquidsoap/1.0.1/liquidsoap-1.0.1-full.tar.bz2

BuildRequires: pcre-ocaml ocaml libmad taglib libvorbis flac

%prep
%setup -q -n liquidsoap-1.0.1-full
cp PACKAGES.minimal PACKAGES
./configure --disable-camomile
make

%install
make install DESTDIR=%{buildroot} OCAMLFIND_DESTDIR=%{buildroot} prefix=%{buildroot}

%files
/etc/logrotate.d/liquidsoap
/etc/liquidsoap/radio.liq.example
/bin/liquidsoap
/bin/liguidsoap
/share/man/man1/liguidsoap.1
/share/man/man1/liquidsoap.1
/share/doc/liquidsoap-1.0.1/examples/README
/share/doc/liquidsoap-1.0.1/examples/transitions.liq
/share/doc/liquidsoap-1.0.1/examples/radio.liq
/share/doc/liquidsoap-1.0.1/examples/geek.liq
/share/doc/liquidsoap-1.0.1/examples/fallible.liq
/lib/python2.6/site-packages/liquidsoap/widgets.pyo
/lib/python2.6/site-packages/liquidsoap/editable.pyc
/lib/python2.6/site-packages/liquidsoap/mix.pyc
/lib/python2.6/site-packages/liquidsoap/liguidsoap.py
/lib/python2.6/site-packages/liquidsoap/queue.pyo
/lib/python2.6/site-packages/liquidsoap/mix.pyo
/lib/python2.6/site-packages/liquidsoap/playlist.pyc
/lib/python2.6/site-packages/liquidsoap/widgets.pyc
/lib/python2.6/site-packages/liquidsoap/playlist.pyo
/lib/python2.6/site-packages/liquidsoap/output.py
/lib/python2.6/site-packages/liquidsoap/client.pyo
/lib/python2.6/site-packages/liquidsoap/client.py
/lib/python2.6/site-packages/liquidsoap/output.pyo
/lib/python2.6/site-packages/liquidsoap/playlist.py
/lib/python2.6/site-packages/liquidsoap/queue.pyc
/lib/python2.6/site-packages/liquidsoap/widgets.py
/lib/python2.6/site-packages/liquidsoap/client.pyc
/lib/python2.6/site-packages/liquidsoap/mix.py
/lib/python2.6/site-packages/liquidsoap/output.pyc
/lib/python2.6/site-packages/liquidsoap/editable.py
/lib/python2.6/site-packages/liquidsoap/liguidsoap.pyo
/lib/python2.6/site-packages/liquidsoap/editable.pyo
/lib/python2.6/site-packages/liquidsoap/liguidsoap.pyc
/lib/python2.6/site-packages/liquidsoap/queue.py
/lib/liquidsoap/1.0.1/lastfm.liq
/lib/liquidsoap/1.0.1/extract-replaygain
/lib/liquidsoap/1.0.1/http_codes.liq
/lib/liquidsoap/1.0.1/video_text.liq
/lib/liquidsoap/1.0.1/http.liq
/lib/liquidsoap/1.0.1/flows.liq
/lib/liquidsoap/1.0.1/liquidtts
/lib/liquidsoap/1.0.1/utils.liq
/lib/liquidsoap/1.0.1/externals.liq
/lib/liquidsoap/1.0.1/shoutcast.liq
/lib/liquidsoap/1.0.1/pervasives.liq

%description
Liquidsoap is a powerful and flexible language for describing your streams. It offers a rich collection of operators that you can combine at will, giving you more power than you need for creating or transforming streams. But liquidsoap is still very light and easy to use, in the Unix tradition of simple strong components working together.

%changelog
* Sat Oct 21 2012 Martin Konecny <martin dot konecny at gmail.com> - 1.0-2
- initial version 
