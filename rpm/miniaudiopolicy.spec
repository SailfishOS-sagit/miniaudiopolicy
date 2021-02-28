%define strip /bin/true
%define __requires_exclude  ^.*$
%define __find_requires     %{nil}
%global debug_package       %{nil}
%define __provides_exclude_from ^.*$
%define device_rpm_architecture_string armv7hl
%define _target_cpu %{device_rpm_architecture_string}

Name:     miniaudiopolicy
Summary:  Android Fake MiniAudioPolicy service
Version:  0.1.0
Release:  %(date +'%%Y%%m%%d%%H%%M')
License:  ASL 2.0
Source0:  out/miniaudiopolicyservice

%description
%{summary}

%build
pwd
ls -lh

%install
mkdir -p $RPM_BUILD_ROOT/usr/libexec/droid-hybris/system/etc/init
mkdir -p $RPM_BUILD_ROOT/usr/libexec/droid-hybris/system/bin
cp out/miniaudiopolicyservice $RPM_BUILD_ROOT/usr/libexec/droid-hybris/system/bin/
cp service/miniaudiopolicy.rc $RPM_BUILD_ROOT/usr/libexec/droid-hybris/system/etc/init/

%files
%defattr(-,root,root,-)
/usr/libexec/droid-hybris/system/etc/init/miniaudiopolicy.rc
/usr/libexec/droid-hybris/system/bin/miniaudiopolicyservice
