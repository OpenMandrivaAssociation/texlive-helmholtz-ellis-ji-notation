%global tl_name helmholtz-ellis-ji-notation
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Beautiful in-line microtonal just intonation accidentals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/helmholtz-ellis-ji-notation
License:	cc-by-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/helmholtz-ellis-ji-notation.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/helmholtz-ellis-ji-notation.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/helmholtz-ellis-ji-notation.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Helmholtz-Ellis JI Pitch Notation (HEJI), devised in the early 2000s
by Marc Sabat and Wolfgang von Schweinitz, explicitly notates the
raising and lowering of the untempered diatonic Pythagorean notes by
specific microtonal ratios defined for each prime. It provides visually
distinctive "logos" distinguishing families of justly tuned intervals
that relate to the harmonic series. These take the form of strings of
additional accidental symbols based on historical precedents, extending
the traditional sharps and flats. Since its 2020 update, HEJI ver. 2
("HEJI2") provides unique microtonal symbols through the 47-limit. This
package is a simple LaTeX implementation of HEJI2 that allows for in-
line typesetting of microtonal accidentals for use within theoretical
texts, program notes, symbol legends, etc. Documents must be compiled
using XeLaTeX.

