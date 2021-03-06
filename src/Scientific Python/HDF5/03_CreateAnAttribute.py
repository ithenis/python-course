#
# This examaple creates and writes two attributes on the "dset" dataset created by 01_CreateDataset.py.
#
import h5py
import numpy as np
#
# Open an existing file using defaut properties.
#
file = h5py.File('dset.h5','r+')
#
# Open "dset" dataset.
#
dataset = file['/dset']
#
# Create string attribute.
#
attr_string = "Meter per second"
dataset.attrs["Units"] = attr_string
#
# Create integer array attribute.
#
attr_data = np.zeros((2))
attr_data[0] = 100
attr_data[1] = 200
#
#
dataset.attrs.create("Speed", attr_data, (2,), h5py.h5t.STD_I32BE)
#
# Close the file before exiting
#
file.close()
