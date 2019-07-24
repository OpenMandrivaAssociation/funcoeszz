Summary:	Handy bash functions called zz*
Name:		funcoeszz
Version:	15.5
Release:	1
License:	GPLv2+
Group:		Text tools
Url:		http://funcoeszz.net/
Source0:	http://funcoeszz.net/funcoeszz
Source1:	zzwrapper
Requires:	lynx
BuildArch:	noarch

%description
Handy bash functions called zz*, to deal with files, internet dictionary
queries, freshmeat, and others.

%files
%{_bindir}/funcoeszz
%{_bindir}/zz*

#----------------------------------------------------------------------------

%prep

%build

%install
install -d %{buildroot}%{_bindir}
install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/funcoeszz
install -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/zzwrapper
pushd %{buildroot}%{_bindir}
grep '^zz.*()' funcoeszz | sed 's,(),,g' | xargs -n1 ln -s zzwrapper
popd
