Summary:	Fax4CUPS - CUPS backend for a serial fax modem
Name:		fax4CUPS
Version:	1.22
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://gongolo.usr.dsi.unimi.it/~vigna/%{name}/%{name}-%{version}.tar.gz
URL:		http://gongolo.usr.dsi.unimi.it/~vigna/%{name}/
Requires:	cups
BuildRequires:	cups-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fax4CUPS - CUPS backend for a serial fax modem

%package -n cups-backend-fax-compat
Summary:	Compatibility fax backend
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description -n cups-backend-fax-compat
Compatibility fax backend.

%package -n cups-backend-efax
Summary:	efax backend
Group:		Applications/Communications
Requires:	%{name} = %{version}
Requires:	efax

%description -n cups-backend-efax
efax backend

%package -n cups-backend-hylafax
Summary:	hylafax backend
Group:		Applications/Communications
Requires:	%{name} = %{version}
Requires:	hylafax-client

%description -n cups-backend-hylafax
hylafax backend

%prep
%setup -q

%build
exit 0

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

install -d $RPM_BUILD_ROOT%(cups-config --serverbin)/backend
install -d $RPM_BUILD_ROOT%(cups-config --datadir)/model

install fax efax hylafax $RPM_BUILD_ROOT%(cups-config --serverbin)/backend
install *.ppd $RPM_BUILD_ROOT%(cups-config --datadir)/model

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_mandir}/man1/*

%files -n cups-backend-fax-compat
%defattr(644,root,root,755)
%attr(755,root,root) %(cups-config --serverbin)/backend/fax
%(cups-config --datadir)/model/fax.ppd

%files -n cups-backend-efax
%defattr(644,root,root,755)
%attr(755,root,root) %(cups-config --serverbin)/backend/efax
%(cups-config --datadir)/model/efax.ppd

%files -n cups-backend-hylafax
%defattr(644,root,root,755)
%attr(755,root,root) %(cups-config --serverbin)/backend/hylafax
%(cups-config --datadir)/model/hylafax.ppd
