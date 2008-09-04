Name: funcoeszz
Version: 4.0518
Release: 61042cl
Summary: Handy bash functions called zz*
Summary(pt_BR): Fun��es �teis em bash chamadas zz*
Group: Utilities
Group(pt_BR): Utilit�rios
Group(es): Utilitarios
License: GPL
URL: http://aurelio.net/zz
Source: %{name}-%{version}.tgz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Handy bash functions called zz*, to deal with files, internet dictionary
queries, freshmeat, and others.
    
%description -l pt_BR
Fun��es �teis em bash de aplica��es diversificadas como manipular arquivos,
fazer c�lculos e fazer consultas na internet em dicion�rios e tradutores, bem
como cota��es, dicas-l, freshmeat, detran, imposto de renda, cep, etc.

%prep
%setup -q

%install
install -d    %{buildroot}%{_bindir}
cp -r %{name} %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root,0755)
%{_bindir}/%{name}



