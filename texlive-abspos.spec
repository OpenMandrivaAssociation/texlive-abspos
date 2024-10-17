Name:		texlive-abspos
Version:	64465
Release:	2
Summary:	Absolute placement with coffins
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/abspos
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abspos.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abspos.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abspos.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package lets you place contents at an absolute position,
anchored at some specified part of the contents, similar to how
TikZ nodes work, though without using the two-pass strategy of
TikZ. It also avoids messing with the order of beamer overlays,
which is what happens when one uses the textpos package with
the overlay option. The solution used is quite straightforward,
combining coffins (using l3coffins) with the placement
mechanisms of atbegshi.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/abspos
%{_texmfdistdir}/tex/latex/abspos
%doc %{_texmfdistdir}/doc/latex/abspos

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
