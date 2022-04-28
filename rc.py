__all__ = ['rc']

import pkg_resources
import os

path = 'run_vasp_default.py'
filepath = pkg_resources.resource_filename(__name__,path)



def rc(q="'*@@schneider_d12chas'", pe = "'mpi-24'", nprocs = 24):
    script = open(filepath,"r")
    alllines = script.readlines()
    for i,line in enumerate(alllines):
        if 'q =' in line:
            line = line.split(' ')
            line[-1] = "'"+q+"'"+'\n'
            alllines[i] = ' '.join(line)
        if 'pe =' in line:
            line = line.split(' ')
            line[-1] = "'"+pe+"'"+'\n'
            alllines[i] = ' '.join(line)
        if 'nprocs =' in line:
            line = line.split(' ')
            line[-1] = str(nprocs)+"'\n"
            alllines[i] = ' '.join(line)

    file = os.getenv('VASP_SCRIPT')
    #file = '/afs/crc.nd.edu/user/j/jcrum/System/run_vasp_2.py'
    file1 = open(file, "w")
    file1.writelines(alllines)
    file1.close()

    return
