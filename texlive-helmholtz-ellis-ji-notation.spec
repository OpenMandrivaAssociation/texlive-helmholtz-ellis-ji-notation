Name:		texlive-helmholtz-ellis-ji-notation
Version:	55213
Release:	2
Summary:	Beautiful in-line microtonal just intonation accidentals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/helmholtz-ellis-ji-notation
License:	cc-by-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/helmholtz-ellis-ji-notation.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/helmholtz-ellis-ji-notation.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/helmholtz-ellis-ji-notation.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Helmholtz-Ellis JI Pitch Notation (HEJI), devised in the
early 2000s by Marc Sabat and Wolfgang von Schweinitz,
explicitly notates the raising and lowering of the untempered
diatonic Pythagorean notes by specific microtonal ratios
defined for each prime. It provides visually distinctive
"logos" distinguishing families of justly tuned intervals that
relate to the harmonic series. These take the form of strings
of additional accidental symbols based on historical
precedents, extending the traditional sharps and flats. Since
its 2020 update, HEJI ver. 2 ("HEJI2") provides unique
microtonal symbols through the 47-limit. This package is a
simple LaTeX implementation of HEJI2 that allows for in-line
typesetting of microtonal accidentals for use within
theoretical texts, program notes, symbol legends, etc.
Documents must be compiled using XeLaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/helmholtz-ellis-ji-notation
%{_texmfdistdir}/tex/latex/helmholtz-ellis-ji-notation
%{_texmfdistdir}/fonts/opentype/public/helmholtz-ellis-ji-notation
%doc %{_texmfdistdir}/doc/fonts/helmholtz-ellis-ji-notation

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
