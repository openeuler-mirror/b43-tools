Name:           b43-tools
Version:        019
Release:        2
Summary:        Tools for the Broadcom 43xx series WLAN chip
License:        GPLv2 and GPLv2+ and GPLv3
URL:            https://bues.ch/cgit/b43-tools.git
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  bison flex flex-static python2-devel

Patch0001:      0001-b43-tools-fix-format-security-errors.patch


%description
Tools for the Broadcom 43xx series WLAN chip.


%prep
%autosetup -n %{name}-%{version} -p1
install -p -m 0644 assembler/COPYING COPYING.assembler
install -p -m 0644 assembler/README README.assembler
install -p -m 0644 debug/COPYING COPYING.debug
install -p -m 0644 debug/README README.debug
install -p -m 0644 disassembler/COPYING COPYING.disassembler
install -p -m 0644 ssb_sprom/README README.ssb_sprom
install -p -m 0644 ssb_sprom/COPYING COPYING.ssb_sprom
install -p -m 0644 debug/install.py debug/setup.py


%build
CFLAGS="%{optflags}" %make_build -C assembler
CFLAGS="%{optflags}" %make_build -C disassembler
CFLAGS="%{optflags}" %make_build -C ssb_sprom
cd debug
%py2_build


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
%py2_install


%files
%doc README.* COPYING.*
%{_bindir}/*
%{python2_sitelib}/*


%changelog
* Thu Nov 28 2019 zoushuangshuang<zoushuangshuang@huawei.com> - 019-2
- Package init
