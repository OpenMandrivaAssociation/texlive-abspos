%global tl_name abspos
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Absolute placement with coffins
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/abspos
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abspos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abspos.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abspos.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package lets you place contents at an absolute position, anchored
at some specified part of the contents, similar to how TikZ nodes work,
though without using the two-pass strategy of TikZ. It also avoids
messing with the order of beamer overlays, which is what happens when
one uses the textpos package with the overlay option. The solution used
is quite straightforward, combining coffins (using l3coffins) with the
placement mechanisms of atbegshi.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/abspos
%dir %{_datadir}/texmf-dist/source/latex/abspos
%dir %{_datadir}/texmf-dist/tex/latex/abspos
%doc %{_datadir}/texmf-dist/doc/latex/abspos/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/abspos/README.md
%doc %{_datadir}/texmf-dist/doc/latex/abspos/abspos.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abspos/demo.tex
%doc %{_datadir}/texmf-dist/source/latex/abspos/abspos.dtx
%{_datadir}/texmf-dist/tex/latex/abspos/abspos.sty
