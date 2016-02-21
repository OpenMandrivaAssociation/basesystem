Summary:	Skeleton package which defines a simple %{distribution} system
Name:		basesystem
Version:	2015.0
Release:	0.11
License:	GPLv2+
Group:		System/Base
Requires:	kernel
Requires(pre):	basesystem-minimal
Requires:	etcskel
Requires:	libutempter
Requires:	less
Requires:	net-tools
Requires:	procps-ng
Requires:	psmisc
Requires:	rootfiles
Requires:	vim
Requires:	time
%ifnarch %{arm}
Requires:	bootloader
%endif
Requires:	kmod
Requires:	common-licenses
Requires:	systemd
Requires:	kbd
Requires:	e2fsprogs
Requires:	logrotate
Conflicts:	makedev <= 4.4-15
Suggests:	sudo

%description
Basesystem defines the components of a basic %{distribution} system (for
example, the package installation order to use during bootstrapping).
Basesystem should be the first package installed on a system, and it
should never be removed.

%package minimal
Summary:	Minimalistic skeleton package definining a simple %{distribution} system
Requires:	setup
Requires(pre):	filesystem
Requires:	sed
Requires:	bash
Requires:	coreutils
Requires:	findutils
Requires:	grep
Requires:	gzip
Requires:	gzip-utils
Requires:	ncurses
Requires:	pam
Requires:	passwd
Requires:	rpm
Requires:	shadow
# (tpg) we use bsdtar from libarchive as a replacement for tar
# originall tar was renamed to gnutar
# bsdtar froom libarchive provides tar, and bsdtar
%if "%{distepoch}" >= "2015.0"
Requires:	bsdtar
%else
Requires:	tar
%endif
Requires:	util-linux
Requires:	which
Requires:	distro-release >= %{version}
Requires:	bzip2
Requires:	xz
Requires:	wget

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
