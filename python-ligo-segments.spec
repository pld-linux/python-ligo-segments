#
# Conditional build:
%bcond_without	python2		# CPython 2.x module
%bcond_without	python3		# CPython 3.x module
%bcond_with	py2_tests	# python2 based testing (requires no longer supported lal module)
%bcond_without	py3_tests	# python3 based testing

Summary:	Representations of semi-open intervals
Summary(pl.UTF-8):	Reprezentacja przedziałów jednostronnie otwartych
Name:		python-ligo-segments
Version:	1.4.0
Release:	1
License:	GPL v3+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ligo-segments/
Source0:	https://files.pythonhosted.org/packages/source/l/ligo-segments/ligo-segments-%{version}.tar.gz
# Source0-md5:	ca0627db1385379ae1652f09826ea7c0
Patch0:		ligo-segments-setuptools.patch
URL:		https://pypi.org/project/ligo-segments/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with py2_tests}
BuildRequires:	python-lal
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with py3_tests}
BuildRequires:	python3-lal
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Defines the segment, segmentlist, and segmentlistdict objects for
manipulating semi-open intervals.

%description -l pl.UTF-8
Moduł definiuje obiekty segment, segmentlist i segmentlistdict do
operacji na przedziałach jednostronnie otwartych.

%package -n python3-ligo-segments
Summary:	Representations of semi-open intervals
Summary(pl.UTF-8):	Reprezentacja przedziałów jednostronnie otwartych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-ligo-segments
Defines the segment, segmentlist, and segmentlistdict objects for
manipulating semi-open intervals.

%description -n python3-ligo-segments -l pl.UTF-8
Moduł definiuje obiekty segment, segmentlist i segmentlistdict do
operacji na przedziałach jednostronnie otwartych.

%prep
%setup -q -n ligo-segments-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with py2_tests}
PYTHONPATH=$(readlink -f build-2/lib.*) \
%{__make} -C test check \
	PYTHON=%{__python}
%endif
%endif

%if %{with python3}
%py3_build

%if %{with py3_tests}
PYTHONPATH=$(readlink -f build-3/lib.*) \
%{__make} -C test check \
	PYTHON=%{__python3}
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py_sitedir}/ligo
%dir %{py_sitedir}/ligo/segments
%attr(755,root,root) %{py_sitedir}/ligo/segments/__segments.so
%{py_sitedir}/ligo/segments/*.py[co]
%{py_sitedir}/ligo_segments-%{version}-py*.egg-info
%{py_sitedir}/ligo_segments-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-ligo-segments
%defattr(644,root,root,755)
%doc README.rst
%dir %{py3_sitedir}/ligo
%dir %{py3_sitedir}/ligo/segments
%attr(755,root,root) %{py3_sitedir}/ligo/segments/__segments.cpython-*.so
%{py3_sitedir}/ligo/segments/*.py
%{py3_sitedir}/ligo/segments/__pycache__
%{py3_sitedir}/ligo_segments-%{version}-py*.egg-info
%{py3_sitedir}/ligo_segments-%{version}-py*-nspkg.pth
%endif
