%define		pdir	MIME
%define		pnam	Base64-Scripts
Summary:	Scripts to decode/encode base64 and quoted-printable
Summary(pl.UTF-8):	Skrypty kodujące i dekodujące base64 i quoted-printable
Name:		perl-MIME-Base64-Scripts
Version:	1.00
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MIME/GAAS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7e861d070b3063b0bf14ef3b3653b029
URL:		http://search.cpan.org/dist/MIME-Base64-Scripts/
BuildRequires:	perl-MIME-Base64 >= 3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a few scripts that used to live in the
MIME-Base64 package but was not assimilated as part of the perl-5.8
core.

%description -l pl.UTF-8
Ten pakiet zawiera kilka skryptów obecnych wcześniej w pakiecie
MIME-Base64, ale nie włączonych do dystrybucji perla 5.8.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
