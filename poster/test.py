from __future__ import print_function
import numpy as np 
import subprocess
from netCDF4 import Dataset
import time
import json as js

times = {}
sizes = np.array([64,128,256,512,1024,2048,4096])
sizes=sizes[:4]

for lang in ('pyt',) :
  times[lang] = []
  for n in sizes :
    print('lang: ', lang, ' size: ', n, 'x', n)
    # simulation parameters (via the netCDF global attributes)
    ncfile = 'data-' + lang + '.nc'
    nc = Dataset(ncfile, mode='w')
    nc.np = 1
    nc.nx = n
    nc.ny = n
    nc.no = 10
    nc.nt = 100
    nc.Cx = .5
    nc.Cy = .5

    nc.createDimension('t', 0) # unlimited dim
    nc.createDimension('x', nc.nx)
    nc.createDimension('y', nc.ny)
    psi = nc.createVariable('psi', 'float32', ('t','x','y'))
    psi[0,0,0] = 1

    # closing the file, running the solver and reopening the file
    nc.close()
  
    cmd = ('./egu2012-' + lang,) if lang != 'pyt' else ('python', './egu2012.py')
    t0 = time.time()
    subprocess.check_call(cmd + (ncfile,))
    times[lang].append(time.time() - t0)
  
    #nc = netcdf_file(ncfile, mode='r')
    # plotting the result
    #for t in range(nc.nt / nc.no + 1):
    #  print lang, nc.variables['psi'][t,:,:]

js.dump(times, open('times.js','w'))
out=sizes**2.
out=list(out)
print(out)
js.dump(out, open('sizes.js','w'))
