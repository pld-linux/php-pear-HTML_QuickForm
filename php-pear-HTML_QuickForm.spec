%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - methods for creating, validating, processing HTML forms
Summary(pl):	%{_pearname} - metody do tworzenia, kontroli i przetwarzania formularzy HTML
Name:		php-pear-%{_pearname}
Version:	2.3
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
Patch0:		%{name}-cosmetic.patch
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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
Klasa HTML_QuickForm zawiera metody to tworzenia, kontroli poprawno¶ci
i przetwarzania formularzy HTML. Cechy:
- tworzy elementy formularzy ró¿nego typu zgodnie z xHTML
- pozwala na wybór nieograniczonej liczby atrybutów HTML
- pozwala tworzyæ w³asne elementy przy u¿yciu w³asnych klas
- przetwarza warto¶ci z formularzy (nale¿y podmieniæ metodê process)
- tworzy kod sprawdzaj±cy w JavaScripcie przy u¿yciu wyra¿eñ
  regularnych
- kontroluje poprawno¶æ wprowadzonych danych tak¿e po stronie serwera
- pozwala na tworzenie w³asnych regu³ kontroluj±cych poprawno¶æ
- obs³uguje upload plików
- pozwala na "zamro¿enie" niektórych elementów formularza
- pozwala na zmianê wygl±du formularza na wiele sposobów
- modyfikacja elementów formularzy poprzez wzorce.

%prep
%setup -q -c
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
