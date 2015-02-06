%define upstream_name    AI-NNFlex
%define upstream_version 0.24

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Flexible API for neural networks
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/AI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Math::Matrix)
BuildArch:	noarch

%description
AI::NNFlex is a base class for constructing your own neural network
modules. To implement a neural network, start with the documentation for
AI::NNFlex::Backprop, included in this distribution

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES INSTALL MANIFEST README.txt TODO
%doc examples/*.pl examples/cars/cars.pl
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.240.0-2mdv2011.0
+ Revision: 654828
- rebuild for updated spec-helper

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-1mdv2011.0
+ Revision: 401791
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.24-3mdv2010.0
+ Revision: 375967
- rebuild

* Thu Apr 02 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.24-2mdv2009.1
+ Revision: 363431
- import perl-AI-NNFlex


* Wed Apr 01 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.24-2mdv2009.1
- include some docs and examples

* Wed Apr 01 2009 cpan2dist 0.24-1mdv
- initial mdv release, generated with cpan2dist

