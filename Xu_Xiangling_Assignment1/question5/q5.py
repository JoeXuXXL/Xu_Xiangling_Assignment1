import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

#define f(x), derivative is 2x-1, at x=1, derivative is 1
def myf(x):
	return x*(x-1)

print "Analytical derivative f'(x)= 2x-1"
print "At x = 1, the analytical derivative f'(x)=1"
print " "

#define derivative function with x and delta,
#with definition of derivative
def de(x,sdelta):
	bdelta = myf(x+sdelta) - myf(x)
#derv for dealing with abnomality for small float
	derv = bdelta/sdelta
	return derv

#generate an array from 1e-14 to 1e-4 with log space
dellog = np.logspace(-14,-4)

print "The numerical results converge to 1 as delta goes smaller" 
print "i.e results get more precise to the analytical result as delta gets smaller"

#plotting
plt.figure(figsize = (15,4))
plt.clf()
plt.plot(dellog, de(1,dellog))
plt.ylabel("value of derivative")
plt.xlabel("log-spaced value of $delta$, actual value is 10 to the 'label'")
plt.title("Value of Derivative at x=1 for f=x(x-1) for Different $delta$")
plt.show()

