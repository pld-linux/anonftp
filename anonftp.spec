Summary: A program which enables anonymous FTP access.
Name: anonftp
Version: 2.8
Release: 1
Copyright: GPL
Group: System Environment/Daemons
Prefix: /home/ftp
BuildRoot: /var/tmp/anonftp-root
AutoReqProv: 0
Requires: ftpserver

%description
The anonftp package contains the files you need in order to
allow anonymous FTP access to your machine. Anonymous FTP access allows
anyone to download files from your machine without having a user account. 
Anonymous FTP is a popular way of making programs available via the
Internet.

You should install anonftp if you would like to enable anonymous FTP
downloads from your machine.

%prep
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/home/ftp
mkdir -p $RPM_BUILD_ROOT/home/ftp/pub
mkdir -p $RPM_BUILD_ROOT/home/ftp/etc
mkdir -p $RPM_BUILD_ROOT/home/ftp/bin
mkdir -p $RPM_BUILD_ROOT/home/ftp/lib

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

%define LDSOVER 2
%define LIBCVER 2.1.1
%define LIBNSSVER 2

%ifarch i386 sparc armv4l
%define LIBCSOVER 6
%define LIBNSLVER 1
%endif

%ifarch alpha
%define LIBCSOVER 6.1
%define LIBNSLVER 1.1
%endif

%define ROOT $RPM_BUILD_ROOT/home/ftp/lib

cp -fd /etc/ld.so.cache $RPM_BUILD_ROOT/home/ftp/etc
cp -fd /lib/libc.so.%{LIBCSOVER} /lib/libc-%{LIBCVER}.so %{ROOT}
cp -fd /lib/ld-linux.so.%{LDSOVER} /lib/ld-%{LIBCVER}.so %{ROOT}
cp -fd /lib/libnss_files-%{LIBCVER}.so \
	/lib/libnss_files.so.%{LIBNSSVER}	%{ROOT}
cp -fd /lib/libnsl-%{LIBCVER}.so /lib/libnsl.so.%{LIBNSLVER} %{ROOT}

%ifnarch armv4l
cp -fd	/lib/libnss1_files-%{LIBCVER}.so %{ROOT}
%endif

cp -fd /bin/ls /bin/cpio /bin/gzip /bin/tar $RPM_BUILD_ROOT/home/ftp/bin
cp -fd /bin/ash $RPM_BUILD_ROOT/home/ftp/bin/sh
ln -sf gzip $RPM_BUILD_ROOT/home/ftp/bin/zcat
cp -fd /usr/bin/compress $RPM_BUILD_ROOT/home/ftp/bin

strip $RPM_BUILD_ROOT/home/ftp/lib/*
cd $RPM_BUILD_ROOT/home/ftp/bin/
strip ls cpio gzip tar 
cd -

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%attr(0444,root,root) %config /home/ftp/etc/passwd
%attr(0444,root,root) %config /home/ftp/etc/group

/home/ftp/etc/ld.so.cache
/home/ftp/lib/libc.so.%{LIBCSOVER}
/home/ftp/lib/libc-%{LIBCVER}.so
/home/ftp/lib/ld-linux.so.%{LDSOVER}
/home/ftp/lib/ld-%{LIBCVER}.so
/home/ftp/lib/libnss_files-%{LIBCVER}.so
/home/ftp/lib/libnss_files.so.%{LIBNSSVER}
/home/ftp/lib/libnsl-%{LIBCVER}.so
/home/ftp/lib/libnsl.so.%{LIBNSLVER}

%attr(0755,root,root) %dir /home/ftp
%attr(0111,root,root) %dir /home/ftp/bin
%attr(0111,root,root) %dir /home/ftp/etc
%attr(2755,root,ftp) %dir /home/ftp/pub
%dir /home/ftp/lib
%attr(0111,root,root) /home/ftp/bin/ls
%attr(0111,root,root) /home/ftp/bin/compress
%attr(0111,root,root) /home/ftp/bin/cpio
%attr(0111,root,root) /home/ftp/bin/gzip
%attr(0111,root,root) /home/ftp/bin/sh
%attr(0111,root,root) /home/ftp/bin/tar
%attr(0111,root,root) /home/ftp/bin/zcat
