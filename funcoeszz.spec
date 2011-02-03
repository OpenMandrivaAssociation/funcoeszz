Name: funcoeszz
Version: 10.12	
Release: 1
Summary: Handy bash functions called zz*
Summary(pt_BR): Funções úteis em bash chamadas zz*
Group: Text tools
Group(pt_BR): Ferramentas de texto
License: GPL
URL: http://funcoeszz.net/
Source0: http://funcoeszz.net/funcoeszz
Source1: zzwrapper
Patch0: funcoeszz-10.12-zzsenha-more-chars.patch
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Handy bash functions called zz*, to deal with files, internet dictionary
queries, freshmeat, and others.
    
%description -l pt_BR
Funções úteis em bash de aplicações diversificadas como manipular arquivos,
fazer cálculos e fazer consultas na internet em dicionários e tradutores,
bem como cotações, dicas-l, freshmeat, detran, imposto de renda, cep, etc.

%prep
if [ -d %{name}-%{version} ]; then
	rm -rf %{name}-%{version}
fi
install -d %{name}-%{version}
cp %{_sourcedir}/{funcoeszz,zzwrapper} %{name}-%{version}/
cd %{name}-%{version}/
%patch0 -p1

%install
cd %{name}-%{version}
install -d %{buildroot}%{_bindir}
cp funcoeszz zzwrapper %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
grep '^zz.*()' funcoeszz | sed 's,(),,g' | xargs -n1 ln -s zzwrapper
popd

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root,0755)
%{_bindir}/funcoeszz
%{_bindir}/zz*
