%define oname   id-generator
%define  _root   /opt/%{oname}
Name:       id-generator
Version:    0.1.4
Release:    1%{?dist}
Summary:    id generator

Group:      Development/Tools
License:    GPLv2
URL:        https://github.com/detailyang/id-generator
Source0:    id-generator-%{version}.tar.gz
Source1:    id-generator.init
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  zlib-devel
Requires:   zlib

%description
id-generator is a id generator for distributed environment

%prep
%setup -q -n %{oname}-%{version}

%build
make

%install
rm -rf %{buildroot}
make PREFIX=%{buildroot}%{_root} install
mkdir -p %{buildroot}/data/%{oname}
mkdir -p %{buildroot}/etc/init.d
install -m 0755 %{SOURCE1} %{buildroot}/etc/init.d/id-generatord

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_root}
/data/%{oname}
/etc/init.d/id-generator
%doc

%post
if [ $1 -eq 1 ] ; then
    #install
    id idgen 2>/dev/null || useradd -r idgen
    chown -R idgen.idgen /data/id-generator
    chkconfig --add id-generator
    chkconfig id-generator on
elif [ $1 -eq 2 ]; then
    #update
    id idgen 2>/dev/null || useradd -r idgen
    chown -R idgen.idgen /data/id-generator
    chkconfig --add id-generator
    chkconfig id-generator on
fi

%changelog
* Mon Feb 22 2016 detailyang <detailyang@gmail.com> 0.1.4-1
  id-generator init.
