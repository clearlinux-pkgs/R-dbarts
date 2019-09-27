#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dbarts
Version  : 0.9.13
Release  : 30
URL      : https://cran.r-project.org/src/contrib/dbarts_0.9-13.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dbarts_0.9-13.tar.gz
Summary  : Discrete Bayesian Additive Regression Trees Sampler
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-dbarts-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-dbarts package.
Group: Libraries

%description lib
lib components for the R-dbarts package.


%prep
%setup -q -c -n dbarts

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569613640

%install
export SOURCE_DATE_EPOCH=1569613640
rm -rf %{buildroot}
export LANG=C.UTF-8
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dbarts
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dbarts
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dbarts
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc dbarts || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dbarts/CITATION
/usr/lib64/R/library/dbarts/DESCRIPTION
/usr/lib64/R/library/dbarts/INDEX
/usr/lib64/R/library/dbarts/Meta/Rd.rds
/usr/lib64/R/library/dbarts/Meta/features.rds
/usr/lib64/R/library/dbarts/Meta/hsearch.rds
/usr/lib64/R/library/dbarts/Meta/links.rds
/usr/lib64/R/library/dbarts/Meta/nsInfo.rds
/usr/lib64/R/library/dbarts/Meta/package.rds
/usr/lib64/R/library/dbarts/NAMESPACE
/usr/lib64/R/library/dbarts/NEWS.Rd
/usr/lib64/R/library/dbarts/R/dbarts
/usr/lib64/R/library/dbarts/R/dbarts.rdb
/usr/lib64/R/library/dbarts/R/dbarts.rdx
/usr/lib64/R/library/dbarts/common/almostLinearBinaryData.R
/usr/lib64/R/library/dbarts/common/friedmanData.R
/usr/lib64/R/library/dbarts/common/hillData.R
/usr/lib64/R/library/dbarts/common/multithreadData.R
/usr/lib64/R/library/dbarts/common/pdData.R
/usr/lib64/R/library/dbarts/common/probitData.R
/usr/lib64/R/library/dbarts/help/AnIndex
/usr/lib64/R/library/dbarts/help/aliases.rds
/usr/lib64/R/library/dbarts/help/dbarts.rdb
/usr/lib64/R/library/dbarts/help/dbarts.rdx
/usr/lib64/R/library/dbarts/help/paths.rds
/usr/lib64/R/library/dbarts/html/00Index.html
/usr/lib64/R/library/dbarts/html/R.css
/usr/lib64/R/library/dbarts/include/dbarts/R_C_interface.hpp
/usr/lib64/R/library/dbarts/include/dbarts/bartFit.hpp
/usr/lib64/R/library/dbarts/include/dbarts/control.hpp
/usr/lib64/R/library/dbarts/include/dbarts/cstdint.hpp
/usr/lib64/R/library/dbarts/include/dbarts/data.hpp
/usr/lib64/R/library/dbarts/include/dbarts/model.hpp
/usr/lib64/R/library/dbarts/include/dbarts/random.hpp
/usr/lib64/R/library/dbarts/include/dbarts/results.hpp
/usr/lib64/R/library/dbarts/include/dbarts/scratch.hpp
/usr/lib64/R/library/dbarts/include/dbarts/state.hpp
/usr/lib64/R/library/dbarts/include/dbarts/types.hpp
/usr/lib64/R/library/dbarts/include/dbarts/types.hpp.in
/usr/lib64/R/library/dbarts/include/dbarts/types.hpp.win
/usr/lib64/R/library/dbarts/tests/testthat.R
/usr/lib64/R/library/dbarts/tests/testthat/test-01-dbartsDataArgs.R
/usr/lib64/R/library/dbarts/tests/testthat/test-02-dbartsModelArgs.R
/usr/lib64/R/library/dbarts/tests/testthat/test-03-dbartsControl.R
/usr/lib64/R/library/dbarts/tests/testthat/test-04-continuousResponse.R
/usr/lib64/R/library/dbarts/tests/testthat/test-05-binaryResponse.R
/usr/lib64/R/library/dbarts/tests/testthat/test-06-dbartsSampler.R
/usr/lib64/R/library/dbarts/tests/testthat/test-07-multithreaded.R
/usr/lib64/R/library/dbarts/tests/testthat/test-08-xbart.R
/usr/lib64/R/library/dbarts/tests/testthat/test-09-predict.R
/usr/lib64/R/library/dbarts/tests/testthat/test-10-makeModelMatrix.R
/usr/lib64/R/library/dbarts/tests/testthat/test-11-multipleAssignment.R
/usr/lib64/R/library/dbarts/tests/testthat/test-12-multipleChains.R
/usr/lib64/R/library/dbarts/tests/testthat/test-13-bart2.R
/usr/lib64/R/library/dbarts/tests/testthat/test-14-rbart.R
/usr/lib64/R/library/dbarts/tests/testthat/test-15-simd.R
/usr/lib64/R/library/dbarts/tests/testthat/test-16-pdbart.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/dbarts/libs/dbarts.so
/usr/lib64/R/library/dbarts/libs/dbarts.so.avx2
/usr/lib64/R/library/dbarts/libs/dbarts.so.avx512
