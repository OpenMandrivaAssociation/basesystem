#rh-7.0-2

%define with_systemd 1

Summary:	The skeleton package which defines a simple system
Name:		basesystem
Version:	2012
Release:	3
License:	GPLv2+
Group:		System/Base
Requires:	kernel basesystem-minimal
%ifnarch %{mips}
Requires:	bootloader
%endif
# (sb) need pdisk hfsutils ybin mktemp to setup bootloader PPC
# (fg) 20001027 ia64 uses eli as a bootloader
%ifarch ia64
Requires:	mkinitrd-command
%endif

%package	minimal
Summary:	The skeleton package which defines a simple system for chroot systems
Group:		System/Base

Requires:	setup filesystem sed kbd utempter
Requires:	chkconfig coreutils crontabs dev
Requires:	e2fsprogs etcskel findutils grep gzip gzip-utils less
Requires:	logrotate losetup mingetty mount net-tools passwd procps
Requires:	psmisc rootfiles rpm sash shadow-utils
Requires:	stat tar termcap time util-linux vim
Requires:	vixie-cron which perl-base common-licenses
Requires:	kmod
Requires:	rosa-release
Requires:	syslog-daemon
Requires:	bzip2 xz
%if %{with_systemd}
Requires(post):	systemd-sysvinit
%else
Requires(post):	sysvinit
Requires:	initscripts
%endif

# (gb) Add timezone database here for now before moving it to DrakX
Requires:	timezone
Suggests:	prelink

%package	uml
Summary:	The skeleton package which defines a simple system to be run under UML
Group:		System/Base
Requires:	basesystem-minimal
Requires:	dhcpcd
Requires:	urpmi

%description
Basesystem defines the components of a basic Rosa Linux system (for
example, the package installation order to use during bootstrapping).
Basesystem should be the first package installed on a system, and it
should never be removed.

%description minimal
Basesystem defines the components of a basic Rosa Linux system (for
example, the package installation order to use during bootstrapping).
Basesystem should be the first package installed on a system, and it
should never be removed.

%description uml
Basesystem defines the components of a basic Rosa Linux system (for
example, the package installation order to use during bootstrapping).
Basesystem should be the first package installed on a system, and it
should never be removed.

This package can be used to setup a full and working system runned with
kernel-uml, using urpmi %{name}-uml  --root ...

%files
%files minimal
%files uml


%changelog
* Tue Jul 26 2012 Alex Burmashev <alex.burmashev@rosalab.ru> 2012-1
- import from cooker

* Fri Jul 20 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2012-4
+ Revision: 810473
- require kmod instead of module-init-tools on mdv 2012

