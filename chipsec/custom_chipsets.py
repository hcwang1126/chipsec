#!/usr/bin/env python
#
# *********************************************************
# 
#                   PRE-RELEASE NOTICE
#
#        This file contains pre-release functionality
#        Please do not distribute this file publicly
#
# *********************************************************
#
#CHIPSEC: Platform Security Assessment Framework
#Copyright (c) 2010-2017, Intel Corporation
# 
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; Version 2.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#Contact information:
#chipsec@intel.com
#



"""
Contains support of pre-release platforms
"""

import chipset

CHIPSET_ID_BLK  = 1000 + 1
CHIPSET_ID_CNTG = 1000 + 2
CHIPSET_ID_EGLK = 1000 + 3
CHIPSET_ID_TBG  = 1000 + 4
CHIPSET_ID_LFD  = 1000 + 5
CHIPSET_ID_JSP  = 1000 + 6
CHIPSET_ID_WSM  = 1000 + 7

CHIPSET_ID_SKX  = 1000 + 12
CHIPSET_ID_KNL  = 1000 + 13

CHIPSET_ID_APL  = 2000 + 2


chipset.CHIPSET_FAMILY_XEON.extend([CHIPSET_ID_TBG,CHIPSET_ID_SKX,CHIPSET_ID_KNL])
chipset.CHIPSET_FAMILY_CORE.extend([CHIPSET_ID_LFD,CHIPSET_ID_WSM])
chipset.CHIPSET_FAMILY_ATOM.extend([CHIPSET_ID_APL])
chipset.CHIPSET_FAMILY_QUARK.extend([])


my_dict = {

# 3 Series Desktop Chipset (Broadwater and Bearlake) = 29xx
0x2970 : {'name' : 'Bearlake',       'id' : CHIPSET_ID_BLK , 'code' : 'BLK',  'longname' : 'BearLake MCH / ICH9' },
0x2980 : {'name' : 'Bearlake',       'id' : CHIPSET_ID_BLK , 'code' : 'BLK',  'longname' : 'BearLake MCH - Woodriver / ICH9' },
0x2990 : {'name' : 'Bearlake',       'id' : CHIPSET_ID_BLK , 'code' : 'BLK',  'longname' : 'BearLake MCH - Aledo / ICH9' },
0x29B0 : {'name' : 'Bearlake',       'id' : CHIPSET_ID_BLK , 'code' : 'BLK',  'longname' : 'BearLake MCH - Q35 Host Controller / ICH9' },
0x29C0 : {'name' : 'Bearlake',       'id' : CHIPSET_ID_BLK , 'code' : 'BLK',  'longname' : 'BearLake MCH - G33/P35 Host Controller / ICH9' },
0x29D0 : {'name' : 'Bearlake',       'id' : CHIPSET_ID_BLK , 'code' : 'BLK',  'longname' : 'BearLake MCH - Q33 Host Controller / ICH9' },
0x29E0 : {'name' : 'Bearlake',       'id' : CHIPSET_ID_BLK , 'code' : 'BLK',  'longname' : 'BearLake MCH - X38 Host Controller / ICH9' },
0x29F0 : {'name' : 'Bearlake',       'id' : CHIPSET_ID_BLK , 'code' : 'BLK',  'longname' : 'BearLake MCH - Bigby / ICH9' },

# 4 Series Mobile Chipset (Cantiga) = 2A4x - 2AF0
0x2A40 : {'name' : 'Cantiga',        'id' : CHIPSET_ID_CNTG, 'code' : 'CNTG',  'longname' : 'Cantiga MCH / ICH9m' },
0x2A50 : {'name' : 'Cantiga',        'id' : CHIPSET_ID_CNTG, 'code' : 'CNTG',  'longname' : 'Cantiga MCH / ICH9m' },
0x2A60 : {'name' : 'Cantiga',        'id' : CHIPSET_ID_CNTG, 'code' : 'CNTG',  'longname' : 'Cantiga MCH / ICH9m' },
0x2A70 : {'name' : 'Cantiga',        'id' : CHIPSET_ID_CNTG, 'code' : 'CNTG',  'longname' : 'Cantiga MCH / ICH9m' },
0x2A80 : {'name' : 'Cantiga',        'id' : CHIPSET_ID_CNTG, 'code' : 'CNTG',  'longname' : 'Cantiga MCH / ICH9m' },
0x2A90 : {'name' : 'Cantiga',        'id' : CHIPSET_ID_CNTG, 'code' : 'CNTG',  'longname' : 'Cantiga MCH / ICH9m' },
0x2AA0 : {'name' : 'Cantiga',        'id' : CHIPSET_ID_CNTG, 'code' : 'CNTG',  'longname' : 'Cantiga MCH / ICH9m' },
0x2AB0 : {'name' : 'Cantiga',        'id' : CHIPSET_ID_CNTG, 'code' : 'CNTG',  'longname' : 'Cantiga MCH / ICH9m' },
0x2AC0 : {'name' : 'Cantiga',        'id' : CHIPSET_ID_CNTG, 'code' : 'CNTG',  'longname' : 'Cantiga MCH / ICH9m' },
0x2AD0 : {'name' : 'Cantiga',        'id' : CHIPSET_ID_CNTG, 'code' : 'CNTG',  'longname' : 'Cantiga MCH / ICH9m' },
0x2AE0 : {'name' : 'Cantiga',        'id' : CHIPSET_ID_CNTG, 'code' : 'CNTG',  'longname' : 'Cantiga MCH / ICH9m' },
0x2AF0 : {'name' : 'Cantiga',        'id' : CHIPSET_ID_CNTG, 'code' : 'CNTG',  'longname' : 'Cantiga MCH / ICH9m' },

# 4 Series Desktop Chipset (Eaglelake) = 2E0x,2E1x,2E2x,2E3x,2E4
0x2E00 : {'name' : 'Eaglelake',      'id' : CHIPSET_ID_EGLK, 'code' : 'EGLK',  'longname' : 'EagleLake MCH / ICH10' },
0x2E10 : {'name' : 'Eaglelake',      'id' : CHIPSET_ID_EGLK, 'code' : 'EGLK',  'longname' : 'EagleLake MCH - Q45/Q43 Host Controller / ICH10' },
0x2E20 : {'name' : 'Eaglelake',      'id' : CHIPSET_ID_EGLK, 'code' : 'EGLK',  'longname' : 'EagleLake MCH - G45/G43/P45 Host Controller / ICH10'    },
0x2E30 : {'name' : 'Eaglelake',      'id' : CHIPSET_ID_EGLK, 'code' : 'EGLK',  'longname' : 'EagleLake MCH - G41 Host Controller / ICH10'            },
0x2E40 : {'name' : 'Eaglelake',      'id' : CHIPSET_ID_EGLK, 'code' : 'EGLK',  'longname' : 'EagleLake MCH - B43 Host Controller / ICH10'            },
0x2E90 : {'name' : 'Eaglelake',      'id' : CHIPSET_ID_EGLK, 'code' : 'EGLK',  'longname' : 'EagleLake MCH - B43 (Upgraded) Host Controller / ICH10' },

# Core Processor Family (Westmere)
# 0x004x
# 0x0061 ??
0x0040 : {'name' : 'Westmere',       'id' : CHIPSET_ID_WSM , 'code' : 'WSM',  'longname' : 'Westmere Desktop (Ironlake GMCH) / Ibex Peak PCH' },
0x0044 : {'name' : 'Westmere',       'id' : CHIPSET_ID_WSM , 'code' : 'WSM',  'longname' : 'Westmere Mobile (Ironlake GMCH) / Ibex Peak PCH' },
0x0048 : {'name' : 'Westmere',       'id' : CHIPSET_ID_WSM , 'code' : 'WSM',  'longname' : 'Westmere Workstation/Server (Ironlake GMCH) / Ibex Peak PCH' },


# Tylersburg IOH
# 0x340x
0x3400 : {'name' : 'Tylersburg',     'id' : CHIPSET_ID_TBG , 'code' : 'TBG',  'longname' : 'Nehalem CPU / Tylersburg IOH' },
0x3401 : {'name' : 'Tylersburg',     'id' : CHIPSET_ID_TBG , 'code' : 'TBG',  'longname' : 'Nehalem CPU / Tylersburg IOH' },
0x3402 : {'name' : 'Tylersburg',     'id' : CHIPSET_ID_TBG , 'code' : 'TBG',  'longname' : 'Nehalem CPU / Tylersburg IOH' },
0x3403 : {'name' : 'Tylersburg',     'id' : CHIPSET_ID_TBG , 'code' : 'TBG',  'longname' : 'Nehalem CPU / Tylersburg IOH' },
0x3404 : {'name' : 'Tylersburg',     'id' : CHIPSET_ID_TBG , 'code' : 'TBG',  'longname' : 'Nehalem CPU / Tylersburg IOH' },
0x3405 : {'name' : 'Tylersburg',     'id' : CHIPSET_ID_TBG , 'code' : 'TBG',  'longname' : 'Nehalem CPU / Tylersburg IOH' },
0x3406 : {'name' : 'Tylersburg',     'id' : CHIPSET_ID_TBG , 'code' : 'TBG',  'longname' : 'Nehalem CPU / Tylersburg IOH' },
0x3407 : {'name' : 'Tylersburg',     'id' : CHIPSET_ID_TBG , 'code' : 'TBG',  'longname' : 'Nehalem CPU / Tylersburg IOH' },

# Lynnfield based CPUs
0xD130 : {'name' : 'Lynnfield',      'id' : CHIPSET_ID_LFD , 'code' : 'LFD',  'longname' : 'Foxhollow' },
0xD131 : {'name' : 'Lynnfield',      'id' : CHIPSET_ID_LFD , 'code' : 'LFD',  'longname' : 'Intel Core i7-800 and i5-700 Desktop (Lynnfield DT)' },
0xD132 : {'name' : 'Lynnfield',      'id' : CHIPSET_ID_LFD , 'code' : 'LFD',  'longname' : 'Intel Core i7-800 and i5-700 Desktop (Lynnfield DT)' },
0xD133 : {'name' : 'Lynnfield',      'id' : CHIPSET_ID_LFD , 'code' : 'LFD',  'longname' : 'Intel Core i7-800 and i5-700 Desktop (Lynnfield DT)' },
0xD134 : {'name' : 'Lynnfield',      'id' : CHIPSET_ID_LFD , 'code' : 'LFD',  'longname' : 'Intel Core i7-800 and i5-700 Desktop (Lynnfield DT)' },
0xD135 : {'name' : 'Lynnfield',      'id' : CHIPSET_ID_LFD , 'code' : 'LFD',  'longname' : 'Intel Core i7-800 and i5-700 Desktop (Lynnfield DT)' },
0xD136 : {'name' : 'Lynnfield',      'id' : CHIPSET_ID_LFD , 'code' : 'LFD',  'longname' : 'Intel Core i7-800 and i5-700 Desktop (Lynnfield DT)' },
0xD137 : {'name' : 'Lynnfield',      'id' : CHIPSET_ID_LFD , 'code' : 'LFD',  'longname' : 'Intel Core i7-800 and i5-700 Desktop (Lynnfield DT)' },


# Jasper Forest
# 0x371x - 0x372x ??
0x3710 : {'name' : 'Jasper Forest',  'id' : CHIPSET_ID_JSP , 'code' : 'JSP',  'longname' : 'Jasper Forest' },

# Sandy Bridge
0x010C : {'name' : 'Sandy Bridge',   'id' : chipset.CHIPSET_ID_SNB , 'code' : 'SNB',  'longname' : 'Sandy Bridge' },

# Knights Landing Server
0x7801 : {'name' : 'Knights Landing Server', 'id' : CHIPSET_ID_KNL,  'code' : 'KNL',  'longname' : 'Intel Xeon Phi Processor (Knights Landing Server CPU / Wellsburg PCH)'},
0x7802 : {'name' : 'Knights Landing Server', 'id' : CHIPSET_ID_KNL,  'code' : 'KNL',  'longname' : 'Intel Xeon Phi Processor (Knights Landing Server CPU / Wellsburg PCH)'},
0x7803 : {'name' : 'Knights Landing Server', 'id' : CHIPSET_ID_KNL,  'code' : 'KNL',  'longname' : 'Intel Xeon Phi Processor (Knights Landing Server CPU / Wellsburg PCH)'},
0x7804 : {'name' : 'Knights Landing Server', 'id' : CHIPSET_ID_KNL,  'code' : 'KNL',  'longname' : 'Intel Xeon Phi Processor (Knights Landing Server CPU / Wellsburg PCH)'},
0x7805 : {'name' : 'Knights Landing Server', 'id' : CHIPSET_ID_KNL,  'code' : 'KNL',  'longname' : 'Intel Xeon Phi Processor (Knights Landing Server CPU / Wellsburg PCH)'},
0x7806 : {'name' : 'Knights Landing Server', 'id' : CHIPSET_ID_KNL,  'code' : 'KNL',  'longname' : 'Intel Xeon Phi Processor (Knights Landing Server CPU / Wellsburg PCH)'},
0x7818 : {'name' : 'Knights Landing Server', 'id' : CHIPSET_ID_KNL,  'code' : 'KNL',  'longname' : 'Intel Xeon Phi Processor (Knights Landing Server CPU / Wellsburg PCH)'},
0x7819 : {'name' : 'Knights Landing Server', 'id' : CHIPSET_ID_KNL,  'code' : 'KNL',  'longname' : 'Intel Xeon Phi Processor (Knights Landing Server CPU / Wellsburg PCH)'},
0x783D : {'name' : 'Knights Landing Server', 'id' : CHIPSET_ID_KNL,  'code' : 'KNL',  'longname' : 'Intel Xeon Phi Processor (Knights Landing Server CPU / Wellsburg PCH)'},

# Broadwell
0x1608 : {'name' : 'Broadwell',      'id' : chipset.CHIPSET_ID_BDW , 'code' : 'BDW',  'longname' : 'Intel Xeon Processor E3 (Broadwell CPU)' },

# Kabylake
0x5914 : {'name' : 'Kabylake',       'id' : chipset.CHIPSET_ID_KBL , 'code' : chipset.CHIPSET_CODE_KBL,  'longname' : 'Desktop 7th Generation Core Processor (Kabylake)' },

# Skylake Server 
0x2020 : {'name' : 'Skylake',        'id' : CHIPSET_ID_SKX , 'code' : 'SKX',  'longname' : 'Intel Xeon Processor E5 v5 (Skylake CPU)' },

#
# Atom based SoC platforms
#

# Braswell
0x22B0 : {'name' : 'Braswell','id' : chipset.CHIPSET_ID_BSW , 'code' : 'BSW',  'longname' : 'Braswell SoC' },

# Apollo Lake
0x5AF0 : {'name' : 'Apollo Lake','id' : CHIPSET_ID_APL , 'code' : 'APL',  'longname' : 'Apollo Lake' },


}

chipset.Chipset_Dictionary.update(my_dict)
