## Check intermediate values to debug the mandelbrot_calculator written in VHDL
import numpy as np
import matplotlib.pyplot as plt

num_iter = 100

c_real = 0.25
c_imag = 0.25
z_real = 0
z_imag = 0

for i in range (num_iter) :
    z_real_new = z_real**2 - z_imag**2 + c_real
    z_imag_new = z_imag*2*z_real + c_imag

    z_real = z_real_new
    z_imag = z_imag_new
    print("iteration : %d | z_real = %.8f | z_imag = %.8f" % (i,z_real,z_imag))
    if ((z_real**2 + z_imag**2) >= 4) :
        iter_array[IM, RE] = i
        break
