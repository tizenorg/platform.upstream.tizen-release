%define tizen_version_major 3
%define tizen_version_minor 0
%define tizen_version_patch 0

%define tizen_version %{tizen_version_major}.%{tizen_version_minor}
%define tizen_full_version %{tizen_version}.%{tizen_version_patch}
%define vendor tizen

Name:           tizen-release
Version:        %{tizen_full_version}
Release:        0
License:        GPL-2.0
Summary:        Tizen release files
Url:            http://www.tizen.com
Group:          System/Base
Provides:       system-release = %{version}
Provides:       tizen-release = %{version}
Provides:       product()
Provides:       product(Tizen) = %{version}

#HACK
Provides:       lsb = 4.1

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

install -d %{buildroot}/etc
cat > %{buildroot}%{_sysconfdir}/tizen-release <<EOF
%{release_name} %{tizen_full_version} (%{_arch})
VERSION = %{tizen_full_version}
CODENAME = Next
EOF

ln -s tizen-release %{buildroot}%{_sysconfdir}/system-release

cat > %{buildroot}%{_sysconfdir}/os-release <<EOF
NAME=Tizen
VERSION="%{tizen_full_version} (%{release_name})"
ID=tizen
VERSION_ID=%{tizen_full_version}
PRETTY_NAME="Tizen %{tizen_full_version} (%{release_name})"
ANSI_COLOR="0;36"
CPE_NAME="cpe:/o:tizen:tizen:%{tizen_full_version}"
EOF

mkdir -p %{buildroot}%{_sysconfdir}/products.d
cat >%{buildroot}%{_sysconfdir}/products.d/tizen.prod << EOF
<?xml version="1.0" encoding="UTF-8"?>
<product schemeversion="0">
  <vendor>Tizen.org</vendor>
  <name>Tizen</name>
  <version>%{tizen_full_version}</version>
  <release>%{release_name}</release>
  <arch>%{_target_cpu}</arch>
  <productline>Tizen</productline>
  <register>
    <target>tizen-%{tizen_full_version}-%{_target_cpu}</target>
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
    <url name="repository">https://download.tizen.org/snapshots/tizen/%{profile}/latest/repos/%{_repository}/packages/%{_tarch}/</url>
  </urls>
  <buildconfig>
    <producttheme>Tizen</producttheme>
    <betaversion></betaversion>
  </buildconfig>
  <installconfig>
    <defaultlang>en_US</defaultlang>
    <releasepackage name="tizen-release" flag="EQ" version="%{tizen_full_version}" release="%{release}" />
    <distribution>Tizen</distribution>
  </installconfig>
  <runtimeconfig />
</product>

EOF

# this is a base product, create symlink
ln -s tizen.prod %{buildroot}%{_sysconfdir}/products.d/baseproduct


# generate tizen-build.conf


cat > %{buildroot}%{_sysconfdir}/tizen-build.conf <<'EOF'
TZ_BUILD_RELEASE_NAME="%{release_name}"
TZ_BUILD_VERSION=%{tizen_version}
TZ_BUILD_FULLVER=%{tizen_full_version}

TZ_BUILD_PROFILE=%{profile}
TZ_BUILD_PROJECT=%{_project}
TZ_BUILD_VENDOR=%{vendor}
TZ_BUILD_REPO=%{_repository}
TZ_BUILD_ARCH=%{_arch}

TZ_BUILD_ID=@BUILD_ID@
TZ_BUILD_DATE=@BUILD_DATE@
TZ_BUILD_TIME=@BUILD_TIME@
TZ_BUILD_TS=@BUILD_TS@

TZ_BUILD_URL=http://download.tizen.org
TZ_BUILD_SNAPSHOT_URL=${TZ_BUILD_URL}/snapshots/tizen/%{profile}/
TZ_BUILD_DAILY_URL=${TZ_BUILD_URL}/releases/daily/tizen/%{profile}/
TZ_BUILD_WEEKLY_URL=${TZ_BUILD_URL}/releases/weekly/tizen/%{profile}/
TZ_BUILD_MILESTONE_URL=${TZ_BUILD_URL}/releases/milestone/tizen/%{profile}/

TZ_BUILD_WITH_MESA=%{?_with_mesa}
TZ_BUILD_WITH_WAYLAND=%{?_with_wayland}
TZ_BUILD_WITH_RDP=%{?_with_rdp}
TZ_BUILD_WITH_X=%{?_with_x}
TZ_BUILD_WITH_EMULATOR=%{?_with_emulator}

EOF

%files
%config %attr(0644,root,root) %{_sysconfdir}/tizen-release
%config %attr(0644,root,root) %{_sysconfdir}/os-release
%config %attr(0444,root,root) %{_sysconfdir}/tizen-build.conf
%{_sysconfdir}/system-release
%{_sysconfdir}/products.d

