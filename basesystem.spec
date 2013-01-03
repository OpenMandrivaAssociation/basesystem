%define with_systemd 1

Summary:	Skeleton package which defines a simple %{distribution} system
Name:		basesystem
Version:	2013
Release:	6
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

%package	minimal
Summary:	Minimalistic skeleton package definining a simple %{distribution} system
Requires(pre):	setup
Requires(pre):	filesystem
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
%if %mdvver >= 201300
Requires:	procps-ng
%else
Requires:	procps
%endif
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
Requires:	mandriva-release >= 2013.0
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

%changelog
* Thu Dec 13 2012 Bernhard Rosenkränzer <bero@bero.eu> 2013-3
- Remove rosa-release-common conflict because mandriva-release-common
  provides it

* Wed Dec 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2013-1
- add conflict on rosa-release-common to workaround unversioned obsoletes
  creating issues when upgrading from cooker

* Tue Sep 11 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2012-7
+ Revision: 816758
- remove redundant requires on losetup and mount
- spec file clean

* Sun Sep 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2012-6
+ Revision: 816572
- add missing summary tags
- add a conflicts on 'makedev'
- drop dependency on 'dev' (makedev) as it's deprecated since ages ago
- move logrotate out of minimal
- move e2fsprogs out of minimal
- fix summary-too-long
- move crontabs out of stable
- move kbd out of minimal
- move sysvinit, systemd & initscripts out of minimal
- move syslog-daemon out of minimal
- drop dependency on sash
- move common-licenses out of minimal package
- move vixie-cron out of minimal package
- move prelink suggests out of minimal package
- we don't need kmod without no kernel, so move requires out of minimal package
- change requires on vim to suggests

* Fri Jul 20 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2012-4
+ Revision: 810473
- require kmod instead of module-init-tools on mdv 2012

* Fri Jul 20 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2012-3
+ Revision: 810362
- do not require initscripts when systemd is enabled

* Tue Jun 05 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2012-2
+ Revision: 802667
- change dhcp-client dependency to dhcp-client-daemon so that dhcpcd can satisfy
  it as well
- change mkinitrd dependency to mkinitrd-command
- add a suggests on prelink
- bump version to 2012
- rebuild to get rid of rpmlib(DistEpoch) blunder and also clean out a bit

* Tue Mar 13 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2011.0-7
+ Revision: 784611
- require new gzip-utils package (contains zcat etc.)

* Sat Dec 03 2011 Paulo Andrade <pcpa@mandriva.com.br> 2011.0-6
+ Revision: 737536
- systemd-sysvinit provides sysvinit.

* Sat Dec 03 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2011.0-5
+ Revision: 737516
- remove obsolete and broken dependency on libgcc

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - add conflicts on sysvinit

* Sat Nov 19 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2011.0-3
+ Revision: 731778
- use post requires

* Wed Nov 09 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2011.0-2
+ Revision: 729489
- requires systemd-sysvinit instead of sysvinit

* Tue Apr 19 2011 Antoine Ginies <aginies@mandriva.com> 2011.0-1
+ Revision: 655951
- bump to 2011 release

* Thu Feb 24 2011 Eugeni Dodonov <eugeni@mandriva.com> 2010.0-4
+ Revision: 639731
- Add requires on bzip2 and xz

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 2010.0-3mdv2011.0
+ Revision: 603755
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2010.0-2mdv2010.1
+ Revision: 522188
- rebuilt for 2010.1

* Fri Sep 25 2009 Olivier Blin <blino@mandriva.org> 2010.0-1mdv2010.0
+ Revision: 448803
- bump version to 2010.0
- do not require bootloader for mips (from Arnaud Patard)
