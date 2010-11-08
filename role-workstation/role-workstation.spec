Name:		role-workstation
Version:	0.2.5
Release:	2%{?dist}
Summary:	configures a graphical workstation

Group:		System Environment/Base
License:	GPLv3+
URL:		http://github.com/jumanjiman/workstation
Source0:	%{name}-%{version}.tar.gz
buildarch:	noarch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: asciidoc

Requires:	nautilus-open-terminal
Requires:	baseline
Requires:	GConf2
Requires:	initscripts
Requires:	kernel-doc
requires:	git-all

# eclipse tools
requires:	eclipse-demos
requires:	eclipse-rpmstubby
requires:	eclipse-rpm-editor
requires:	eclipse-setools
requires:	eclipse-pydev
requires:	eclipse-systemtapgui
requires:	systemtapguiserver
requires:	eclipse-oprofile
requires:	eclipse-linuxprofilingframework
requires:	eclipse-valgrind
requires:	eclipse-egit
requires:	eclipse-cdt
requires:	eclipse-emf-xsd
requires:	eclipse-callgraph

# profiling tools
requires:	oprofile-gui
requires:	gprof2dot
requires:	systemtap
requires:	systemtap-client
requires:	systemtap-grapher
requires:	systemtap-runtime
requires:	systemtap-server
requires:	systemtap-testsuite
requires:	tuned-utils
requires:	dwarves
requires:	spu-binutils
requires:	seekwatcher

# virtualization tools
requires:	qemu-kvm-tools

# thin clients
requires:	tsclient

# gui debugging
%if 0%{?fedora} < 14
# this is orphaned in F14
requires:	system-config-display
%endif
requires:   xorg-x11-apps

# edit gnome menus
requires:	alacarte

# email
requires:	mutt
requires:	grepmail

# instant messaging
requires:	pidgin
requires:	pidgin-otr
requires:	purple-plugin_pack-pidgin

# authoring
requires:	publican
requires:	publican-redhatgps
requires:	docbook-dtds
requires:	docbook-utils
requires:	docbook-simple
requires:	docbook-style-xsl
requires:	docbook-utils-pdf
requires:	docbook5-schemas
requires:	docbook2X
requires:	docbook-slides
requires:	docbook-style-dsssl
requires:	docbook5-style-xsl

# text utils
requires:   dictd
requires:   diction

# servers
requires:	dhcp
requires:	tftp-server
requires:	bind
requires:	bind-chroot
requires:	httpd

# conditional dependencies as described at
# https://fedoraproject.org/wiki/Packaging/DistTag
%if 0%{?fedora} >= 11
Requires:	bash-doc
Requires:	man-pages
Requires:	yum-plugin-protect-packages
Requires:	diveintopython
Requires:	diveintopython-pdf
Requires:	python-application
%endif

%if 0%{?fedora} >= 14
Requires:	compizconfig-backend-gconf
%endif

# see also https://fedoraproject.org/wiki/Packaging/ScriptletSnippets

%description
Install this package to configure your host as a
graphical workstation. This package requires numerous
other packages and applies configurations for a comfortable
fit.

%prep
%setup -q


%clean
%{__rm} -fr %{buildroot}


%build
asciidoc -b html4 doc/tips.asciidoc


%install
%{__rm} -fr %{buildroot}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/role-workstation/
%{__mkdir_p} %{buildroot}%{_sysconfdir}/sysconfig/modules/
%{__mkdir_p} %{buildroot}%{_sysconfdir}/profile.d/
%{__install} -p -m 644 src/gconf-keys.conf %{buildroot}%{_sysconfdir}/role-workstation/
%{__install} -p -m 644 src/workstation.conf %{buildroot}%{_sysconfdir}/role-workstation/
%{__install} -p -m755 src/workstation.sh %{buildroot}%{_sysconfdir}/profile.d/
%{__install} -p -m755 src/workstation.modules %{buildroot}%{_sysconfdir}/sysconfig/modules



%files
%defattr(-,root,root,-)
%doc README.asciidoc
%doc README.rpmbuild
%doc doc/*
%config %{_sysconfdir}/role-workstation/gconf-keys.conf
%config %{_sysconfdir}/role-workstation/workstation.conf
%{_sysconfdir}/profile.d/workstation.sh
%{_sysconfdir}/sysconfig/modules/workstation.modules

%post
if [ $1 -gt 0 ]; then
  %{_sysconfdir}/profile.d/workstation.sh
  %{_sysconfdir}/sysconfig/modules/workstation.modules
fi


%changelog
* Sun Nov 07 2010 Paul Morgan <jumanjiman@gmail.com> 0.2.5-2
- s-c-display is orphaned in f14 (jumanjiman@gmail.com)
- python development utils (jumanjiman@gmail.com)

* Tue Oct 19 2010 Paul Morgan <jumanjiman@gmail.com> 0.2.5-1
- add tips to documentation (jumanjiman@gmail.com)

* Tue Oct 19 2010 Paul Morgan <jumanjiman@gmail.com> 0.2.4-3
- require profiling tools (jumanjiman@gmail.com)
- require eclipse tools (jumanjiman@gmail.com)
- require alacarte to edit gnome menus (jumanjiman@gmail.com)

* Mon Oct 18 2010 Paul Morgan <jumanjiman@gmail.com> 0.2.4-2
- require pidgin IM client (jumanjiman@gmail.com)
- require xinput for troubleshooting (jumanjiman@gmail.com)
- require dictd and diction text utilities (jumanjiman@gmail.com)
- require mutt and grepmail (jumanjiman@gmail.com)

* Mon Sep 13 2010 Paul Morgan <jumanjiman@gmail.com> 0.2.4-1
- requires documentation tools (jumanjiman@gmail.com)
- workstation server dependencies (jumanjiman@gmail.com)
- requires git-all (jumanjiman@gmail.com)
- requires system-config-display (jumanjiman@gmail.com)
- requires tsclient (jumanjiman@gmail.com)

* Sun Sep 12 2010 Paul Morgan <jumanjiman@gmail.com> 0.2.3-1
- fix typo (jumanjiman@gmail.com)

* Sun Sep 12 2010 Paul Morgan <jumanjiman@gmail.com> 0.2.2-1
- fix source spec for tito (jumanjiman@gmail.com)

* Sun Sep 12 2010 Paul Morgan <jumanjiman@gmail.com> 0.2.1-1
- import from srpm

* Sat Jun 19 2010 Paul Morgan <pmorgan@redhat.com> 0.1-9
- FIX: typo in workstation.sh

* Mon Jun 14 2010 Paul Morgan <pmorgan@redhat.com> 0.1-8
- FIX: basename in workstation.sh that manifested only during sudo -i

* Sun Jun 13 2010 Paul Morgan <pmorgan@redhat.com> 0.1-7
- ADD: trackpad preferences
- ADD: workstation.sh logs to syslog

* Sun Jun 13 2010 Paul Morgan <pmorgan@redhat.com> 0.1-6
- ADD: README.rpmbuild

* Sun Jun 13 2010 Paul Morgan <pmorgan@redhat.com> 0.1-5
- ADD: conditional requires yum-plugin-protect-packages

* Sun Jun 13 2010 Paul Morgan <pmorgan@redhat.com> 0.1-4
- ADD: conditional requires man-pages and bash-doc

* Sun Jun 13 2010 Paul Morgan <pmorgan@redhat.com> 0.1-3
- RENAME: workstation.conf as gconf-keys.conf
- ADD: workstation.conf file
- ADD: workstation.modules
- ADD: apply settings during post-install

* Sun Jun 13 2010 Paul Morgan <pmorgan@redhat.com> 0.1-2
- ADD: settings to workstation.conf
- CHANGE: workstation.sh uses new format for workstation.conf

* Sat Jun 12 2010 Paul Morgan <pmorgan@redhat.com> 0.1-1
- initial pkg
