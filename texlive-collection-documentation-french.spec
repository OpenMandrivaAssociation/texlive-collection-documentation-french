# revision 25105
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-french
Version:	20120223
Release:	1
Summary:	French documentation
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-documentation-french.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-apprends-latex
Requires:	texlive-epslatex-fr
Requires:	texlive-impatient-fr
Requires:	texlive-l2tabu-french
Requires:	texlive-lshort-french
Requires:	texlive-texlive-fr
Requires:	texlive-translation-array-fr
Requires:	texlive-translation-dcolumn-fr
Requires:	texlive-translation-natbib-fr
Requires:	texlive-translation-tabbing-fr
Requires:	texlive-collection-documentation-base

%description
TeXLive collection-documentation-french package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
