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



""" 
usage as a standalone utility:
    >>> chipsec_util gpio dump
"""

__version__ = '1.0'

from chipsec.command    import BaseCommand
from chipsec.hal.gpio   import *
from chipsec.chipset import *

# ###################################################################
#
# Chipset GPIO pin definition
#
# ###################################################################
class GpioCommand(BaseCommand):
    """
    >>> chipsec_util gpio dump
    
    Examples: chipsec_util gpio dump
    
    >>> chipsec_util gpio dump
    """

    def requires_driver(self):
        return True

    def run(self):
        if False == is_support_gpio(self.cs):
            return

        try:
            _gpio = GPIO( self.cs )
        except GpioRuntimeError, msg:
            print msg
            return
        
        op = self.argv[2]
        if ( 'dump' == op ):
            _gpio.dump()
        else:
            self.logger.error( "unknown command-line option '%.32s'" % op )
            print GpioCommand.__doc__
            return
        
commands = { 'gpio': GpioCommand }
