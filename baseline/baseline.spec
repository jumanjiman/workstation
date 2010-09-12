Name: baseline
summary: baseline configuration 
Version: 0.3.3
Release: 1%{?dist}

url: http://github.com/jumanjiman/workstation
Group: System Environment/Base
License: GPL v3
Source0: %{name}-%{version}.tar.gz

buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Buildarch: noarch

requires: reach
requires: bash-profile-scripts
requires: baseline-release = %{version}-%{release}

# cli access to pastebin
requires: nopaste

# satserver tools
requires: spacecmd

# browser
requires: google-chrome

# common OS pkgs
requires: authconfig
requires: bash >= 4
requires: bridge-utils
requires: chkconfig
requires: device-mapper-multipath
requires: dstat
requires: grep
requires: iproute
requires: iptraf
requires: lslk
requires: lsscsi
requires: ltrace
requires: mutt
requires: net-snmp
requires: net-snmp-utils
requires: nmap
requires: openldap-devel
requires: ntp
requires: patchutils
requires: setroubleshoot
requires: sg3_utils
requires: strace
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
%doc README.asciidoc

# ----------------------------------------------------------------------

%package devel

summary: baseline development tools

# lockstep with baseline
requires: baseline = %{version}-%{release}
requires: baseline-release = %{version}-%{release}

# common tools
requires: rpm-build
requires: rpmlint
requires: python-setuptools

# selinux tools
requires: setools-devel
requires: eclipse-setools

%description devel
Developer tools for consistent Fedora build.

%files devel
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
%config %{_sysconfdir}/yum.repos.d/workstation.repo
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
%{__install} -p -m644 src/services_on  %{buildroot}%{_sysconfdir}/baseline
%{__install} -p -m644 src/services_off %{buildroot}%{_sysconfdir}/baseline

# files for -release subpkg
%{__install} -p -m644 src/workstation.repo %{buildroot}%{_sysconfdir}/yum.repos.d
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

