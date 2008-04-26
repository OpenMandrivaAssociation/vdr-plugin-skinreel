
%define plugin	skinreel
%define name	vdr-plugin-%plugin
%define version	0.0.1
%define rel	5

Summary:	VDR plugin: Reel Skin-Plugin
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
# License according to reelmedia representative posting in thread below:
URL:		http://www.vdr-portal.de/board/thread.php?threadid=42586
Source:		vdr-%plugin-%version.tar.bz2
Patch0:		skinreel-0.0.1-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This is a skin for VDR based on sources of skin for reelbox.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
