#!/usr/local/bin/python
#CHIPSEC: Platform Security Assessment Framework
#Copyright (c) 2010-2015, Intel Corporation
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



# -------------------------------------------------------------------------------
#
# CHIPSEC: Platform Hardware Security Assessment Framework
# (c) 2010-2012 Intel Corporation
#
# -------------------------------------------------------------------------------

"""
Access to MMIO (Memory Mapped IO) BARs and Memory-Mapped PCI Configuration Space (MMCFG)

usage:
    >>> read_MMIO_reg(cs, bar_base, 0x0, 4 )

    Access MMIO by BAR name:
    
    >>> read_MMIO_BAR_reg( cs, 'MCHBAR', 0x0, 4 )

    Access Memory Mapped Config Space:
    
    >>> get_MMCFG_base_address(cs)
    
    DEPRECATED: Access MMIO by BAR id:
    
    >>> read_MMIOBAR_reg( cs, mmio.MMIO_BAR_MCHBAR, 0x0 )
"""

__version__ = '1.0'

import struct
import sys

import chipsec.chipset
from chipsec.logger import logger
#from chipsec.pci import PCI_BDF

from chipsec.cfg.common import *
from chipsec.chipset    import is_register_defined
from chipsec.hal.pci import PCI_HDR_VID_OFF, PCI_HDR_DID_OFF
from chipsec.hal.hal_base import HALBase

#
# Lewisburg Production LPC Device ID's
#
PCH_LBG_PROD_LPC_DEVICE_ID_0 = 0xA1C0           #LBG PRQ Unfused LBG 0 SKU
PCH_LBG_PROD_LPC_DEVICE_ID_1G = 0xA1C1          #LBG PRQ Fused LBG 1G
PCH_LBG_PROD_LPC_DEVICE_ID_2 = 0xA1C2           #LBG PRQ Fused LBG 2
PCH_LBG_PROD_LPC_DEVICE_ID_4 = 0xA1C3           #LBG PRQ Fused LBG 4
PCH_LBG_PROD_LPC_DEVICE_ID_E = 0xA1C4           #LBG PRQ Fused LBG E
PCH_LBG_PROD_LPC_DEVICE_ID_M = 0xA1C5           #LBG PRQ Fused LBG M
PCH_LBG_PROD_LPC_DEVICE_ID_T = 0xA1C6           #LBG PRQ Fused LBG T (both uplinks SKU - NS)
PCH_LBG_PROD_LPC_DEVICE_ID_LP = 0xA1C7          #LBG PRQ Fused LBG LP

PCH_LBG_PROD_LPC_DEVICE_ID_RESERVED_MAX = 0xA1CF         #0xA1C8-0xA1CF reserved for future QS/PRQ SKUs

#
# Lewisburg SSX (Super SKUs and pre production) LPC Device ID's
#
PCH_LBG_LPC_DEVICE_ID_UNFUSED = 0xA240          #LBG SSX Unfused SKU
PCH_LBG_LPC_DEVICE_ID_SS_0 = 0xA241          #LBG SSX Super SKU 0
PCH_LBG_LPC_DEVICE_ID_SS_4_SD = 0xA242          #LBG SSX Super SKU 4/SD
PCH_LBG_LPC_DEVICE_ID_SS_T80_NS = 0xA243          #LBG SSX Super SKU T80/NS
PCH_LBG_LPC_DEVICE_ID_SS_1G = 0xA244          #LBG SSX Super SKU 1G
PCH_LBG_LPC_DEVICE_ID_SS_T = 0xA245          #LBG Super SKU - T
PCH_LBG_LPC_DEVICE_ID_SS_L = 0xA246          #LBG Super SKU - L

PCH_LBG_LPC_DEVICE_ID_RESERVED_SS_MAX = 0xA24F          #0xA247-0xA24F Super SKU reserved

#
# PCH-LP LPC Device IDs
#
PCH_LP_LPC_DEVICE_ID_MB_SUPER_SKU = 0x9D41          #PCH LP Mobile Super SKU unlocked
PCH_LP_LPC_DEVICE_ID_MB_0 = 0x9D42          #PCH LP Mobile Super SKU locked
PCH_LP_LPC_DEVICE_ID_MB_1 = 0x9D43          #PCH LP Mobile (U) Base SKU
PCH_LP_LPC_DEVICE_ID_MB_2 = 0x9D46          #PCH LP Mobile (Y) Premium SKU
PCH_LP_LPC_DEVICE_ID_MB_3 = 0x9D48          #PCH LP Mobile (U) Premium SKU
PCH_LP_LPC_DEVICE_ID_UNFUSE = 0x9D40          #PCH LP Unfuse

PCH_SERIES_PCH_H = 1
PCH_SERIES_PCH_LP = 2
PCH_SERIES_PCH_UNKNOWN = 3

PCH_H_GPIO_GROUP_MAX = 13
PCH_LP_GPIO_GROUP_MAX = 8

DEFAULT_PCI_BUS_NUMBER_PCH = 0x00
PCI_DEVICE_NUMBER_PCH_P2SB = 0x1f
PCI_FUNCTION_NUMBER_PCH_P2SB = 0x01
PCH_P2SB_CONTROL_OFFSET = 0xE0
PCI_VID_INTEL = 0x8086

def unhide_pch_p2sb(cs):
    # if the P2S bridge is hided then we can't see its VID. 
    vid = cs.pci.read_word( DEFAULT_PCI_BUS_NUMBER_PCH,\
                            PCI_DEVICE_NUMBER_PCH_P2SB,\
                            PCI_FUNCTION_NUMBER_PCH_P2SB,\
                            PCI_HDR_VID_OFF )
    
    if vid == PCI_VID_INTEL:
        return

    # write the control register 0xE0 BIT8 to 0
    # before the bridge is unhided, the register value always is 0xFF
    # so don't need to read and keep other bits before writing.
    cs.pci.write_byte( DEFAULT_PCI_BUS_NUMBER_PCH,\
                       PCI_DEVICE_NUMBER_PCH_P2SB,\
                       PCI_FUNCTION_NUMBER_PCH_P2SB,\
                       PCH_P2SB_CONTROL_OFFSET + 1,\
                       0x00 )

    return    

def is_pch_lbg_prod_lpc_device_id(did):
    if (did >= PCH_LBG_PROD_LPC_DEVICE_ID_0 and\
        did <= PCH_LBG_PROD_LPC_DEVICE_ID_RESERVED_MAX):
        return True
    return False

def is_pch_lbg_ns_lpc_device_id(did):
    if (did == PCH_LBG_LPC_DEVICE_ID_SS_T80_NS or\
        did == PCH_LBG_PROD_LPC_DEVICE_ID_T):
        return True
    return False

def is_pch_lbg_ws_lpc_device_id(did):
    return False

def is_pch_lbg_ssku_lpc_device_id(did):
    if (did >= PCH_LBG_LPC_DEVICE_ID_UNFUSED and\
        did <= PCH_LBG_LPC_DEVICE_ID_RESERVED_SS_MAX):
        return True
    return False

#
# Device IDs that are PCH-H Mobile specific
#
def is_pch_lgb_lpc_device_id(did):
    if (is_pch_lbg_prod_lpc_device_id(did) or\
        is_pch_lbg_ns_lpc_device_id(did) or\
        is_pch_lbg_ws_lpc_device_id(did) or\
        is_pch_lbg_ssku_lpc_device_id(did)):
        return True
    return False

#
# Device IDs that are PCH-LP Mobile specific
#
def is_pch_lp_lpc_device_id_mobile(did):
    if (did == PCH_LP_LPC_DEVICE_ID_UNFUSE or\
        did == PCH_LP_LPC_DEVICE_ID_MB_SUPER_SKU or\
        did == PCH_LP_LPC_DEVICE_ID_MB_0 or\
        did == PCH_LP_LPC_DEVICE_ID_MB_1 or\
        did == PCH_LP_LPC_DEVICE_ID_MB_2 or\
        did == PCH_LP_LPC_DEVICE_ID_MB_3):
        return True
    return False

def get_pch_series(cs):
    lpc_did = cs.pci.read_word( int(cs.Cfg.CONFIG_PCI[ 'LPC' ].get( 'bus' ), 16),\
                                int(cs.Cfg.CONFIG_PCI[ 'LPC' ].get( 'dev' ), 16),\
                                int(cs.Cfg.CONFIG_PCI[ 'LPC' ].get( 'fun' ), 16),\
                                PCI_HDR_DID_OFF )
    if (is_pch_lgb_lpc_device_id(lpc_did)):
        return PCH_SERIES_PCH_H
    elif (is_pch_lp_lpc_device_id_mobile(lpc_did)):
        return PCH_SERIES_PCH_LP
    return PCH_SERIES_PCH_UNKNOWN

def is_support_gpio(cs):
    return True

class GpioRuntimeError (RuntimeError):
    pass

class GPIO(HALBase):
    def __init__( self, cs ):
        self.cs = cs

    def dump(self):
        gpio_bar = []
        if (False == self.get_base_address( gpio_bar )):
          return False
        
        for gpio in self.cs.Cfg.GPIOS:
            val = chipsec.chipset.read_register ( self.cs, gpio )
            logger().log( "%s = 0x%x" % (gpio, val) )

        return True

    #
    # Get base address of GPIO
    #
    def get_base_address(self, bar):
        if False == chipsec.chipset.is_register_defined( self.cs, 'GPIOBASE' ):
            logger().error( "Couldn't find definition of required configuration registers" )
            return False

        val = chipsec.chipset.read_register_field( self.cs, 'GPIOBASE', 'Base', preserve_field_position=True )

        if (0x00 == val or
            0xFF == val):
          logger().error( "GPIO BAR value is not vaild!" )
          return False

        bar.append( val )
    
        return True



