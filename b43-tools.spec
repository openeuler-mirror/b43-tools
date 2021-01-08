Name:           b43-tools
Version:        019
Release:        5
Summary:        Tools for the Broadcom 43xx series WLAN chip
License:        GPLv2 and GPLv2+ and GPLv3 and BSD-2-Clause and Public Domain
URL:            https://bues.ch/cgit/b43-tools.git
Source0:        https://bues.ch/cgit/b43-tools.git/snapshot/b43-tools-b43-fwcutter-019.tar.xz
BuildRequires:  bison flex flex-static python3-devel
Patch0001:      0001-b43-tools-fix-format-security-errors.patch
Patch0002:      0002-Explicitly-use-python3.patch

%description
Tools for the Broadcom 43xx series WLAN chip.

%prep
%autosetup -n b43-tools-b43-fwcutter-019 -p1
install -p -m 0644 assembler/COPYING COPYING.assembler
install -p -m 0644 assembler/README README.assembler
install -p -m 0644 debug/COPYING COPYING.debug
install -p -m 0644 debug/README README.debug
install -p -m 0644 disassembler/COPYING COPYING.disassembler
install -p -m 0644 ssb_sprom/README README.ssb_sprom
install -p -m 0644 ssb_sprom/COPYING COPYING.ssb_sprom
install -p -m 0644 debug/install.py debug/setup.py

2to3 -w .

%build
CFLAGS="%{optflags}" %make_build -C assembler
CFLAGS="%{optflags}" %make_build -C disassembler
CFLAGS="%{optflags}" %make_build -C ssb_sprom
cd debug
%py3_build

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 assembler/b43-asm %{buildroot}%{_bindir}
install -p -m 0755 assembler/b43-asm.bin %{buildroot}%{_bindir}
install -p -m 0755 disassembler/b43-dasm %{buildroot}%{_bindir}
install -p -m 0755 disassembler/b43-ivaldump %{buildroot}%{_bindir}
install -p -m 0755 disassembler/brcm80211-fwconv %{buildroot}%{_bindir}
install -p -m 0755 disassembler/brcm80211-ivaldump %{buildroot}%{_bindir}
install -p -m 0755 ssb_sprom/ssb-sprom %{buildroot}%{_bindir}
cd debug
%py3_install

%files
%doc README.* COPYING.*
%{_bindir}/*
%{python3_sitelib}/*

%changelog
* Tue Jan 5 2021 Ge Wang<wangge20@huawei.com> - 019-5
- Modify license information

* Tue Oct 27 2020 leiju<leiju4@huawei.com> - 019-4
- Modify BuildRequires from python2-devel to python3-devel

* Thu Jan 16 2020 sunguoshuai<sunguoshuai@huawei.com> - 019-3
- Change tar packages.

* Thu Nov 28 2019 zoushuangshuang<zoushuangshuang@huawei.com> - 019-2
- Package init
