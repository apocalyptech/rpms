# $Id$
# Authority: dag
# Upstream: Paul Marquess <pmqs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DB_File

Summary: Perl module providing access to Berkeley DB version 1.x
Name: perl-DB_File
Version: 1.815
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DB_File/

Source: http://www.cpan.org/modules/by-module/DB_File/DB_File-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-DB_File is a Perl module providing access to Berkeley DB version 1.x.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/DB_File.3pm*
%{perl_vendorarch}/DB_File.pm
%{perl_vendorarch}/auto/DB_File/

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.815-1
- Initial package. (using DAR)
