Name:		motd-generator
Version:	1.0.0
Release:	1%{?dist}
Summary:	Custom message of the day (MOTD) designed to be as practical and informative as possible.

License:	Unknown
URL:		https://github.com/gonoph/motd-generator
Source0:	https://github.com/gonoph/motd-generator/archive/v1.0.0.tar.gz

Requires:	systemd

%{?systemd_requires}

%description
This is a custom message of the day (MOTD) designed to be as practical and
informative as possible. The truth is, no one actually reads the MOTD. As such,
the MOTD should contain useful, yet minimal, information about the host system
such that a quick glance at it when logging in may actually be worth a person's
precious time. This way, any potential issues are noticed and not naively
ignored. This MOTD generator scripts has the ability to output text in color.
Using this feature, potential issues can be highlighted for easy
identification.


%prep
%setup -q

# %build


%install
DESTDIR=%{buildroot}
DIR_BIN=${DESTDIR}%{_bindir}
DIR_STATE=${DESTDIR}%{_sharedstatedir}/%{name}
DIR_SYSTEMD=${DESTDIR}%{_exec_prefix}/lib/systemd/system
DIR_PRESETS=${DESTDIR}%{_exec_prefix}/lib/systemd/system-preset/
mkdir -p $DIR_BIN
mkdir -p $DIR_STATE
mkdir -p $DIR_SYSTEMD
install -m 755 -t $DIR_BIN motd_gen.py motd_stat.py
install -m 644 -t $DIR_SYSTEMD motd_stat.service
echo "enable motd_stat.service" > $DIR_PRESETS/50-motd_stat.preset

%pre
U=$(getent passwd motd)
test "x$U" == "x" && useradd -r -d $DIR_STATE -M -U motd || :

%post
%systemd_post motd_stat.service

%preun
%systemd_preun motd_stat.service

%postun
%systemd_postun_with_restart motd_stat.service
if [ $1 -gt 0 ] ; then
  exit 0
fi
userdel motd || :

%files
%defattr(644, motd, motd, -)
%attr(755,-,-) %{_bindir}/motd_gen.py
%attr(755,-,-) %{_bindir}/motd_stat.py
%{_sharedstatedir}/%{name}
%{_exec_prefix}/lib/systemd/system/motd_stat.service
%{_exec_prefix}/lib/systemd/system-preset/50-motd_stat.preset
%doc README.md
%doc motd_stat
%dir %{_sharedstatedir}/%{name}

%changelog
* Fri Sep 14 2018 Billy Holmes <billy@gonoph.net> - 1.0.0-1
- Initial release
