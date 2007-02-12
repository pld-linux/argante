Summary:	Virtual operating system
Summary(pl.UTF-8):	Wirtualny system operacyjny
Name:		argante
Version:	1.0
Release:	1
License:	LGPL
Group:		Applications/System
Source0:	http://lcamtuf.na.export.pl/arg.tgz
# Source0-md5:	cf5d46d8e5d12521abb7ad4e6277d331
URL:		http://agt.buka.org/
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	svgalib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Argante is a fully-operational, software-embedded virtual operating
system environment, designed for high security, efficiency and
usability, reducing amount of resources required to develop complex
networked applications and solutions. It supports Hierarchical Access
Control, remote Inter-Process Communication for distributed computing
(easy clusters / virtual router development) as well as many other
features. It comes with comprehensive documentation, many examples, a
compact HTTP server and DVR (distributed virtual router) examples.

%description -l pl.UTF-8
Argante to w pełni sprawny wirtualny systemem operacyjny
zaprojektowany do tworzenia aplikacji i rozwiązań sieciowych o
wysokim poziomie bezpieczeństwa, skuteczności i użyteczności. System
wspiera HAC (hierarchiczne listy dostępu, zdalną komunikację
międzyprocesową dla przetwarzania rozproszonego (klastry, wirtualne
routery) jak i wiele innych. Wraz z systemem dostarczana jest
dokumentacja, wiele przykładów, kompaktowy serwer HTTP oraz DVR
(rozproszony router wirtualny).

%prep
%setup -q -n Argante
touch * */* */*/*

%build
OPT="%{rpmcflags}" ./build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/argante,%{_mandir}/man1}

install argante			$RPM_BUILD_ROOT%{_bindir}
install tools/{agt*,ripcd}	$RPM_BUILD_ROOT%{_bindir}
install compiler/agtc		$RPM_BUILD_ROOT%{_bindir}
install hll/{ahlt,elim,acc}	$RPM_BUILD_ROOT%{_bindir}
install modules/*.so		$RPM_BUILD_ROOT%{_libdir}/argante
install Documentation/man/*.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Documentation/{ANNOUNCE,ChangeLog,DVR.README,People,README,TODO} Examples conf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %dir %{_libdir}/argante
%attr(755,root,root) %{_libdir}/argante/*.so
%{_mandir}/man*/*
