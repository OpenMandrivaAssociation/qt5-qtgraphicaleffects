%define api 5
%define major %api

%define qtminor 4
%define qtsubminor 0

%define qtversion %{api}.%{qtminor}.%{qtsubminor}
%define debug_package %nil

%define qttarballdir qtgraphicaleffects-opensource-src-%{qtversion}

Name:		qt5-qtgraphicaleffects
Version:	%{qtversion}
Release:	1
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt-project.org
Source0:	http://download.qt-project.org/official_releases/qt/%{api}.%{qtminor}/%{version}/submodules/%{qttarballdir}.tar.xz
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
