Summary:	Skeleton package which defines a simple %{distribution} system
Name:		basesystem
# Ugly, but needed to allow for 2015.0 -> 3.0 transition
Epoch:		1
Version:	4
Release:	17
License:	GPLv2+
Group:		System/Base
Requires:	kernel
Requires(pre):	basesystem-minimal
Requires:	etcskel
Requires:	findutils
Requires:	gnupg
Requires:	gzip-utils
Requires:	hostname
Requires:	pinentry
Requires:	libutempter
Requires:	less
Requires:	net-tools
Requires:	procps-ng
Requires:	psmisc
Requires:	rootfiles
Requires:	vim-minimal
Requires:	time
%ifnarch %{armx}
Requires:	bootloader
%endif
Requires:	common-licenses
Requires:	systemd
Requires:	systemd-analyze >= 238-4
Requires:	systemd-coredump >= 235-9
Requires:	systemd-console >= 235-9
Suggests:	systemd-documentation >= 235-9
Requires:	systemd-hwdb >= 235-9
Requires:	systemd-locale >= 235-9
Requires:	systemd-polkit >= 235-9
Requires:	systemd-cryptsetup >= 238-3
Requires:	e2fsprogs
Requires:	logrotate
Requires:	iputils
Requires:	pam
Requires:	pam-cracklib
Requires:	shadow
Requires:	passwd
Conflicts:	makedev <= 4.4-15
Recommends:	sudo

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
Requires:	rootfiles
Requires:	bash
Requires:	coreutils
Requires:	grep
Requires:	gzip
Requires:	ncurses
Requires:	rpm
Requires:	bsdtar
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

%package build
Summary:	The skeleton package which defines a simple system for package builds
Group:		System/Base
Requires:	basesystem-minimal rpmlint-distro-policy
Requires:	openmandriva-repos-pkgprefs dwz
Requires:	locales locales-en task-devel
Requires:	gnupg shadow wget

%description build
Basesystem defines the components of a basic OpenMandriva Linux build system 
for the package installation order to use during bootstrapping.

This package can be used to setup a full and working system for package builds

%package uml
Summary:	Skeleton package definining a simple uml %{distribution} system
Requires:	basesystem-minimal
Requires:	dhcp-client-daemon
Requires:	dnf

%description uml
Basesystem defines the components of a basic %{distribution} system (for
example, the package installation order to use during bootstrapping).
Basesystem should be the first package installed on a system, and it
should never be removed.

This package can be used to setup a full and working system runned with
kernel-uml, using dnf %{name}-uml  --root ...

%files
%files minimal
%files uml
%files build
