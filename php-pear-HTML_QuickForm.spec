%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - methods for creating, validating, processing HTML forms
Summary(pl):	%{_class}_%{_subclass} - metody do tworzenia, korekcji i przetwarzania formularzy HTML
Name:		php-pear-%{_pearname}
Version:	2.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
BuildRequires:	rpm-php-pearprov
URL:		http://pear.php.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::HTML_QuickForm package provides methods for creating,
validating, processing HTML forms. Features:
- Creates xHTML compliant form elements of various type.
- Allows you to choose an unlimited number of html attributes.
- Allows you to create your own custom elements using your own
  classes.
- Process form values (you should override the process method).
- Creates javascript validation code using regular expression.
- Server-side validation too.
- Allows you to create your own validation rules.
- Manages file uploads.
- Allows you to freeze some elements in your form.
- Allows you to customize the look of your form in many ways.
- Template-like form elements customization...

%description -l pl

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install *.php			$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_subclass}/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
