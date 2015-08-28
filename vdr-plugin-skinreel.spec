%define plugin	skinreel

Summary:	VDR plugin: Reel Skin-Plugin
Name:		vdr-plugin-%plugin
Version:	0.0.1
Release:	12
Group:		Video
License:	GPL
# License according to reelmedia representative posting in thread below:
URL:		http://www.vdr-portal.de/board/thread.php?threadid=42586
Source:		vdr-%plugin-%version.tar.bz2
Patch0:		skinreel-0.0.1-i18n-1.6.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This is a skin for VDR based on sources of skin for reelbox.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%vdr_plugin_prep
find . -perm 0600 -exec chmod a+r {} \;

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.1-8mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.1-7mdv2009.1
+ Revision: 359365
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1-6mdv2009.0
+ Revision: 197977
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1-5mdv2009.0
+ Revision: 197722
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1-4mdv2008.1
+ Revision: 145201
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1-3mdv2008.1
+ Revision: 103211
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1-2mdv2008.0
+ Revision: 50045
- rebuild for new vdr

* Wed Jun 27 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1-1mdv2008.0
+ Revision: 44964
- initial Mandriva release

