Summary:	Fax4CUPS - CUPS backend for a serial fax modem
Name:		fax4CUPS
Version:	1.22
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://gongolo.usr.dsi.unimi.it/~vigna/%{name}/%{name}-%{version}.tar.gz
URL:		http://gongolo.usr.dsi.unimi.it/~vigna/%{name}/
Requires:	cups
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fax4CUPS - CUPS backend for a serial fax modem

%package compat
Summary:	Compatibility fax backend
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description compat
Compatibility fax backend.

%package efax
Summary:	efax backend
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description efax
efax backend

%package hylafax
Summary:	hylafax backend
Group:		Applications/Communications
Requires:	%{name} = %{version}
Requires:	hylafax-client

%description hylafax
hylafax backend

%prep
%setup -q

%build
exit 0

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

install -d $RPM_BUILD_ROOT%{_libdir}/cups/backend
install -d $RPM_BUILD_ROOT%{_datadir}/cups/model

install fax efax hylafax $RPM_BUILD_ROOT%{_libdir}/cups/backend
install *.ppd $RPM_BUILD_ROOT%{_datadir}/cups/model

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_mandir}/man1/*

%files compat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cups/backend/fax
%{_datadir}/cups/model/fax.ppd

%files efax
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cups/backend/efax
%{_datadir}/cups/model/efax.ppd

%files hylafax
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cups/backend/hylafax
%{_datadir}/cups/model/hylafax.ppd
