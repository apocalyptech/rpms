# $Id$

# Authority: dries
# Upstream: Alistair Francis <alizta$cpan,org>

%define real_name Crypt-Vigenere
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Implementation of the Vigenere cipher
Name: perl-Crypt-Vigenere
Version: 0.07
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Vigenere/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/A/AL/ALIZTA/Crypt-Vigenere-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This modules allows you to recreate the workings of the cryptographic
cipher invented several hundred years ago by a French cryptographer,
Blaise de Vigenère. 

The Crypt::Vigenere module accepts only alpha characters in the keyword
and will return an undefined object if any other characters are entered.
The module also only encrypts/decrypts alpha characters, any other 
characters will be stripped out of the resulting encrption/decryption.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Crypt/Vigenere.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
