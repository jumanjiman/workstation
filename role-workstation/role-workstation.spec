Name:		role-workstation
Version:	0.2.1
Release:	1%{?dist}
Summary:	configures a graphical workstation

Group:		System Environment/Base
License:	GPLv3+
URL:		http://github.com/jumanjiman/workstation
Source0:	%{name}-%{version}.tgz
buildarch:	noarch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	nautilus-open-terminal
Requires:	baseline
Requires:	GConf2
Requires:	initscripts
Requires:	kernel-doc

# conditional dependencies as described at
# https://fedoraproject.org/wiki/Packaging/DistTag
%if 0%{?fedora} >= 11
Requires:	bash-doc
Requires:	man-pages
Requires:	yum-plugin-protect-packages
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
# nothing to build


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
