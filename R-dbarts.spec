#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: 750e50d
#
Name     : R-dbarts
Version  : 0.9.26
Release  : 68
URL      : https://cran.r-project.org/src/contrib/dbarts_0.9-26.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dbarts_0.9-26.tar.gz
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
%setup -q -n dbarts
pushd ..
cp -a dbarts buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707150914

%install
export SOURCE_DATE_EPOCH=1707150914
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/dbarts/Meta/vignette.rds
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
/usr/lib64/R/library/dbarts/doc/gibbs_sampler_mixture_model.R
/usr/lib64/R/library/dbarts/doc/gibbs_sampler_mixture_model.Rmd
/usr/lib64/R/library/dbarts/doc/gibbs_sampler_mixture_model.pdf
/usr/lib64/R/library/dbarts/doc/index.html
/usr/lib64/R/library/dbarts/doc/working_with_saved_trees.R
/usr/lib64/R/library/dbarts/doc/working_with_saved_trees.Rmd
/usr/lib64/R/library/dbarts/doc/working_with_saved_trees.pdf
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
/usr/lib64/R/library/dbarts/tests/testthat/test-09-generics.R
/usr/lib64/R/library/dbarts/tests/testthat/test-10-makeModelMatrix.R
/usr/lib64/R/library/dbarts/tests/testthat/test-11-multipleAssignment.R
/usr/lib64/R/library/dbarts/tests/testthat/test-12-multipleChains.R
/usr/lib64/R/library/dbarts/tests/testthat/test-13-bart2.R
/usr/lib64/R/library/dbarts/tests/testthat/test-14-rbart.R
/usr/lib64/R/library/dbarts/tests/testthat/test-15-simd.R
/usr/lib64/R/library/dbarts/tests/testthat/test-16-pdbart.R
/usr/lib64/R/library/dbarts/tests/testthat/test-17-rng.R
/usr/lib64/R/library/dbarts/tests/testthat/test-18-extractedTrees.R
/usr/lib64/R/library/dbarts/tests/testthat/test-19-splitProbabilities.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/dbarts/libs/dbarts.so
/usr/lib64/R/library/dbarts/libs/dbarts.so
