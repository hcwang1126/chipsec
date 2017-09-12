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
#Copyright (c) 2010-2016, Intel Corporation
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
# Authors:
#  HC Wang
#


"""
Checks if performance registers are correct.

"""

from chipsec.module_common import *

IOUT_SLOPE_DEFAULT = 0x200

# ############################################################
# SPECIFY PLATFORMS THIS MODULE IS APPLICABLE TO
# ############################################################
_MODULE_NAME = 'perf'

TAGS = [MTAG_HWCONFIG]


class perf(BaseModule):

    def __init__(self):
        BaseModule.__init__(self)

    def is_supported(self):
        return True

    def check_iout_slope(self):
        vr_misc_config = self.cs.read_register( 'VR_MISC_CONFIG' )
        self.cs.print_register( 'VR_MISC_CONFIG', vr_misc_config )

        return self.cs.read_register_field( 'VR_MISC_CONFIG', 'IOUT_SLOPE', True )

    def check_perf_cfg( self ):
        self.logger.start_test( "Performance Registers Check" )

        iout_slope= self.check_iout_slope()
        
        if iout_slope > IOUT_SLOPE_DEFAULT:
            res = ModuleResult.WARNING
            self.logger.log_warn_check( "IOUT_SLOPE could be not equal to default for better performance." )
        else:
            res = ModuleResult.PASSED
            self.logger.log_passed_check( "All registers are set in performance spec" )

        return res


    # --------------------------------------------------------------------------
    # run( module_argv )
    # Required function: run here all tests from this module
    # --------------------------------------------------------------------------
    def run( self, module_argv ):
        return self.check_perf_cfg()
