Summary:	A program which enables anonymous FTP access.
Summary(pl):	Program, który pozwala na anonimowy dostêp do FTP'a.
Summary(ja):	Anonymous FTP ¤ò²ÄÇ½¤Ë¤¹¤ë¥×¥í¥°¥é¥à
Summary(pt_BR):	Habilita acesso via ftp anônimo
Summary(es):	Habilita acceso vía ftp anónimo
Name:		anonftp
Version:	2.8
Release:	1
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
AutoReqProv:	0
BuildRequires:	/bin/ash
Requires:	ftpserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The anonftp package contains the files you need in order to allow
anonymous FTP access to your machine. Anonymous FTP access allows
anyone to download files from your machine without having a user
account. Anonymous FTP is a popular way of making programs available
via the Internet.

You should install anonftp if you would like to enable anonymous FTP
downloads from your machine.

%description -l pl
pakiet anonftp zawiera pliki niezbêdne w celu uruchomienia serwera
anonimowego FTP na danej maszynie. Dostêp przez anonimowy FTP pozwala
ka¿demu pobieraæ pliki z danego komputera bez potzreby posiadania
konta u¿ytkownika. Anonimowe FTP jest popularnym sposbem udostepniania
plików w Internecie.

%description -l ja
anonftp¥Ñ¥Ã¥±¡¼¥¸¤Ï anonymous FTP ¤ò¸ø³«¤¹¤ë¤¿¤á¤ËÉ¬Í×¤Ê´Ä¶­¤òÄó¶¡¤·¤Þ¤¹¡£
anonymous FTP ¤òÍøÍÑ¤¹¤ì¤Ð¡¢¥æ¡¼¥¶¥¢¥«¥¦¥ó¥È¤Ê¤·¤Ç¤âFTP¤Ø¤Î¥¢¥¯¥»¥¹¤¬²ÄÇ½
¤Ë¤Ê¤ê¤Þ¤¹¡£

%description -l pt_BR
Contém os arquivos necessários para permitir acesso ftp anônimo
a sua máquina.  Isso deixa qualquer usuário pegar arquivos de
sua máquina sem ter uma conta, o que é um meio popular de tornar
programas disponíveis na Internet.

%description -l es
Contiene los archivos necesarios para permitir acceso ftp anónimo
a tu máquina. Esto deja cualquier usuario coger archivos de tu
máquina sin tener una cuenta, esto es un medio popular de poner a
disposición programas en Internet.

%prep
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/ftp/{pub,etc,bin,lib}

cat > $RPM_BUILD_ROOT/home/ftp%{_sysconfdir}/passwd <<EOF
root:*:0:0:::
bin:*:1:1:::
operator:*:11:0:::
ftp:*:14:50:::
nobody:*:99:99:::
EOF

cat > $RPM_BUILD_ROOT/home/ftp%{_sysconfdir}/group <<EOF
root::0:
bin::1:
daemon::2:
sys::3:
adm::4:
ftp::50:
EOF

install %{_sysconfdir}/ld.so.cache $RPM_BUILD_ROOT/home/ftp%{_sysconfdir}
install /lib/{libc-*.so,ld-*.so,libnss_files-*.so,libnsl-*.so} \
	$RPM_BUILD_ROOT/home/ftp/lib

install /bin/{ls,cpio,gzip,tar}			$RPM_BUILD_ROOT/home/ftp/bin
install /bin/ash				$RPM_BUILD_ROOT/home/ftp/bin/sh
install %{_bindir}/compress			$RPM_BUILD_ROOT/home/ftp/bin/compress
ln -sf gzip 					$RPM_BUILD_ROOT/home/ftp/bin/zcat

%post 
/sbin/ldconfig /home/ftp/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(0755,root,root) %dir /home/ftp
%attr(0111,root,root) %dir /home/ftp/bin
%attr(0111,root,root) %dir /home/ftp%{_sysconfdir}
%attr(2755,root,root) %dir /home/ftp/pub
%attr(0755,root,root) %dir /home/ftp/lib
%attr(0444,root,root) %config /home/ftp%{_sysconfdir}/passwd
%attr(0444,root,root) %config /home/ftp%{_sysconfdir}/group
%attr(0444,root,root) /home/ftp%{_sysconfdir}/ld.so.cache
%attr(0111,root,root) /home/ftp/bin/*
%attr(0555,root,root) /home/ftp/lib/*
