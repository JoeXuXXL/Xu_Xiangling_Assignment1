import numpy as np
import matplotlib.pyplot as plt
import warnings

#due to the nature of this code, some values may be to small
#and so the data may be overflow
#here use filter to sort out these warnings
warnings.filterwarnings("ignore", message="overflow encountered in square")
warnings.filterwarnings("ignore", message="overflow encountered in add")
warnings.filterwarnings("ignore", message="overflow encountered in multiply")
warnings.filterwarnings("ignore", message="overflow encountered in substract")
warnings.filterwarnings("ignore", message="invalid \
value encountered in multiply")
warnings.filterwarnings("ignore", message="invalid \
value encountered in subtract")

#N determines the resolution of the plot
print "please enter the resolution N"
print " "
print "The default resolution N is set to 2000, when image"
print "quality is acceptable without zooming in"
print " "
print "Warning: the higher the N is, the longer the plotting will be"
print "If the N is too big "

N = input("Please enter the resolution N of the plot you want: ")

print " "
print "Plotting..."

#define the recursive squence with input 
#of real part and imaginary part of c
def recu(real,imag):
#initialize parameters
	z0 = 0
	i = 0
	c = real*1. + imag * 1.j
	z = z0**2 + c
	bound = 0
#use while loop to compute zk with recursive formula up to k=100
#a reasonable large number to see divergency and convergency
	while i < 100:
#some basic math to get the square of complex number
		zsquare = (z.real*1.)**2 - (z.imag*1.)**2 + 2.j*(z.real*1.)*(z.imag)
#compute the sequence with formula
		z = zsquare + c
		i += 1
#get the square of abs of the last one of the sequence
#as for assessment of bounded or not
	zabsqr = (z.real)**2 + (z.imag)**2
#convert N by N array into N**2 by 1 array for convenience
	zabsqrfla = zabsqr.flatten()
#for all values in the array, check for convergency
	for k in np.arange(N**2):
#if the value is smaller than a big number(1e6 in this case) 
#after so many recursion, can see the sequence to be convergent
#set to value 0
		if zabsqrfla[k] < 1.e6:
			zabsqrfla[k] = 0
#if bigger than the big number, see as divergent, set value 1
		else:
			zabsqrfla[k] = 1
#reshape the new array (with all entries 1 or 0) into N by N
#array for ploting purpose
	outp = zabsqrfla.reshape(N,N)
	return outp

#generating array to represent points on -2-2 for
#both of real number line and imaginary
x = np.linspace(-2,2,N)
y = np.linspace(-2,2,N)

#for plotting
xv, yv=np.meshgrid(x,y)
vals = recu(xv,yv)

axdis = np.array([0,1,2,3,4])
axlab = np.array(np.linspace(-2,-1,0,1,2))

#set labels, plot
plt.imshow(vals, cmap = 'viridis')
plt.title("Fractals/Divergence vs. Convergence in Complex Plane") 
plt.colorbar().set_label("0 is convergent, 1 is convergent")
plt.xlabel("real axis in proportion, the corresponding\
"+'\n'+"real coordinate is (4x/N-2)")
plt.ylabel("imaginary axis in proportion, the corresponding\
"+'\n'+"imaginary coordinate is (4x/N-2)")

plt.show()

#Note
#one of the problem of this code is that it will
#tick axes of both real and imag from 0 to N
#I don't know how to resolve this properly
