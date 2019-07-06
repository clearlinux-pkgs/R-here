#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-here
Version  : 0.1
Release  : 10
URL      : https://cran.r-project.org/src/contrib/here_0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/here_0.1.tar.gz
Summary  : A Simpler Way to Find Your Files
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : R-backports
BuildRequires : R-rprojroot
BuildRequires : buildreq-R

%description
here [![Travis-CI Build Status](https://travis-ci.org/krlmlr/here.svg?branch=master)](https://travis-ci.org/krlmlr/here)
========================================================================================================================

%prep
%setup -q -c -n here

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552894753

%install
export SOURCE_DATE_EPOCH=1552894753
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library here
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library here
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library here
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  here || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/here/DESCRIPTION
/usr/lib64/R/library/here/INDEX
/usr/lib64/R/library/here/Meta/Rd.rds
/usr/lib64/R/library/here/Meta/features.rds
/usr/lib64/R/library/here/Meta/hsearch.rds
/usr/lib64/R/library/here/Meta/links.rds
/usr/lib64/R/library/here/Meta/nsInfo.rds
/usr/lib64/R/library/here/Meta/package.rds
/usr/lib64/R/library/here/NAMESPACE
/usr/lib64/R/library/here/NEWS.md
/usr/lib64/R/library/here/R/here
/usr/lib64/R/library/here/R/here.rdb
/usr/lib64/R/library/here/R/here.rdx
/usr/lib64/R/library/here/help/AnIndex
/usr/lib64/R/library/here/help/aliases.rds
/usr/lib64/R/library/here/help/here.rdb
/usr/lib64/R/library/here/help/here.rdx
/usr/lib64/R/library/here/help/paths.rds
/usr/lib64/R/library/here/html/00Index.html
/usr/lib64/R/library/here/html/R.css
