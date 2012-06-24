Summary:	A program which enables anonymous FTP access.
Summary(pl):	Program, kt�ry pozwala na anonimowy dost�p do FTP'a.
Summary(ja):	Anonymous FTP ���ǽ�ˤ���ץ����
Summary(pt_BR):	Habilita acesso via ftp an�nimo
Summary(es):	Habilita acceso v�a ftp an�nimo
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
pakiet anonftp zawiera pliki niezb�dne w celu uruchomienia serwera
anonimowego FTP na danej maszynie. Dost�p przez anonimowy FTP pozwala
ka�demu pobiera� pliki z danego komputera bez potzreby posiadania
konta u�ytkownika. Anonimowe FTP jest popularnym sposbem udostepniania
plik�w w Internecie.

%description -l ja
anonftp�ѥå������� anonymous FTP ��������뤿���ɬ�פʴĶ����󶡤��ޤ���
anonymous FTP �����Ѥ���С��桼����������Ȥʤ��Ǥ�FTP�ؤΥ�����������ǽ
�ˤʤ�ޤ���

%description -l pt_BR
Cont�m os arquivos necess�rios para permitir acesso ftp an�nimo
a sua m�quina.  Isso deixa qualquer usu�rio pegar arquivos de
sua m�quina sem ter uma conta, o que � um meio popular de tornar
programas dispon�veis na Internet.

%description -l es
Contiene los archivos necesarios para permitir acceso ftp an�nimo
a tu m�quina. Esto deja cualquier usuario coger archivos de tu
m�quina sin tener una cuenta, esto es un medio popular de poner a
disposici�n programas en Internet.

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
