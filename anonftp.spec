Summary:	A program which enables anonymous FTP access.
Name:		anonftp
Version:	2.8
Release:	1
License:	GPL
Group:          Networking/Daemons
Group(pl):      Sieciowe/Serwery
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
AutoReqProv:	0
Requires:	ftpserver

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

%prep
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/ftp/{pub,etc,bin,lib}

cat > $RPM_BUILD_ROOT/home/ftp/etc/passwd <<EOF
root:*:0:0:::
bin:*:1:1:::
operator:*:11:0:::
ftp:*:14:50:::
nobody:*:99:99:::
EOF

cat > $RPM_BUILD_ROOT/home/ftp/etc/group <<EOF
root::0:
bin::1:
daemon::2:
sys::3:
adm::4:
ftp::50:
EOF

install %{_sysconfdir}/ld.so.cache $RPM_BUILD_ROOT/home/ftp/etc
install /lib/{libc-*.so,ld-*.so,libnss_files-*.so,libnsl-*.so} \
	$RPM_BUILD_ROOT/home/ftp/lib

install /bin/{ls,cpio,gzip,tar}			$RPM_BUILD_ROOT/home/ftp/bin
install /bin/ash				$RPM_BUILD_ROOT/home/ftp/bin/sh
install %{_bindir}/compress			$RPM_BUILD_ROOT/home/ftp/bin/compress
ln -sf gzip 					$RPM_BUILD_ROOT/home/ftp/bin/zcat

strip $RPM_BUILD_ROOT/home/ftp/lib/*
strip $RPM_BUILD_ROOT/home/ftp/bin/{ls,cpio,gzip,tar}

%post 
/sbin/ldconfig /home/ftp/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(0755,root,root) %dir /home/ftp
%attr(0111,root,root) %dir /home/ftp/bin
%attr(0111,root,root) %dir /home/ftp/etc
%attr(2755,root,root) %dir /home/ftp/pub
%attr(0755,root,root) %dir /home/ftp/lib
%attr(0444,root,root) %config /home/ftp/etc/passwd
%attr(0444,root,root) %config /home/ftp/etc/group
%attr(0444,root,root) /home/ftp/etc/ld.so.cache
%attr(0111,root,root) /home/ftp/bin/*
%attr(0555,root,root) /home/ftp/lib/*
