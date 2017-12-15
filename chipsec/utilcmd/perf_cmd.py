#!/usr/bin/python
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
The temperature command allows to get the temperature of CPU.
"""

import os
import time

import chipsec_util
import chipsec.defines
import chipsec.file

from chipsec.logger     import print_buffer
from chipsec.command    import BaseCommand

from chipsec.hal.msr    import Msr

# system performance
class PerfCommand(BaseCommand):
    """
    >>> chipsec_util perf <op>
    >>>
    >>> <op>                : regsdump

    Examples:

    >>> chipsec_util perf regsdump         
    """

    def dump_regs(self):
        return
        
    def requires_driver(self):
        # No driver required when printing the util documentation
        if len(self.argv) < 3:
            return False
        return True      

    def run(self):
        if len(self.argv) < 3:
            print PerfCommand.__doc__
            return

        op = self.argv[2]
        t = time.time()

        if 'regsdump'   == op:
            self.dump_regs()
        else:
            print PerfCommand.__doc__
            return
        
        self.logger.log( "[CHIPSEC] (mem) time elapsed %.3f" % (time.time()-t) )

commands = { 'perf': PerfCommand }
