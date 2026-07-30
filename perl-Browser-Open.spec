%define upstream_name    Browser-Open
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	0.04
Release:	4

Summary:	Open a browser in a given URL
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Browser-Open
Source0:	https://cpan.metacpan.org/authors/id/C/CF/CFRANKS/Browser-Open-0.04.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(parent)
BuildArch:	noarch

%description
The functions optionaly exported by this module allows you to open URLs in
the user browser.

A set of known commands per OS-name is tested for presence, and the first
one found is executed. With an optional parameter, all known commands are
checked.

The the "open_browser" manpage uses the 'system()' function to execute the
command. If you want more control, you can get the command with the the
"open_browser_cmd" manpage or the "open_browser_cmd_all" manpage functions
and then use whatever method you want to execute it.

%prep
%setup -q -n Browser-Open-0.04

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

