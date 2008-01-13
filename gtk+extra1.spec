Summary:	A useful widget set complementary to GTK+
Summary(pl.UTF-8):	Zbiór użytecznych widgetów uzupełniający GTK+
Name:		gtk+extra1
Version:	0.99.17
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://gtkextra.sourceforge.net/src/gtk+extra-%{version}.tar.gz
# Source0-md5:	390e622c12a5c7f7845ee144ae13ab93
Patch0:		gtk+extra-ac_am.patch
URL:		http://gtkextra.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1:1.2.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk+extra is a useful widget set complementary to GTK+ for creating
graphical interfaces for the X11 Window System. It is written in C and
requires GTK+ version 1.2.x.

%description -l pl.UTF-8
gtk+extra jest zbiorem pożytecznych widgetów uzupełniających GTK+,
służących do tworzenia graficznych interfejsów w systemie X11 Window.
Został napisany w C i wymaga biblioteki GTK+ w wersji 1.2.x.

%package devel
Summary:	Header files for gtk+extra library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gtk+extra
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+-devel >= 1:1.2.0

%description devel
Header files for gtk+extra library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtk+extra.

%package static
Summary:	Static gtk+extra libraries
Summary(pl.UTF-8):	Biblioteki statyczne gtk+extra
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtk+extra libraries.

%description static -l pl.UTF-8
Biblioteki statyczne gtk+extra.

%prep
%setup -q -n gtk+extra-%{version}
%patch0 -p1

# just libtool macros
rm -f acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO docs/gtk*
%attr(755,root,root) %{_libdir}/libgtkextra-0.99.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkextra-0.99.so.17

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtkextra-config
%attr(755,root,root) %{_libdir}/libgtkextra.so
%{_libdir}/libgtkextra.la
%{_includedir}/gtkextra
%{_aclocaldir}/gtkextra.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkextra.a
