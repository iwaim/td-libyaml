# $Id$
# Authority: dries
# Upstream: Kirill <xi$gamma,dn,ua>

Summary: Implementation of a YAML 1.1 parser and emitter
Name: td-libyaml
Version: 0.1.4
Release: 2%{?dist}
License: MIT/X Consortium
Group: Development/Libraries
URL: http://pyyaml.org/wiki/LibYAML

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: %{name}-%{version}.tar.gz
Patch0: libyaml-string-overflow.patch
Patch1: libyaml-node-id-hardening.patch
Patch2: libyaml-guard-against-overflows-in-indent-and-flow_level.patch
Patch3: CVE-2014-2525.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
LibYAML is a C library implementation of a YAML 1.1 parser and emitter.
It includes a Python language binding.

# 2011/08/01 Kazuki Ohta <kazuki.ohta@gmail.com>
# prevent stripping the debug info.
%define debug_package %{nil}
%define __strip /bin/true

%prep

%setup -n yaml-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build

%configure --disable-static --prefix=%{_libdir}/fluent/libyaml --exec-prefix=%{_libdir}/fluent/libyaml --libdir=%{_libdir}/fluent/libyaml/lib --includedir=%{_libdir}/fluent/libyaml/include
%{__make} %{?_smp_mflags} AM_CFLAGS=""

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc
%{_libdir}/fluent/libyaml/

%changelog
* Mon Jun 16 2014 IWAI, Masaharu <iwaim.sub@gmail.com> - 0.1.4-2
- add some patches from Debian wheezy: libyaml 0.1.4-2+deb7u4
 - libyaml-string-overflow.patch
 -  libyaml-node-id-hardening.patch
 -  libyaml-guard-against-overflows-in-indent-and-flow_level.patch
 -  CVE-2014-2525.patch

* Tue Dec 27 2011 Rilindo Foster (rilindo.foster@monzell.com - 0.1.4-1
- Updated to release 0.1.4, added path to pkgconfig

* Mon May 17 2010 Dag Wieers <dag@wieers.com> - 0.1.3-1
- Updated to release 0.1.3.

* Mon May 28 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.1-1
- Initial package.
