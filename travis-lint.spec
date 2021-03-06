#
# Conditional build:
%bcond_with	tests		# build without tests

Summary:	Checks your .travis.yml for possible issues, deprecations and so on
Name:		travis-lint
Version:	1.8.0
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	c4a1e80786570ac94b10662275367701
URL:		https://github.com/travis-ci/travis-lint
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-rspec < 3
BuildRequires:	ruby-rspec >= 2.8
%endif
Requires:	ruby-hashr < 0.1
Requires:	ruby-hashr >= 0.0.22
Requires:	ruby-safe_yaml < 0.10
Requires:	ruby-safe_yaml >= 0.9.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
travis-lint is a tool that check your .travis.yml for possible issues,
deprecations and so on. Recommended for all travis-ci.org users.

%prep
%setup -q
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/travis-lint
%dir %{ruby_vendorlibdir}/travis
%{ruby_vendorlibdir}/travis/lint.rb
%{ruby_vendorlibdir}/travis/lint
