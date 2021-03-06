name: bash-profile-scripts
summary: Adds /etc/profile.d/ files for Bash

version: 0.2.6
release: 1%{?dist}

license: GPLv3 and GPLv2
group: System Environment/Base

url: http://github.com/jumanjiman/workstation
source: %{name}-%{version}.tar.gz
buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
buildarch: noarch

requires:	bash >= 4
requires:	pinfo
requires:	vim-minimal
requires:	sysstat
requires:	readline
#requires:	elinks
#requires:	rsync

%description
Places files in /etc/profiles.d to configure Bash
the way I like it.

%prep
%setup -q 

%clean
%{__rm} -fr %{buildroot}

%build
# nothing to build

%install
%{__rm} -fr %{buildroot}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/profile.d
%{__install} -p -m644 src/pm-sar.sh %{buildroot}%{_sysconfdir}/profile.d
%{__install} -p -m644 src/pm-info.sh %{buildroot}%{_sysconfdir}/profile.d
%{__install} -p -m644 src/pm-grep.sh %{buildroot}%{_sysconfdir}/profile.d
%{__install} -p -m644 src/pm-less.sh %{buildroot}%{_sysconfdir}/profile.d
%{__install} -p -m644 src/pm-hist.sh %{buildroot}%{_sysconfdir}/profile.d
%{__install} -p -m644 src/pm-inputrc.sh %{buildroot}%{_sysconfdir}/profile.d
%{__install} -p -m644 src/pm-clear.sh %{buildroot}%{_sysconfdir}/profile.d
%{__install} -p -m644 src/pm-editor.sh %{buildroot}%{_sysconfdir}/profile.d
%{__install} -p -m644 src/git-completion.sh %{buildroot}%{_sysconfdir}/profile.d
%{__install} -p -m644 src/eiffelstudio.sh %{buildroot}%{_sysconfdir}/profile.d
%{__install} -p -m644 src/kcscope.sh %{buildroot}%{_sysconfdir}/profile.d


%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/profile.d/pm-sar.sh
%config %{_sysconfdir}/profile.d/pm-info.sh
%config %{_sysconfdir}/profile.d/pm-grep.sh
%config %{_sysconfdir}/profile.d/pm-less.sh
%config %{_sysconfdir}/profile.d/pm-hist.sh
%config %{_sysconfdir}/profile.d/pm-inputrc.sh
%config %{_sysconfdir}/profile.d/pm-clear.sh
%config %{_sysconfdir}/profile.d/pm-editor.sh
%config %{_sysconfdir}/profile.d/git-completion.sh
%config %{_sysconfdir}/profile.d/eiffelstudio.sh
%config %{_sysconfdir}/profile.d/kcscope.sh
%doc README.asciidoc
%doc src/sample.bashrc
%doc COPYING.GPLv2
%doc COPYING.GPLv3

%changelog
* Tue Dec 28 2010 Paul Morgan <jumanjiman@gmail.com> 0.2.6-1
- fix filename in spec (jumanjiman@gmail.com)

* Tue Dec 28 2010 Paul Morgan <jumanjiman@gmail.com> 0.2.5-1
- rename file (jumanjiman@gmail.com)
- remove dangerous "exit 0" (jumanjiman@gmail.com)

* Fri Nov 05 2010 Paul Morgan <jumanjiman@gmail.com> 0.2.4-1
- add alias for kcscope (jumanjiman@gmail.com)

* Wed Oct 20 2010 Paul Morgan <jumanjiman@gmail.com> 0.2.3-2
- sigh, add new file to spec file (jumanjiman@gmail.com)

* Wed Oct 20 2010 Paul Morgan <jumanjiman@gmail.com> 0.2.3-1
- set environment variables for EiffelStudio (jumanjiman@gmail.com)

* Mon Sep 20 2010 Paul Morgan <jumanjiman@gmail.com> 0.2.2-1
- add git-completion.sh (jumanjiman@gmail.com)

* Sun Sep 12 2010 Paul Morgan <jumanjiman@gmail.com> 0.2.1-1
- import from previous srpm

* Sun Jun 13 2010 Paul Morgan <pmorgan@redhat.com> 0.1-6
- CHANGE: sample.bashrc to override globals

* Sun Jun 13 2010 Paul Morgan <pmorgan@redhat.com> 0.1-5
- ADD: requires vim-minimal for editor.sh
- ADD: PAGER env to less.sh

* Sat Jun 12 2010 Paul Morgan <pmorgan@redhat.com> 0.1-4
- ADD: ~/.etc/inputrc support

* Sat Jun 12 2010 Paul Morgan <pmorgan@redhat.com> 0.1-3
- ADD: requires pinfo

* Thu Jun  3 2010 Paul Morgan <pmorgan@redhat.com> 0.1-2
- ADD: sample.bashrc that has some of my favorite personalizations

* Thu Jun  3 2010 Paul Morgan <pmorgan@redhat.com> 0.1-1
- initial packaging
