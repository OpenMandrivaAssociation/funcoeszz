Name: funcoeszz
Version: 10.12	
Release: %mkrel 0.1
Summary: Handy bash functions called zz*
Summary(pt_BR): Funções úteis em bash chamadas zz*
Group: Text tools
Group(pt_BR): Ferramentas de texto
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
Funções úteis em bash de aplicações diversificadas como manipular arquivos,
fazer cálculos e fazer consultas na internet em dicionários e tradutores,
bem como cotações, dicas-l, freshmeat, detran, imposto de renda, cep, etc.

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


%changelog
* Mon Dec 27 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 10.12-0.1mdv2011.0
+ Revision: 625369
- new version 10.12, 43 new commands!

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 8.7-3mdv2011.0
+ Revision: 618370
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 8.7-2mdv2010.0
+ Revision: 428966
- rebuild

* Thu Sep 04 2008 Bogdano Arendartchuk <bogdano@mandriva.com> 8.7-1mdv2009.0
+ Revision: 280861
- new version 8.7
- use symlinks for zz* commands so that it will not pollute the shell
  environment
- import funcoeszz


* Fri May 21 2004 Aurelio Marinho Jargas <aurelio@conectiva.com.br>
+ 2004-05-21 10:20:13 (61042)
- New upstream release: 4.0518

* Fri Nov 07 2003 Aurelio Marinho Jargas <aurelio@conectiva.com.br>
+ 2003-11-07 18:00:04 (39137)
- New upstream release: 3.1002

* Thu Aug 14 2003 Antonio Edison Vieira J�nior <antoniojr@conectiva.com.br>
+ 2003-08-14 12:02:25 (34183)
- New upstream release: 3.0713

* Thu Apr 10 2003 Antonio Edison Vieira J�nior <antoniojr@conectiva.com.br>
+ 2003-04-10 14:48:21 (29685)
- New upstream release: 3.0403

* Fri Oct 18 2002 jason
+ 2002-10-18 15:33:34 (17869)
- New upstream release

* Tue Sep 03 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-09-03 14:36:41 (11541)
- Imported package from snapshot.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 17:40:28 (7812)
- Imported package from 8.0.
