%define name python-jenkins
%define version 0.4.13.dev1
%define unmangled_version %{version}
%define release 3%{?dist}

Summary: UNKNOWN
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: OpenStack <openstack@lists.launchpad.net>
Url: http://git.openstack.org/cgit/stackforge/python-jenkins
Requires: python-six
Requires: python-pbr >= 0.8.2
BuildRequires: python
BuildRequires: python-setuptools

Requires: python-multi_key_dict

%description
Python bindings for the remote Jenkins API

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
