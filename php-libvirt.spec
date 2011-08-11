%define		req_libvirt_version 0.6.2
%define		php_confdir %{_sysconfdir}/php.d 
%define		php_extdir  %{_libdir}/php/modules

Name:		php-libvirt
Version:	0.4.3
Release:	1%{?dist}%{?extra_release}
Summary:	PHP language binding for Libvirt

Group:		Development/Libraries
License:	LGPLv2+
URL:		http://libvirt.org/php
Source0:	http://libvirt.org/sources/php/php-libvirt-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	php-devel
BuildRequires:	libvirt-devel >= %{req_libvirt_version}
BuildRequires:	libxml2-devel
BuildRequires:	libxslt
BuildRequires:	xhtml1-dtds
Requires:	libvirt >= %{req_libvirt_version}
Requires:	php
Requires:	php(zend-abi) = %{php_zend_api}
Requires:	php(api) = %{php_core_api}

%define		debug_package	%{nil} 
%global		_use_internal_dependency_generator	0

%description
PHP language bindings for Libvirt API. 
For more details see: http://www.libvirt.org/php/

%package -n php-libvirt-doc
Summary:	Document of php-libvirt
Group:		Development/Libraries
BuildArch:	noarch
Requires:	php-libvirt = %{version}

%description -n php-libvirt-doc
PHP language bindings for Libvirt API. 
For more details see: http://www.libvirt.org/php/ http://www.php.net/

This package contain the document for php-libvirt.

%prep
%setup -q -n php-libvirt-%{version}

%build
%configure
./configure --with-html-dir=%{_datadir}/doc --with-html-subdir=%{name}-%{version}/html --libdir=%{php_extdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%{php_extdir}/php-libvirt.so
%config(noreplace) %{php_confdir}/php-libvirt.ini

%files -n php-libvirt-doc
%defattr(-,root,root,-)
%doc README
%dir %{_datadir}/doc/%{name}-%{version}
%{_datadir}/doc/%{name}-%{version}/html

%changelog
* Thu Aug 11 2011 Michal Novotny <minovotn@redhat.com> - 0.4.3
- Rebase to 0.4.3 from master branch

* Tue Apr 19 2011 Michal Novotny <minovotn@redhat.com> - 0.4.1-5
- Minor memory leak fixes
- Several bug fixes

* Mon Apr 11 2011 Michal Novotny <minovotn@redhat.com> - 0.4.1-4
- Add new storagepool API functions
- Add optional xPath argument for *_get_xml_desc() functions
- Add new network API functions
- Add new API functions to add/remove disks

* Wed Mar 23 2011 Michal Novotny <minovotn@redhat.com> - 0.4.1-3
- Add connection information function
- Add coredump support
- Add snapshots support
- Improve error reporting for destructors

* Thu Mar 10 2011 Michal Novotny <minovotn@redhat.com> - 0.4.1-2
- Changes done to comply with Fedora package policy

* Tue Feb 8 2011 Michal Novotny <minovotn@redhat.com> - 0.4.1-1
- Initial commit (from github)
