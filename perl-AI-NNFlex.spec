%define upstream_name    AI-NNFlex
%define upstream_version 0.24

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Flexible API for neural networks
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/AI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Math::Matrix)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
AI::NNFlex is a base class for constructing your own neural network
modules. To implement a neural network, start with the documentation for
AI::NNFlex::Backprop, included in this distribution

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
