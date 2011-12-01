Summary: Perl bindings for the Newt library
Name: perl-Newt
Version: 1.08
Release: 26%{?dist}
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://search.cpan.org/~amedina/Newt-1.08/
Source: http://search.cpan.org/CPAN/authors/id/A/AM/AMEDINA/Newt-1.08.tar.gz
Patch0: newt-perl-1.08-debian.patch
Patch1: newt-perl-1.08-typemap.patch
Patch2: newt-perl-1.08-fix.patch
Patch3: newt-perl-1.08-xs.patch
Patch4: newt-perl-1.08-lang.patch
Patch5: perl-Newt-bz385751.patch
Patch6: perl-Newt-1.08-export.patch
Patch7: perl-Newt-1.08-pod.patch
Patch8: perl-Newt-1.08-formdestroy.patch
BuildRequires: newt-devel, perl-devel
Obsoletes: newt-perl < 1.08-15
Provides: newt-perl = %{version}-%{release}
Requires: %(eval `perl -V:version`; echo "perl(:MODULE_COMPAT_$version)")
License: GPL+ or Artistic

%description
This package provides Perl bindings for the Newt widget
library, which provides a color text mode user interface.

%prep
%setup -q -n Newt-%{version}
%patch0 -p1 -b .debian
%patch1 -p1 -b .valist
%patch2 -p1 -b .fix
%patch3 -p1 -b .exes
%patch4 -p1 -b .lang
%patch5 -p1 -b .bz385751
%patch6 -p1 -b .export
%patch7 -p1 -b .doc
%patch8 -p1 -b .formdestroy
rm -rf newtlib

%build
perl Makefile.PL PREFIX=%{_prefix} INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -exec rm -v {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc ChangeLog README
%{perl_vendorarch}/Newt.pm
%{perl_vendorarch}/auto/Newt
%{_mandir}/man3/Newt*

%changelog
* Thu Jun 17 2010 Joe Orton <jorton@redhat.com> - 1.08-26
- drop Newt::Form::DESTROY method (Petr Pisar, #600670)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.08-25
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 28 2009 Joe Orton <jorton@redhat.com> 1.08-23
- add fixes from Joe Ogulin (#489825)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Apr  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.08-21
- resolve bz 385751

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.08-20
- Rebuild for new perl (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.08-19
- Autorebuild for GCC 4.3

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.08-18
- rebuild for new perl

* Thu Aug 30 2007 Joe Orton <jorton@redhat.com> 1.08-17
- clarify License tag

* Tue Mar  6 2007 Joe Orton <jorton@redhat.com> 1.08-15
- rename to perl-Newt; Obsolete and Provide newt-perl (#226196)

* Thu Mar  1 2007 Joe Orton <jorton@redhat.com> 1.08-14
- various cleanups (Jason Tibbs, #226196)
- require perl-devel

* Tue Feb 27 2007 Joe Orton <jorton@redhat.com> 1.08-13
- clean up URL, Source, BuildRoot, BuildRequires

* Thu Dec 14 2006 Joe Orton <jorton@redhat.com> 1.08-12
- fix test.pl (Charlie Brady, #181674)

* Thu Dec 14 2006 Joe Orton <jorton@redhat.com> 1.08-11
- fix directory ownership (#216610)

* Wed Nov 15 2006 Joe Orton <jorton@redhat.com> 1.08-10
- fix compiler warnings (#155977)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.08-9.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.08-9.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.08-9.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Sep 27 2005 Petr Rockai <prockai@redhat.com> - 1.08-9
- rebuild against newt 0.52.0

* Fri Mar  4 2005 Joe Orton <jorton@redhat.com> 1.08-8
- rebuild

* Tue Aug 17 2004 Joe Orton <jorton@redhat.com> 1.08-7
- add perl MODULE_COMPAT requirement

* Mon Aug 16 2004 Joe Orton <jorton@redhat.com> 1.08-6
- rebuild

* Mon Sep  8 2003 Joe Orton <jorton@redhat.com> 1.08-5
- fix issue with non-English LANG setting (#67735)

* Tue Aug  5 2003 Joe Orton <jorton@redhat.com> 1.08-4
- rebuild

* Thu May  9 2002 Joe Orton <jorton@redhat.com> 1.08-3
- add newt requirement

* Wed Apr 03 2002 Gary Benson <gbenson@redhat.com> 1.08-2
- tweak perl dependency as suggested by cturner@redhat.com

* Wed Mar 20 2002 Gary Benson <gbenson@redhat.com>
- make like all the other perl modules we ship (bind to perl version,
  use perl dependency finding scripts, build filelist automatically).
- include documentation
- build against perl 5.6.1

* Thu Jan 10 2002 Joe Orton <jorton@redhat.com>
- Adapted for RHL

* Tue Sep 11 2001 Mark Cox <mjc@redhat.com>
- Change paths to new layout

* Mon Jun 11 2001 Joe Orton <jorton@redhat.com>
- Initial revision.
