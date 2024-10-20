%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta %{nil}

Name:		qt5-qtgraphicaleffects
Version:	5.15.15
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtgraphicaleffects-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtgraphicaleffects-everywhere-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
# From KDE
# [currently no patches required]
Summary:	Qt Graphical Effects toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		https://www.qt.io
BuildRequires:	qmake5 >= %{version}
BuildRequires:	qt5-qtquick-private-devel >= %{version}
BuildRequires:	qt5-qtqml-private-devel >= %{version}
BuildRequires:	pkgconfig(Qt5Core) >= %{version}
BuildRequires:	pkgconfig(Qt5Gui) >= %{version}
BuildRequires:	pkgconfig(Qt5Qml) >= %{version}
BuildRequires:	pkgconfig(Qt5Quick) >= %{version}
BuildRequires:	pkgconfig(Qt5Test) >= %{version}
BuildRequires:	qt5-qtqmlmodels-private-devel
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1

%description
Qt Graphical effects toolkit.

%files
%{_qt5_libdir}/qt%{api}/qml/QtGraphicalEffects/

#------------------------------------------------------------------------------

%prep
%autosetup -n %(echo %qttarballdir|sed -e 's,-opensource,,') -p1
%{_libdir}/qt5/bin/syncqt.pl -version %{version}

%build
%qmake_qt5

%make_build
#------------------------------------------------------------------------------

%install
%make_install INSTALL_ROOT=%{buildroot}
