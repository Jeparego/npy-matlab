# npy-matlab

Code to read and write NumPy's NPY format (`.npy` files) in MATLAB for structed ndarrays.

This code
- Only reads a subset of all possible NPY files, specifically structed N-D arrays of
  certain data types.
- Writes not modified yet
- Always outputs a shape according to matlab's convention, e.g. (10, 1)
  rather than (10,).
  
For the complete specification of the NPY format, see the [NumPy documentation](https://www.numpy.org/devdocs/reference/generated/numpy.lib.format.html).

## Installation
After downloading npy-matlab as a zip file or via git, just add the
npy-matlab directory to your search path:

```matlab
>> addpath('/npy-matlab/npy-matlab')  
>> savepath
```
