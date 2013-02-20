%define release_name Tizen Next
%define dist_version 3.0.0

Summary:	Tizen release files
Name:		tizen-release
Version:	3.0.0
Release:	2
License:	GPL-2.0
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

%ifarch  %{ix86}
%define _tarch ia32
%else
%define _tarch %{_arch}
%endif


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


mkdir -p $RPM_BUILD_ROOT/etc/products.d
cat >$RPM_BUILD_ROOT/etc/products.d/tizen.prod << EOF
<?xml version="1.0" encoding="UTF-8"?>
<product schemeversion="0">
  <vendor>Tizen.org</vendor>
  <name>Tizen</name>
  <version>%{version}</version>
  <release>%{release}</release>
  <arch>%{_target_cpu}</arch>
  <productline>Tizen</productline>
  <register>
    <target>tizen-%{version}-%{_target_cpu}</target>
    <release></release>
    <repositories>
    </repositories>
  </register>
  <updaterepokey>000000000</updaterepokey>
  <summary>Tizen</summary>
  <description>Tizen</description>
  <linguas>
    <language>cs</language>
    <language>da</language>
    <language>de</language>
    <language>en</language>
    <language>en_GB</language>
    <language>en_US</language>
    <language>es</language>
    <language>fi</language>
    <language>fr</language>
    <language>hu</language>
    <language>it</language>
    <language>ja</language>
    <language>nb</language>
    <language>nl</language>
    <language>pl</language>
    <language>pt</language>
    <language>pt_BR</language>
    <language>ru</language>
    <language>sv</language>
    <language>zh</language>
    <language>zh_CN</language>
    <language>zh_TW</language>
  </linguas>
  <urls>
    <url name="releasenotes">http://www.tizen.org</url>
    <url name="register">http://www.tizen.org/</url>
    <url name="repository">https://download.tz.otcshare.org/snapshots/trunk/pc/latest/repos/pc/%{_tarch}/packages/</url>
  </urls>
  <buildconfig>
    <producttheme>Tizen</producttheme>
    <betaversion>Milestone 1</betaversion>
  </buildconfig>
  <installconfig>
    <defaultlang>en_US</defaultlang>
    <releasepackage name="tizen-release" flag="EQ" version="3.0.0" release="%{release}" />
    <distribution>Tizen</distribution>
  </installconfig>
  <runtimeconfig />
</product>

EOF

# this is a base product, create symlink
ln -s tizen.prod $RPM_BUILD_ROOT/etc/products.d/baseproduct


%files
%config %attr(0644,root,root) /etc/tizen-release
%config %attr(0644,root,root) /etc/os-release
/etc/system-release
/etc/products.d
