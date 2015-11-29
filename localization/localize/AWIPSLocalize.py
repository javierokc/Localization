'''
Created on Nov 29, 2015

@author: javier

@version: 1.0.1
'''
import sys
from optparse import OptionParser

class AWIPSLocalize(object):
    '''
    AWIPS II 14.4 Localization class
    '''
    EDEX_BASE = "/awips2/edex/data/utility"
    CAVE_CONFIG = EDEX_BASE + "/cave_config"
    CAVE_STATIC = EDEX_BASE + "/cave_static"
    COMMON_STATIC = EDEX_BASE + "/common_static"
    EDEX_STATIC = EDEX_BASE + "/edex_static"
    
    def localizeSite(self):
        bufr = "%s/site/%s" % (self.CAVE_STATIC, self.site)
        print(bufr)
    
    def __repr__(self):
        bufr = "Method: '%s'\n" % self.mode
        bufr += "Site: '%s'\n" % self.site
        bufr += "Verbose: %s" % self.verbose
        return bufr
    
    def __init__(self, site="OUN", verbose=False, mode="create"):
        '''
        Constructor
        '''
        self.site = site
        self.verbose = verbose
        self.mode = mode

        
def main():
    usage = "Usage: %prog [options] SITE"
    parser = OptionParser(usage = usage)
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="Print more")
    parser.add_option("-m", "--method", dest="method", metavar="MODE", default="view", help="Use method MODE: create|erase|view (default=%default)")
    (cmdlineopt, args) = parser.parse_args()
    if cmdlineopt.method in ("view","erase","create") and len(args) > 0:
        site = args[0]
    else:
        parser.print_help()
        sys.exit()
    
    local = AWIPSLocalize(site, cmdlineopt.verbose, cmdlineopt.method)
    local.localizeSite()
    print("%s" % local)
    
if __name__ == "__main__":
    main()
else:
    print("My name is not main; my name is mine.")