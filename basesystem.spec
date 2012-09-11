%define with_systemd 1

Summary:	Skeleton package which defines a simple %{distribution} system
Name:		basesystem
Version:	2012
Release:	7
License:	GPLv2+
Group:		System/Base
Requires:	kernel
Requires:	basesystem-minimal
%ifnarch %{mips}
Requires:	bootloader
%endif
# (sb) need pdisk hfsutils ybin mktemp to setup bootloader PPC
%ifarch ppc
Requires:	pdisk
Requires:	hfsutils
Requires:	ybin
Requires:	mktemp
Requires:	mkinitrd
Requires:	pmac-utils
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
Conflicts:	makedev <= 4.4-15

%description
Basesystem defines the components of a basic %{distribution} system (for
example, the package installation order to use during bootstrapping).
Basesystem should be the first package installed on a system, and it
should never be removed.

%package minimal
Summary:	Minimalistic skeleton package definining a simple %{distribution} system
Requires:	setup
Requires:	filesystem
Requires:	sed
Requires:	utempter
Requires:	chkconfig
Requires:	coreutils
Requires:	etcskel
Requires:	findutils
Requires:	grep
Requires:	gzip
Requires:	gzip-utils
Requires:	less
Requires:	mingetty
Requires:	net-tools
Requires:	passwd
Requires:	procps
Requires:	psmisc
Requires:	rootfiles
Requires:	rpm
Requires:	shadow-utils
Requires:	stat
Requires:	tar
Requires:	termcap
Requires:	time
Requires:	util-linux
Requires:	which
Requires:	perl-base
Requires:	mandriva-release >= 2008.1
Requires:	bzip2
Requires:	xz
Suggests:	vim

# (gb) Add timezone database here for now before moving it to DrakX
Requires:	timezone

%description minimal
Basesystem defines the components of a basic %{distribution} system (for
example, the package installation order to use during bootstrapping).
Basesystem should be the first package installed on a system, and it
should never be removed.

%package uml
Summary:	Skeleton package definining a simple uml %{distribution} system
Requires:	basesystem-minimal
Requires:	dhcp-client-daemon
Requires:	urpmi

%description uml
Basesystem defines the components of a basic %{distribution} system (for
example, the package installation order to use during bootstrapping).
Basesystem should be the first package installed on a system, and it
should never be removed.

This package can be used to setup a full and working system runned with
kernel-uml, using urpmi %{name}-uml  --root ...

%files
%files minimal
%files uml
