Summary:	Skeleton package which defines a simple %{distribution} system
Name:		basesystem
# Ugly, but needed to allow for 2015.0 -> 3.0 transition
Epoch:		1
Version:	4
Release:	30
License:	GPLv2+
Group:		System/Base
%ifnarch %{riscv}
# FIXME Remove ifnarch... once we have a generic RISC-V kernel
Requires:	kernel
%endif
Requires(pre):	basesystem-minimal
Requires(meta):	etcskel
Requires(meta):	gnupg
Requires(meta):	hostname
Requires(meta):	pinentry
Requires(meta):	libutempter
Requires(meta):	less
Requires(meta):	net-tools
Requires(meta):	procps-ng
Requires(meta):	psmisc
Requires(meta):	texteditor
Requires(meta):	time
Requires(meta):	timezone
%ifnarch %{armx} %{riscv}
Requires(meta):	bootloader
%endif
Requires(meta):	common-licenses
Requires(meta):	systemd
Requires(meta):	systemd-analyze >= 238-4
Requires(meta):	systemd-coredump >= 235-9
Requires(meta):	systemd-console >= 235-9
Suggests:	systemd-documentation >= 235-9
Requires(meta):	systemd-hwdb >= 235-9
Requires(meta):	systemd-locale >= 235-9
Requires(meta):	systemd-polkit >= 235-9
Requires(meta):	systemd-cryptsetup >= 238-3
Requires(meta):	systemd-rpm-macros
Requires(meta):	distro-release-rpm-setup
Requires(meta):	e2fsprogs
Requires(meta):	logrotate
Requires(meta):	iputils
Requires(meta):	pam
Requires(meta):	pam-cracklib
Requires(meta):	shadow
Requires(meta):	passwd
Requires(meta):	wget
Requires(meta):	util-linux
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
Requires(meta):	setup
Requires(pre):	filesystem
Requires(meta):	sed
Requires(meta):	rootfiles
Requires(meta):	/bin/sh
Requires(meta):	coreutils
Requires(meta):	findutils
Requires(meta):	grep
Requires(meta):	pigz
Requires(meta):	rpm
Requires(meta):	bsdtar
Requires(meta):	util-linux-core
Requires(meta):	which
Requires(meta):	distro-release >= %{version}
Requires(meta):	pbzip2
Requires(meta):	unzip
Requires(meta):	zstd
Requires(meta):	xz

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
Requires(meta):	basesystem-minimal
# (tpg) keep all the configuration for RPM build in distro-release
Requires(meta):	distro-release-rpm-setup-build
%ifarch %{riscv}
Requires(meta):	atomic-devel
%endif
Requires(meta):	autoconf
Requires(meta):	automake
Requires(meta):	binutils
Requires(meta):	clang
Requires(meta):	cmake
Requires(meta):	coreutils
Requires(meta):	cpio
Requires(meta):	debugedit
Requires(meta):	diffutils
Requires(meta):	distro-release-repos-pkgprefs
Requires(meta):	distro-release-rpmlint-policy
Requires(meta):	dwz
Requires(meta):	elfutils >= 0.167-2
Requires(meta):	file
Requires(meta):	gawk
Requires(meta):	gcc
Requires(meta):	gcc-c++
Requires(meta):	glibc-devel
Requires(meta):	gnupg
Requires(meta):	go-srpm-macros
Requires(meta):	libtool-base
Requires(meta):	llvm-polly
Requires(meta):	locales
Requires(meta):	locales-en
Requires(meta):	make
Requires(meta):	meson
Requires(meta):	%mklibname -d stdc++
Requires(meta):	patch
Requires(meta):	pbzip2
Requires(meta):	pigz
Requires(meta):	pkgconf
Requires(meta):	python >= 3.0
Requires(meta):	python-packaging
Requires(meta):	python-pkg-resources
Requires(meta):	rpm-build
Requires(meta):	rpmlint
Requires(meta):	rust-srpm-macros
Requires(meta):	spec-helper >= 0.31.12
Requires(meta):	systemd-rpm-macros
Requires(meta):	tar >= 3.3.2
Requires(meta):	unzip
Requires(meta):	/usr/bin/gdb-add-index
Requires(meta):	xz
Requires(meta):	zstd

%description build
Basesystem defines the components of a basic OpenMandriva Linux build system 
for the package installation order to use during bootstrapping.

This package can be used to setup a full and working system for package builds

%package container
Summary:	Skeleton package definining a simple uml %{distribution} system
Obsoletes:	basesystem-uml < 1:4-22
Requires(meta):	basesystem-minimal
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
