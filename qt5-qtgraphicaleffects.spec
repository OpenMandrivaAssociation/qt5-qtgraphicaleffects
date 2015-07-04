%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta

%define debug_package %nil

%define qttarballdir qtgraphicaleffects-opensource-src-%{version}%{?beta:-%{beta}}

Name:		qt5-qtgraphicaleffects
Version:	5.5.0
%if 0%{?beta:1}
Release:	1.%{beta}.1
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version} |cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version} |cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt-project.org
BuildRequires:	qt5-qtbase-devel = %{version}


%description
Qt GUI toolkit

%files
%_qt5_libdir/qt%{api}/qml/QtGraphicalEffects/

#------------------------------------------------------------------------------

%prep
%setup -q -n %qttarballdir

%build
%qmake_qt5

%make
#------------------------------------------------------------------------------

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}
