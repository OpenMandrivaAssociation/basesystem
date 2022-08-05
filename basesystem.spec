Summary:	Skeleton package which defines a simple %{distribution} system
Name:		basesystem
# Ugly, but needed to allow for 2015.0 -> 3.0 transition
Epoch:		1
Version:	4
Release:	26
License:	GPLv2+
Group:		System/Base
%ifnarch %{riscv}
# FIXME Remove ifnarch... once we have a generic RISC-V kernel
Requires:	kernel
%endif
Requires(pre):	basesystem-minimal
Requires:	etcskel
Requires:	gnupg
Requires:	hostname
Requires:	pinentry
Requires:	libutempter
Requires:	less
Requires:	net-tools
Requires:	procps-ng
Requires:	psmisc
Requires:	texteditor
Requires:	time
%ifnarch %{armx} %{riscv}
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
Requires:	systemd-rpm-macros
Requires:	distro-release-rpm-setup
Requires:	e2fsprogs
Requires:	logrotate
Requires:	iputils
Requires:	pam
Requires:	pam-cracklib
Requires:	shadow
Requires:	passwd
Requires:	wget
Conflicts:	makedev <= 4.4-15
Recommends:	sudo
Recommends:	dnf

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
Requires:	/bin/sh
Requires:	coreutils
Requires:	findutils
Requires:	grep
Requires:	pigz
Requires:	rpm
Requires:	bsdtar
Requires:	util-linux
Requires:	which
Requires:	distro-release >= %{version}
Requires:	pbzip2
Requires:	unzip
Requires:	zstd
Requires:	xz

%description minimal
Basesystem defines the components of a basic %{distribution} system (for
example, the package installation order to use during bootstrapping).
Basesystem should be the first package installed on a system, and it
should never be removed.

%package build
Summary:	The skeleton package which defines a simple system for package builds
Group:		System/Base
Obsoletes:	task-devel < 2015.0-1
Provides:	task-devel = 2015.0-1
Requires:	basesystem-minimal
# (tpg) keep all the configuration for RPM build in distro-release
Requires:	distro-release-rpm-setup-build
%ifarch %{riscv}
Requires:	atomic-devel
%endif
Requires:	autoconf
Requires:	automake
Requires:	binutils
Requires:	clang
Requires:	coreutils
Requires:	cpio
Requires:	debugedit
Requires:	diffutils
Requires:	distro-release-repos-pkgprefs
Requires:	distro-release-rpmlint-policy
Requires:	dwz
Requires:	elfutils >= 0.167-2
Requires:	file
Requires:	gawk
Requires:	gcc
Requires:	gcc-c++
Requires:	glibc-devel
Requires:	gnupg
Requires:	go-srpm-macros
Requires:	libtool-base
Requires:	llvm-polly
Requires:	locales
Requires:	locales-en
Requires:	make
Requires:	%mklibname -d stdc++
Requires:	patch
Requires:	pbzip2
Requires:	pigz
Requires:	pkgconf
Requires:	python >= 3.0
Requires:	python-packaging
Requires:	python-pkg-resources
Requires:	rpm-build
Requires:	rpmlint
Requires:	rust-srpm-macros
Requires:	shadow
Requires:	spec-helper >= 0.31.12
Requires:	systemd-rpm-macros
Requires:	tar >= 3.3.2
Requires:	unzip
Requires:	/usr/bin/gdb-add-index
Requires:	xz
Requires:	zstd

%description build
Basesystem defines the components of a basic OpenMandriva Linux build system 
for the package installation order to use during bootstrapping.

This package can be used to setup a full and working system for package builds

%package container
Summary:	Skeleton package definining a simple uml %{distribution} system
Obsoletes:	basesystem-uml < 1:4-22
Requires:	basesystem-minimal
Recommends:	microdnf

%description container
Basesystem defines the components of a basic %{distribution} system (for
example, the package installation order to use during bootstrapping).
Basesystem should be the first package installed on a system, and it
should never be removed.

This package can be used to setup a full and working system running
in a container.

%files
%files minimal
%files container
%files build
