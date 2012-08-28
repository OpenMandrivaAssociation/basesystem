#rh-7.0-2

%define with_systemd 1

Summary:	Skeleton package which defines a simple Mandriva Linux system
Name:		basesystem
Version:	2012
Release:	5
License:	GPLv2+
Group:		System/Base
Requires:	kernel basesystem-minimal
%ifnarch %{mips}
Requires:	bootloader
%endif
# (sb) need pdisk hfsutils ybin mktemp to setup bootloader PPC
%ifarch ppc
Requires:	pdisk hfsutils ybin mktemp mkinitrd pmac-utils
%endif
# (fg) 20001027 ia64 uses eli as a bootloader
%ifarch ia64
Requires:	mkinitrd-command
%endif
%if %mdvver < 201200
Requires:	module-init-tools
%else
Requires:	kmod
%endif
Suggests:	prelink
Requires:	vixie-cron
Requires:	common-licenses
Requires:	syslog-daemon
%if %{with_systemd}
Requires(post):	systemd-sysvinit
%else
Requires(post):	sysvinit
Requires:	initscripts
%endif
Requires:	kbd 
Requires:	crontabs 
Requires:	e2fsprogs
Requires:	logrotate 

%package	minimal
Requires:	setup filesystem sed utempter
Requires:	chkconfig coreutils dev
Requires:	etcskel findutils grep gzip gzip-utils less
Requires:	losetup mingetty mount net-tools passwd procps
Requires:	psmisc rootfiles rpm shadow-utils
Requires:	stat tar termcap time util-linux
Suggests:	vim
Requires:	which perl-base
Requires:	mandriva-release >= 2008.1
Requires:	bzip2 xz

# (gb) Add timezone database here for now before moving it to DrakX
Requires:	timezone

%package	uml
Requires:	basesystem-minimal
Requires:	dhcp-client-daemon
Requires:	urpmi

%description
Basesystem defines the components of a basic Mandriva Linux system (for
example, the package installation order to use during bootstrapping).
Basesystem should be the first package installed on a system, and it
should never be removed.

%description minimal
Basesystem defines the components of a basic Mandriva Linux system (for
example, the package installation order to use during bootstrapping).
Basesystem should be the first package installed on a system, and it
should never be removed.

%description uml
Basesystem defines the components of a basic Mandriva Linux system (for
example, the package installation order to use during bootstrapping).
Basesystem should be the first package installed on a system, and it
should never be removed.

This package can be used to setup a full and working system runned with
kernel-uml, using urpmi %{name}-uml  --root ...

%files
%files minimal
%files uml
