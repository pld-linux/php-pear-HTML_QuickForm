%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - methods for creating, validating, processing HTML forms
Summary(pl.UTF-8):	%{_pearname} - metody do tworzenia, kontroli i przetwarzania formularzy HTML
Name:		php-pear-%{_pearname}
Version:	3.2.9
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1cebd6a4a9a1ebb8c3c7f501bba3e47d
URL:		http://pear.php.net/package/HTML_QuickForm/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2
Requires:	php-pear >= 4:1.0-9.1
Requires:	php-pear-HTML_Common >= 1.2.1
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

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa HTML_QuickForm zawiera metody to tworzenia, kontroli poprawności
i przetwarzania formularzy HTML. Cechy:
- tworzy elementy formularzy różnego typu zgodnie z xHTML
- pozwala na wybór nieograniczonej liczby atrybutów HTML
- pozwala tworzyć własne elementy przy użyciu własnych klas
- przetwarza wartości z formularzy (należy podmienić metodę process)
- tworzy kod sprawdzający w JavaScripcie przy użyciu wyrażeń
  regularnych
- kontroluje poprawność wprowadzonych danych także po stronie serwera
- pozwala na tworzenie własnych reguł kontrolujących poprawność
- obsługuje upload plików
- pozwala na "zamrożenie" niektórych elementów formularza
- pozwala na zmianę wyglądu formularza na wiele sposobów
- modyfikacja elementów formularzy poprzez wzorce.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
mv docs/HTML_QuickForm/docs examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Renderer
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Rule
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Renderer/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Rule/*.php
%{_examplesdir}/%{name}-%{version}
