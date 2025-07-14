Summary:	Fax4CUPS - CUPS backend for a serial fax modem
Summary(pl.UTF-8):	Fax4CUPS - backend CUPS-a do szeregowych fax-modemów
Name:		fax4CUPS
Version:	1.24
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://vigna.dsi.unimi.it/fax4CUPS/%{name}-%{version}.tar.gz
# Source0-md5:	42b1a28bba0d91b2e5bd2390fc956abb
Source1:	%{name}-hylafax.config
Patch0:		%{name}-hylafax.patch
URL:		http://vigna.dsi.unimi.it/fax4CUPS/
BuildRequires:	cups-devel
Requires:	bash
Requires:	cups
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fax4CUPS - CUPS backend for a serial fax modem.

%description -l pl.UTF-8
Fax4CUPS - backend CUPS-a do szeregowych fax-modemów.

%package -n cups-backend-fax-compat
Summary:	Compatibility fax backend
Summary(pl.UTF-8):	Backend faksowy dla kompatybilności
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description -n cups-backend-fax-compat
Compatibility fax backend.

%description -n cups-backend-fax-compat -l pl.UTF-8
Backend faksowy dla kompatybilności.

%package -n cups-backend-efax
Summary:	efax backend
Summary(pl.UTF-8):	Backend do efaksa
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	efax

%description -n cups-backend-efax
efax backend.

%description -n cups-backend-efax -l pl.UTF-8
Backend do efaksa.

%package -n cups-backend-hylafax
Summary:	hylafax backend
Summary(pl.UTF-8):	Backend do hylafaksa
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	hylafax-client

%description -n cups-backend-hylafax
hylafax backend.

%description -n cups-backend-hylafax -l pl.UTF-8
Backend do hylafaksa.

%package -n cups-backend-mgetty
Summary:	mgetty backend
Summary(pl.UTF-8):	Backend do mgetty
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	mgetty

%description -n cups-backend-mgetty
mgetty backend.

%description -n cups-backend-mgetty -l pl.UTF-8
Backend do mgetty.

%package -n cups-backend-capisuite
Summary:	capisuite backend
Summary(pl.UTF-8):	Backend do capisuite
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description -n cups-backend-capisuite
capisuite backend.

%description -n cups-backend-capisuite -l pl.UTF-8
Backend do capisuite.

%prep
%setup -q
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

install -d $RPM_BUILD_ROOT%(cups-config --serverbin)/backend
install -d $RPM_BUILD_ROOT%(cups-config --datadir)/model
install -d $RPM_BUILD_ROOT%(cups-config --serverroot)

install fax efax hylafax mgetty-fax $RPM_BUILD_ROOT%(cups-config --serverbin)/backend
install *.ppd $RPM_BUILD_ROOT%(cups-config --datadir)/model
install %{SOURCE1} $RPM_BUILD_ROOT%(cups-config --serverroot)/hylafax

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
%config(noreplace) %verify(not md5 mtime size) %(cups-config --serverroot)/hylafax

%files -n cups-backend-mgetty
%defattr(644,root,root,755)
%attr(755,root,root) %(cups-config --serverbin)/backend/mgetty-fax
%(cups-config --datadir)/model/mgetty-fax.ppd

%files -n cups-backend-capisuite
%defattr(644,root,root,755)
%(cups-config --datadir)/model/capisuite-fax.ppd
