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
./configure --disable-camomile --prefix=%{buildroot}/usr/local
make

%install
make install 
find %{buildroot} -type f -exec sed -i s#%{buildroot}##g {} \;

%files
/usr/local/etc/logrotate.d/liquidsoap
/usr/local/etc/liquidsoap/radio.liq.example
/usr/local/bin/liquidsoap
/usr/local/bin/liguidsoap
/usr/local/share/man/man1/liguidsoap.1
/usr/local/share/man/man1/liquidsoap.1
/usr/local/share/doc/liquidsoap-1.0.1/examples/README
/usr/local/share/doc/liquidsoap-1.0.1/examples/transitions.liq
/usr/local/share/doc/liquidsoap-1.0.1/examples/radio.liq
/usr/local/share/doc/liquidsoap-1.0.1/examples/geek.liq
/usr/local/share/doc/liquidsoap-1.0.1/examples/fallible.liq
/usr/local/lib/python2.6/site-packages/liquidsoap/widgets.pyo
/usr/local/lib/python2.6/site-packages/liquidsoap/editable.pyc
/usr/local/lib/python2.6/site-packages/liquidsoap/mix.pyc
/usr/local/lib/python2.6/site-packages/liquidsoap/liguidsoap.py
/usr/local/lib/python2.6/site-packages/liquidsoap/queue.pyo
/usr/local/lib/python2.6/site-packages/liquidsoap/mix.pyo
/usr/local/lib/python2.6/site-packages/liquidsoap/playlist.pyc
/usr/local/lib/python2.6/site-packages/liquidsoap/widgets.pyc
/usr/local/lib/python2.6/site-packages/liquidsoap/playlist.pyo
/usr/local/lib/python2.6/site-packages/liquidsoap/output.py
/usr/local/lib/python2.6/site-packages/liquidsoap/client.pyo
/usr/local/lib/python2.6/site-packages/liquidsoap/client.py
/usr/local/lib/python2.6/site-packages/liquidsoap/output.pyo
/usr/local/lib/python2.6/site-packages/liquidsoap/playlist.py
/usr/local/lib/python2.6/site-packages/liquidsoap/queue.pyc
/usr/local/lib/python2.6/site-packages/liquidsoap/widgets.py
/usr/local/lib/python2.6/site-packages/liquidsoap/client.pyc
/usr/local/lib/python2.6/site-packages/liquidsoap/mix.py
/usr/local/lib/python2.6/site-packages/liquidsoap/output.pyc
/usr/local/lib/python2.6/site-packages/liquidsoap/editable.py
/usr/local/lib/python2.6/site-packages/liquidsoap/liguidsoap.pyo
/usr/local/lib/python2.6/site-packages/liquidsoap/editable.pyo
/usr/local/lib/python2.6/site-packages/liquidsoap/liguidsoap.pyc
/usr/local/lib/python2.6/site-packages/liquidsoap/queue.py
/usr/local/lib/liquidsoap/1.0.1/lastfm.liq
/usr/local/lib/liquidsoap/1.0.1/extract-replaygain
/usr/local/lib/liquidsoap/1.0.1/http_codes.liq
/usr/local/lib/liquidsoap/1.0.1/video_text.liq
/usr/local/lib/liquidsoap/1.0.1/http.liq
/usr/local/lib/liquidsoap/1.0.1/flows.liq
/usr/local/lib/liquidsoap/1.0.1/liquidtts
/usr/local/lib/liquidsoap/1.0.1/utils.liq
/usr/local/lib/liquidsoap/1.0.1/externals.liq
/usr/local/lib/liquidsoap/1.0.1/shoutcast.liq
/usr/local/lib/liquidsoap/1.0.1/pervasives.liq

%description
Liquidsoap is a powerful and flexible language for describing your streams. It offers a rich collection of operators that you can combine at will, giving you more power than you need for creating or transforming streams. But liquidsoap is still very light and easy to use, in the Unix tradition of simple strong components working together.

%changelog
* Sat Oct 21 2012 Martin Konecny <martin dot konecny at gmail.com> - 1.0-2
- initial version 
