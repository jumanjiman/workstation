Name: baseline
summary: baseline configuration 
Version: 0.3.11
Release: 1%{?dist}

url: http://github.com/jumanjiman/workstation
Group: System Environment/Base
License: GPL v3
Source0: %{name}-%{version}.tar.gz

buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Buildarch: noarch

# no encumbered IP
conflicts: mono-core

# cli access to pastebin
requires: nopaste

# satserver tools
requires: spacecmd

# newsreader from epel and fedora
requires: rss2email

# browser
requires: google-chrome

# common OS pkgs
requires: authconfig
requires: bash >= 4
requires: bridge-utils
requires: chkconfig
requires: device-mapper-multipath
requires: dictd
requires: dstat
requires: ethtool
requires: grep
requires: iproute
requires: iptraf
requires: lslk
requires: lsscsi
requires: ltrace
requires: mtr
requires: mutt
requires: mutrace
requires: net-snmp
requires: net-snmp-utils
requires: ndisc6
requires: nmap
requires: openssh
requires: openldap-clients
requires: openssh-server
requires: openldap-devel
requires: ntp
requires: patchutils
requires: setroubleshoot
requires: iscsi-initiator-utils
requires: sg3_utils
requires: strace
requires: syslinux
requires: sysstat
requires: system-config-kdump
requires: system-config-network
requires: tftp
requires: util-linux
requires: vim-enhanced
requires: wireshark
requires: xorg-x11-xauth
requires: yum 
requires: yum-utils
requires: xterm
requires: subversion
requires: traceroute
requires: lftp
requires: krb5-workstation
requires: tcping

# profiling tools
requires: blktrace
requires: valgrind
requires: systemtap-runtime
requires: systemtap-client
requires: tuned-utils
requires: oprofile
requires: oprofile-jit
requires: glibc-utils
requires: frysk

# selinux tools
requires: policycoreutils
requires: policycoreutils-gui
requires: setools
requires: setools-console
requires: setools-gui

%description 
Install this package to ensure a baseline, common config
for my machine.

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/baseline/services_on
%config %{_sysconfdir}/baseline/services_off
%{_sbindir}/verify-baseline
%{_sbindir}/disable-zeroconf
%{_sbindir}/disable-services
%{_sbindir}/configure-ssh
%doc README.asciidoc
%doc rss2email.asciidoc

# ----------------------------------------------------------------------

%package devel

summary: baseline development tools

# lockstep with baseline
requires: baseline = %{version}-%{release}
requires: baseline-release = %{version}-%{release}

%if 0%{?fedora}
requires: fedora-packager
requires: blktrace
requires: diveintopython-txt
%endif

# common tools
requires: rpm-build
requires: redhat-rpm-config
requires: rpmlint
requires: rpmdevtools
requires: python-setuptools
requires: python-devel
requires: createrepo
requires: cscope

# selinux tools
requires: setools-devel
requires: eclipse-setools

%description devel
Developer tools for consistent Fedora build.

%files devel
%defattr(-,root,root,-)
%doc README.asciidoc

# ----------------------------------------------------------------------
#
# NOTE: baseline-release should be installed in a separate
#       transaction from baseline and baseline-devel

%package release

summary: workstation repo for baseline

%description release
Workstation repo to configure yum for local repo

%files release
%defattr(-,root,root-)
%config %{_sysconfdir}/yum.repos.d/workstation.repo
%config %{_sysconfdir}/yum.repos.d/tmp-tito.repo
%config %{_sysconfdir}/yum.repos.d/google-chrome-stable.repo
%config %{_sysconfdir}/pki/rpm-gpg/pmorgan.pubkey
%config %{_sysconfdir}/pki/rpm-gpg/google.pubkey

# ----------------------------------------------------------------------

%prep
%setup -q


%clean
%{__rm} -fr %{buildroot}


%build
# nothing to build


%install
%{__rm} -fr %{buildroot}
%{__mkdir_p} %{buildroot}%{_sbindir}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/baseline
%{__mkdir_p} %{buildroot}%{_sysconfdir}/yum.repos.d
%{__mkdir_p} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

# files for base pkg
%{__install} -p -m755 src/verify-baseline %{buildroot}%{_sbindir}
%{__install} -p -m755 src/disable-zeroconf %{buildroot}%{_sbindir}
%{__install} -p -m755 src/disable-services %{buildroot}%{_sbindir}
%{__install} -p -m755 src/configure-ssh %{buildroot}%{_sbindir}
%{__install} -p -m644 src/services_on  %{buildroot}%{_sysconfdir}/baseline
%{__install} -p -m644 src/services_off %{buildroot}%{_sysconfdir}/baseline

# files for -release subpkg
%{__install} -p -m644 src/workstation.repo %{buildroot}%{_sysconfdir}/yum.repos.d
%{__install} -p -m644 src/tmp-tito.repo %{buildroot}%{_sysconfdir}/yum.repos.d
%{__install} -p -m644 src/google-chrome-stable.repo %{buildroot}%{_sysconfdir}/yum.repos.d
%{__install} -p -m644 src/pmorgan.pubkey %{buildroot}%{_sysconfdir}/pki/rpm-gpg/pmorgan.pubkey
%{__install} -p -m644 src/google.pubkey %{buildroot}%{_sysconfdir}/pki/rpm-gpg/google.pubkey



# =====================================================
# NOTE ON SCRIPTLETS (pre,post,preun,postun)
# -----------------------------------------------------
# RPM upgrade uses the following sequence.
# The number in parentheses is the value of $1
#   Run pre of new package (2)
#   Install new files
#   Run post of new package (2)
#   Run preun of old package (1)
#   Delete any old files not overwritten by newer ones
#   Run postun of old package (1)
# =====================================================

%pre
if [ $1 -gt 0 ]; then
  :
fi

%post
if [ $1 -gt 0 ]; then
  # at least one copy of this package is installed

  %{_sbindir}/disable-zeroconf
  %{_sbindir}/disable-services
  %{_sbindir}/configure-ssh

  # initialize etckeeper for /etc
  pushd /etc &> /dev/null
  if ! git rev-parse --show-cdup &> /dev/null; then
    # NOTE: this is safe to do multiple times
    etckeeper init
    etckeeper commit "initialized /etc with etckeeper from baseline"
  fi
  popd

fi

%preun
if [ $1 -eq 0 ]; then
  # last removal
  :
else
  # upgrade
  :
fi

%postun
if [ $1 -eq 0 ]; then
  # last removal
  :
else
  # upgrade
  :
fi

%verifyscript
(
%{_sbindir}/verify-baseline
) >&2



%changelog
* Mon Dec 20 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.11-1
- improved exit status of verify-baseline (jumanjiman@gmail.com)
- verify-baseline checks etckeeper init (jumanjiman@gmail.com)
- initialize etckeeper during postinstall (jumanjiman@gmail.com)

* Mon Dec 20 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.10-1
- require openldap-clients (jumanjiman@gmail.com)

* Mon Dec 20 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.9-1
- protect ssh and sshd from plaintext recovery attack
- require ssh and sshd as part of baseline
- enable sshd for boot-time startup

* Tue Nov 30 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.8-1
- require iscsi client tools (jumanjiman@gmail.com)
- require syslinux (jumanjiman@gmail.com)

* Wed Nov 10 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.7-1
- avoid rpmlint warnings (jumanjiman@gmail.com)
- require rss2email (jumanjiman@gmail.com)
- add instructions for rss2email (jumanjiman@gmail.com)
- require rpmdevtools (jumanjiman@gmail.com)
- python book in txt format (jumanjiman@gmail.com)

* Thu Nov 04 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.6-4
- requires cscope (jumanjiman@gmail.com)

* Thu Nov 04 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.6-3
- requires rpm-manifest and rpm-manifest-etckeeper (jumanjiman@gmail.com)

* Tue Nov 02 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.6-2
- avoid mono-core due to encumbrances (jumanjiman@gmail.com)

* Mon Oct 25 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.6-1
- requires blktrace (jumanjiman@gmail.com)

* Sat Oct 23 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.5-4
- requires tcping (jumanjiman@gmail.com)

* Thu Oct 21 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.5-3
- requires frysk (jumanjiman@gmail.com)

* Wed Oct 20 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.5-2
- requires wd (jumanjiman@gmail.com)

* Tue Oct 19 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.5-1
- add yum repo for /tmp/tito (jumanjiman@gmail.com)

* Tue Oct 19 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.4-4
- require createrepo (jumanjiman@gmail.com)

* Tue Oct 19 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.4-3
- require more troubleshooting tools (jumanjiman@gmail.com)

* Tue Oct 19 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.4-2
- Additional dependencies
* Sun Sep 12 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.4-1
- add pmorgan.pubkey (jumanjiman@gmail.com)
- add google.pubkey (jumanjiman@gmail.com)
- add google-chrome-stable repo and dependency (jumanjiman@gmail.com)

* Sun Sep 12 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.3-1
- moved files sections to subpackage sections (jumanjiman@gmail.com)
- add -release subpackage (jumanjiman@gmail.com)

* Sun Sep 12 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.2-1
- add devel subpackage (jumanjiman@gmail.com)
- require bash >= 4 (jumanjiman@gmail.com)
- remove emacs and nano dependencies (jumanjiman@gmail.com)
- add selinux tools (jumanjiman@gmail.com)

* Sun Sep 12 2010 Paul Morgan <jumanjiman@gmail.com> 0.3.1-1
- import from old system

