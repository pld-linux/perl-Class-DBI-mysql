
# Conditional build:
%bcond_with	tests	# perform "make test" (requires database connection)

%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	DBI-mysql
Summary:	Extensions to Class::DBI for MySQL
Summary(pl.UTF-8):	Rozszerzenie Class::DBI dla MySQL-a
Name:		perl-Class-DBI-mysql
Version:	1.00
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3bee2423ba61348a54201f4aca25e79b
URL:		http://search.cpan.org/dist/Class-DBI-mysql/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# not autodetected
Requires:	perl-Class-DBI
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an extension to Class::DBI, containing several functions and
optimisations for the MySQL database. Instead of setting Class::DBI as
your base class, use this instead.

%description -l pl.UTF-8
Jest to rozszerzenie Class::DBI, zawierające kilka funkcji i
optymalizacji dla bazy danych MySQL. Zamiast ustawiania jako klasę
podstawową Class::DBI, można ustawić tę.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/DBI/mysql.pm
%{_mandir}/man3/*
