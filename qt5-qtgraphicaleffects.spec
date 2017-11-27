%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta rc1

%define debug_package %nil

Name:		qt5-qtgraphicaleffects
Version:	5.10.0
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtgraphicaleffects-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%(echo %{beta} |sed -e "s,1$,,")/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtgraphicaleffects-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io
BuildRequires:	qmake5 >= %{version}
BuildRequires:	qt5-qtquick-private-devel >= %{version}
BuildRequires:	qt5-qtqml-private-devel >= %{version}
BuildRequires:	pkgconfig(Qt5Core) >= %{version}
BuildRequires:	pkgconfig(Qt5Gui) >= %{version}
BuildRequires:	pkgconfig(Qt5Qml) >= %{version}
BuildRequires:	pkgconfig(Qt5Quick) >= %{version}
BuildRequires:	pkgconfig(Qt5Test) >= %{version}

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
