
# Conditional build:
%bcond_with	tests	# perform "make test" (requires database connection)

%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	DBI-mysql
Summary:	Extensions to Class::DBI for MySQL
Summary(pl):	Rozszerzenie Class::DBI dla MySQL-a
Name:		perl-Class-DBI-mysql
Version:	0.22
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a800b64d88c8ce681e7a23e472156615
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an extension to Class::DBI, containing several functions and
optimisations for the MySQL database. Instead of setting Class::DBI as
your base class, use this instead.

%description -l pl
Jest to rozszerzenie Class::DBI, zawieraj�ce kilka funkcji i
optymalizacji dla bazy danych MySQL. Zamiast ustawiania jako klas�
podstawow� Class::DBI, mo�na ustawi� t�.

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
