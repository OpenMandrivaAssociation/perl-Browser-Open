%define upstream_name    Browser-Open
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Open a browser in a given URL
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Browser/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 657388
- rebuild for updated spec-helper

* Tue Mar 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.30.0-1
+ Revision: 644904
- import perl-Browser-Open

