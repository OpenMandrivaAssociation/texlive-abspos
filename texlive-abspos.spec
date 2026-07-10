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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package lets you place contents at an absolute position, anchored
at some specified part of the contents, similar to how TikZ nodes work,
though without using the two-pass strategy of TikZ. It also avoids
messing with the order of beamer overlays, which is what happens when
one uses the textpos package with the overlay option. The solution used
is quite straightforward, combining coffins (using l3coffins) with the
placement mechanisms of atbegshi.

