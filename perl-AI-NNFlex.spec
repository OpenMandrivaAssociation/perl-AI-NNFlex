
%define realname   AI-NNFlex
%define version    0.24
%define release    %mkrel 3

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Flexible API for neural networks
Source:     http://www.cpan.org/modules/by-module/AI/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Math::Matrix)

BuildArch: noarch

%description
AI::NNFlex is a base class for constructing your own neural network
modules. To implement a neural network, start with the documentation for
AI::NNFlex::Backprop, included in this distribution





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGES INSTALL MANIFEST README.txt TODO
%doc examples/*.pl examples/cars/cars.pl
#%{_mandir}/man3/*
%perl_vendorlib/*


