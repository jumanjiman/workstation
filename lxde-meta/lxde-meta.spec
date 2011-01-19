Name:		lxde-meta
Version:	0.1
Release:	1%{?dist}
Summary:	Provides components for a lightweight X11 desktop environment

Group:		System Environment/Base
License:	GPLv3+
URL:		http://github.com/jumanjiman/workstation
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

Requires:	lxappearance
Requires:	lxde-common.noarch
Requires:	imsettings-lxde
Requires:	lxde-icon-theme.noarch
Requires:	lxinput
Requires:	lxmenu-data.noarch
Requires:	lxdm
Requires:	lxlauncher
Requires:	lxmusic
Requires:	lxpolkit
Requires:	lxrandr
Requires:	lxsession
Requires:	lxsession-edit
Requires:	lxtask
Requires:	lxpanel
Requires:	lxshortcut
Requires:	lxterminal

%description
Install this meta-package to pull in dependencies
for LXDE and useful components. LXDE provides a 
lightweight X11 desktop environment and is an
alternative to GNOME and KDE.


%prep
%setup -q


%build


%install
rm -rf %{buildroot}
%{__mkdir_p} %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)



%changelog

