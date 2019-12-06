Summary: Config to enable the repository for the Messaging SIG
Name:    centos-release-messaging
Version: 1
Release: 1%{?dist}
License: GPL
URL: http://wiki.centos.org/SpecialInterestGroup/Messaging
Source0: CentOS-Messaging.repo
Source1: RPM-GPG-KEY-CentOS-SIG-Messaging

BuildArch: noarch

Requires: centos-release

%description
yum configs for the CentOS Messaging SIG.

%prep

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-OpsTools.repo
install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-Messaging

%changelog
* Fri Dec 06 2019 Matthias Runge <mrunge@redhat.com> - 1.1
- Initial release
