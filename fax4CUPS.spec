Summary:	Fax4CUPS - CUPS backend for a serial fax modem
Summary(pl):	Fax4CUPS - backend CUPS-a do szeregowych fax-modemów
Name:		fax4CUPS
Version:	1.22
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://gongolo.usr.dsi.unimi.it/~vigna/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	0a7884a59986bd68686077e67ac4ffba
URL:		http://gongolo.usr.dsi.unimi.it/~vigna/%{name}/
BuildRequires:	cups-devel
Requires:	cups
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fax4CUPS - CUPS backend for a serial fax modem.

%description -l pl
Fax4CUPS - backend CUPS-a do szeregowych fax-modemów.

%package -n cups-backend-fax-compat
Summary:	Compatibility fax backend
Summary(pl):	Backend faksowy dla kompatybilności
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description -n cups-backend-fax-compat
Compatibility fax backend.

%description -n cups-backend-fax-compat -l pl
Backend faksowy dla kompatybilności.

%package -n cups-backend-efax
Summary:	efax backend
Summary(pl):	Backend do efaksa
Group:		Applications/Communications
Requires:	%{name} = %{version}
Requires:	efax

%description -n cups-backend-efax
efax backend.

%description -n cups-backend-efax -l pl
Backend do efaksa.

%package -n cups-backend-hylafax
Summary:	hylafax backend
Summary(pl):	Backend do hylafaksa
Group:		Applications/Communications
Requires:	%{name} = %{version}
Requires:	hylafax-client

%description -n cups-backend-hylafax
hylafax backend.

%description -n cups-backend-hylafax -l pl
Backend do hylafaksa.

%prep
%setup -q

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
