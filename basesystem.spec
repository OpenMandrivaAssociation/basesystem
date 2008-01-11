#rh-7.0-2

%define name	basesystem
%define version	2008.0
%define release	%mkrel 4

Summary:	The skeleton package which defines a simple Mandriva Linux system
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Base
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires:	setup filesystem sed initscripts kbd utempter
Requires:	chkconfig coreutils SysVinit crontabs dev
Requires:	e2fsprogs etcskel findutils grep gzip kernel less 
Requires:	logrotate losetup mingetty mount net-tools passwd procps
Requires:	psmisc rootfiles rpm sash shadow-utils 
Requires:	stat tar termcap time util-linux vim
Requires:	vixie-cron which perl-base common-licenses
Requires:	ldconfig module-init-tools
Requires:	mandriva-release >= 2008.0
Requires:	syslog-daemon

# (gb) Add timezone database here for now before moving it to DrakX
Requires:	timezone
Requires:	bootloader

# MDK 9.0 requires a working libgcc
# Note: gcc3.2 is the system compiler there
Requires:	libgcc >= 3.2-1mdk

# (sb) need pdisk hfsutils ybin mktemp to setup bootloader PPC
%ifarch ppc
Requires:	pdisk hfsutils ybin mktemp mkinitrd pmac-utils
%endif
# (fg) 20001027 ia64 uses eli as a bootloader
%ifarch ia64
Requires:	mkinitrd
%endif

%description
Basesystem defines the components of a basic Mandriva Linux system (for
example, the package installation order to use during bootstrapping).
Basesystem should be the first package installed on a system, and it
should never be removed.

%files
