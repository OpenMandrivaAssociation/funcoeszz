Name: funcoeszz
Version: 8.7
Release: %mkrel 1
Summary: Handy bash functions called zz*
Summary(pt_BR): Fun��es �teis em bash chamadas zz*
Group: Utilities
Group(pt_BR): Utilit�rios
Group(es): Utilitarios
License: GPL
URL: http://funcoeszz.net/
Source0: http://funcoeszz.net/funcoeszz
Source1: zzwrapper
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Handy bash functions called zz*, to deal with files, internet dictionary
queries, freshmeat, and others.
    
%description -l pt_BR
Fun��es �teis em bash de aplica��es diversificadas como manipular arquivos,
fazer c�lculos e fazer consultas na internet em dicion�rios e tradutores, bem
como cota��es, dicas-l, freshmeat, detran, imposto de renda, cep, etc.

%install
install -d    %{buildroot}%{_bindir}
cp %{_sourcedir}/{funcoeszz,zzwrapper} %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
grep '^zz.*()' funcoeszz | sed 's,(),,g' | xargs -n1 ln -s zzwrapper
popd

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root,0755)
%{_bindir}/funcoeszz
%{_bindir}/zz*
