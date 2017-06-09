#!/usr/bin/env python

import sys
import subprocess

__all__ = ['get', 'put', 'CAGET', 'CAPUT']

CAGET = 'caget'
CAPUT = 'caput'

def get(*pvs):
    """
    Returns caget output for pvs as string.  Raises ValueError on caget error.
    Returns terse strings if ``terse'' is true.
    """
    pvs = [str(s) for s in pvs]
    args = [CAGET, '-t']
    args.extend(pvs)
    
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = process.communicate()
    
    if process.returncode != 0:
        raise ValueError(stderrdata)
            
    return stdoutdata.strip()

def put(pv, *values):
    """
    Returns caput output as string for writing value_list to pv.  Raises
    ValueError on caput error.  Returns terse strings if ``terse'' is true.
    """
    pv = str(pv)
    value_list = [str(v) for v in values]
    args = [CAPUT, '-t', pv]
    
    if len(value_list) > 1:
        args.insert(2, '-a')
        args.append(str(len(value_list)))
        
    args.extend(value_list)
        
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = process.communicate()
    
    if process.returncode != 0:
        raise ValueError(stderrdata)
    
    return stdoutdata.strip()
    
def main():
    try:
        print get("IOC:BSY0:MP01:TTBLST")
        print get("lclsdev93:aiExample1")
        print get("IOC:BSY0:MP01:DBVERS")
        print put(4, "lclsdev93:testai1")
        print put(7, "lclsdev93:testai1")
        print put(7.4, "lclsdev93:testai2")
    except ValueError, e:
        print 'Error: {0}'.format(e)

if __name__ == '__main__':
    status = main()
    sys.exit(status)
    
    
