Summary:	A program which enables anonymous FTP access
Summary(pl.UTF-8):   Program, który pozwala na anonimowy dostęp do FTP-a
Summary(ja.UTF-8):   Anonymous FTP を可能にするプログラム
Summary(pt_BR.UTF-8):   Habilita acesso via FTP anônimo
Summary(es.UTF-8):   Habilita acceso vía FTP anónimo
Name:		anonftp
Version:	2.8
Release:	2
License:	GPL
Group:		Networking/Daemons
BuildRequires:	/bin/ash
BuildRequires:	/bin/cpio
BuildRequires:	fhs-compliance
Requires:	ftpserver
AutoReqProv:	no
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The anonftp package contains the files you need in order to allow
anonymous FTP access to your machine. Anonymous FTP access allows
anyone to download files from your machine without having a user
account. Anonymous FTP is a popular way of making programs available
via the Internet.

You should install anonftp if you would like to enable anonymous FTP
downloads from your machine.

%description -l pl.UTF-8
pakiet anonftp zawiera pliki niezbędne w celu uruchomienia serwera
anonimowego FTP na danej maszynie. Dostęp przez anonimowy FTP pozwala
każdemu pobierać pliki z danego komputera bez potrzeby posiadania
konta użytkownika. Anonimowe FTP jest popularnym sposobem udostępniania
plików w Internecie.

%description -l ja.UTF-8
anonftpパッケージは anonymous FTP を公開するために必要な環境を提供します。
anonymous FTP を利用すれば、ユーザアカウントなしでもFTPへのアクセスが可能
になります。

%description -l pt_BR.UTF-8
Contém os arquivos necessários para permitir acesso FTP anônimo a sua
máquina. Isso deixa qualquer usuário pegar arquivos de sua máquina sem
ter uma conta, o que é um meio popular de tornar programas disponíveis
na Internet.

%description -l es.UTF-8
Contiene los archivos necesarios para permitir acceso FTP anónimo a tu
máquina. Esto deja cualquier usuario coger archivos de tu máquina sin
tener una cuenta, esto es un medio popular de poner a disposición
programas en Internet.

%prep
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/srv/ftp/{pub,etc,bin,lib}

cat > $RPM_BUILD_ROOT/srv/ftp%{_sysconfdir}/passwd <<EOF
root:*:0:0:::
bin:*:1:1:::
operator:*:11:0:::
ftp:*:14:50:::
nobody:*:99:99:::
EOF

cat > $RPM_BUILD_ROOT/srv/ftp%{_sysconfdir}/group <<EOF
root::0:
bin::1:
daemon::2:
sys::3:
adm::4:
ftp::50:
EOF

install %{_sysconfdir}/ld.so.cache $RPM_BUILD_ROOT/srv/ftp%{_sysconfdir}
install /lib/{libc-*.so,ld-*.so,libnss_files-*.so,libnsl-*.so} \
	$RPM_BUILD_ROOT/srv/ftp/lib

install /bin/{ls,cpio,gzip,tar}			$RPM_BUILD_ROOT/srv/ftp/bin
install /bin/ash				$RPM_BUILD_ROOT/srv/ftp/bin/sh
install %{_bindir}/compress			$RPM_BUILD_ROOT/srv/ftp/bin/compress
ln -sf gzip 					$RPM_BUILD_ROOT/srv/ftp/bin/zcat

%post
/sbin/ldconfig /srv/ftp/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(0755,root,root) %dir /srv/ftp
%attr(0111,root,root) %dir /srv/ftp/bin
%attr(0111,root,root) %dir /srv/ftp%{_sysconfdir}
%attr(2755,root,root) %dir /srv/ftp/pub
%attr(0755,root,root) %dir /srv/ftp/lib
%attr(0444,root,root) %config /srv/ftp%{_sysconfdir}/passwd
%attr(0444,root,root) %config /srv/ftp%{_sysconfdir}/group
%attr(0444,root,root) /srv/ftp%{_sysconfdir}/ld.so.cache
%attr(0111,root,root) /srv/ftp/bin/*
%attr(0555,root,root) /srv/ftp/lib/*
