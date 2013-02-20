%define release_name Tizen Next
%define dist_version 3.0.0

Summary:	Tizen release files
Name:		tizen-release
Version:	3.0.0
Release:	1
License:	GPLv2
Group:		System/Base
URL:		http://www.tizen.com
Provides:	system-release = %{version}-%{release}
Provides:	tizen-release = %{version}-%{release}

#HACK
Provides:   lsb = 4.1

%description
Tizen release files such as various /etc/ files that define the release.

%prep

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/etc
cat > %{buildroot}/etc/tizen-release <<EOF
Tizen %{dist_version} (%{_arch})
VERSION = %{version}
CODENAME = Next
EOF

ln -s tizen-release %{buildroot}/etc/system-release

cat > %{buildroot}/etc/os-release <<EOF
NAME=Tizen
VERSION="%{dist_version} (%{release_name})"
ID=tizen
VERSION_ID=%{dist_version}
PRETTY_NAME="Tizen %{dist_version} (%{release_name})"
ANSI_COLOR="0;36"
CPE_NAME="cpe:/o:tizen:tizen:%{dist_version}"
EOF

%files
%config %attr(0644,root,root) /etc/tizen-release
%config %attr(0644,root,root) /etc/os-release
/etc/system-release
