#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mdadm
Version  : 4.0
Release  : 3
URL      : https://www.kernel.org/pub/linux/utils/raid/mdadm/mdadm-4.0.tar.xz
Source0  : https://www.kernel.org/pub/linux/utils/raid/mdadm/mdadm-4.0.tar.xz
Summary  : mdadm is used for controlling Linux md devices (aka RAID arrays)
Group    : Development/Tools
License  : GPL-2.0
Requires: mdadm-bin
Requires: mdadm-doc

%description
mdadm is a program that can be used to create, manage, and monitor
Linux MD (Software RAID) devices.

%package bin
Summary: bin components for the mdadm package.
Group: Binaries

%description bin
bin components for the mdadm package.


%package doc
Summary: doc components for the mdadm package.
Group: Documentation

%description doc
doc components for the mdadm package.


%prep
%setup -q -n mdadm-4.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489069397
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1489069397
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/lib/udev/rules.d/63-md-raid-arrays.rules
/lib/udev/rules.d/64-md-raid-assembly.rules

%files bin
%defattr(-,root,root,-)
/usr/bin/mdadm
/usr/bin/mdmon

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man4/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*
