Name:		MOTD Generator
Version:	1.0.0
Release:	1%{?dist}
Summary:	Custom message of the day (MOTD) designed to be as practical and informative as possible.

License:	Unknown
URL:		https://github.com/gonoph/motd-generator
Source0:	https://github.com/gonoph/motd-generator/archive/motd-generator-1.0.0.tar.gz

Requires:	systemd

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


%build


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog

