import matplotlib.pyplot as plt
import numpy as np

#this part is for defining useful functions
#defining factorial function
def fac(x):
#the "if"  and "else" are for excluding incorrect input
	if (type(x)==int) and (x >= 0):
		i = 1
#while loop is the calculating part
		while x > 1:
			i = x * i
			x = x - 1
		return i
	else:
		return "Please type in positive integer."

#defining binomial coefficient function with fac(x)
def bincoe(n,k):
#the "if"  and "else" are for excluding incorrect input
	if n >= k >= 0:
		bin = (fac(n) / (fac(k) * fac(n-k)))
		return bin
	else:
		return 0


#below is for part a
print "Part a--Binomial Coefficient: "
print " "

#let users be able to input n and k to calculate binomial coeff
N = input('enter number for n: ')
K = input('enter number for k: ')

#return the final value
print "the binomial coefficient is: ", bincoe(N,K)


#below is for part b
print " "
print " "
print "Part b--Pascal's triangle: "
print " "
raw_input("Press Enter to continue...")

#this function is for obtaining the nth row of Pascal's triangle
def pastri(nthrow):
#creating an empty list and then insert coefficients of
#Pascal's triangle into the list in order
	row = []
	for i in range(0,nthrow+1):
		row.append(bincoe(nthrow,i))
	return row

print "The first 20 lines of the Pascal's triangle are:"
print " "

#print out first 20 lines line by line with pastri()
for k in range(0,20):
	print pastri(k)

print " "
print " "

#below is for part c
print "Part c: "
print " "


#defining the probability function with respect to p, n, k
def prob(p,n,k):
	return ((bincoe(n,k)) * (p**k) * ((1 - p)**(n-k)))

#inputing the p, n, k that we want to use
P = input("entering for the probability of obtaining head: ")
cN = input("entering for the number of total flips: ")
cK = input("entering for the least number of times that you want to get for head: ")

#getting theoretical value by inputs in part c for part d
#for from n times to get exactly k result, given by prob()
#for at least, need to
a = 0
value = 0.

#add up all the probabilities for getting less than k from n flips
while a < cK:
	value = value + prob(P,cN,a)
	a = a + 1
#another equivalent way to get probability, just for checking
b=cK
sum_suc = 0.
while b < cN + 1:
	sum_suc = sum_suc + prob(P,cN,b)
	b = b+1

#use 1 - value can obtian the probability of the case "at least k"
theo = 1 - value


#"if" and "else" are for excluding physically impossible inputs
#eg. in this case probability is smaller than 1 and greater 0
if (cN>=cK) and (1>P>0):

#printing the results
	print "The probability of obtaining heads at least", cK, "times"
	print "in", cN, "flips is: ", theo

else:
	print "Sorry, you input the wrong values"


#below is for part d
print " "
print " "
print "Part d: "
raw_input("Press Enter to continue...")
print "note that when theoretical probability gets very small, the "
print "simulation result may not converge to theoretical value."
print "this is due to the trial times N is probably too small"
print "plotting..."

#defining function that simulate the fliping coin for N times
def simcoin(N):
#initialize varibles for storing number of head that got in flips
	numhead = 0
	numsuc = 0
#k and i is the factor for counting in while loops	
	k = 0
	i = 0
	while k < N:
		while i < cN: 
#use random.random() to simulate fliping
#collecting results by adding up numhead one by one
			if np.random.random() < P: 
				numhead += 1
#update i for counting times of fliping	
			i = i + 1
		if numhead >= cK:
			numsuc += 1.0
		k = k + 1
		numhead = 0 #reset the number of getting head
		i = 0 #ready for next flip
#after while loop, counting number of heads in the list and
#getting the fraction of simulation that are successful in
#obtaining the least number of heads
	return numsuc / N

#simulate for N=10, store the result
fracsuc10 = simcoin(10)
#one for N=1000 
fracsuc10000 = simcoin(10000)
#one for N=100000
fracsuc1000000 = simcoin(1000000)

#creating a list containing the probability obtain above
simfrac = [fracsuc10,fracsuc10000,fracsuc1000000]
thefrac = [theo]

#setting up for the bar plot
fig = plt.figure()
ax = fig.add_subplot(111)
barwidth = 0.3

#creating bar for fraction of simulation
simbar = plt.bar(np.arange(3), simfrac, barwidth, \
                 color='b', label = "simulation probability")
thebar = plt.bar(3, thefrac, barwidth, \
                 color='r', label = "theoretical probability")

#making legends of the plot
plt.title("Probability of Simulation vs. Theoretical Prediction")
plt.xticks(np.arange(3)+barwidth/2, ["10","10000","1000000","theoretical"])
plt.ylabel("probability")
plt.xlabel("value of N(number of times of simulation)")
plt.legend()
ax.axhline(theo, color="red") #make a horizontal line with same hight as theo

plt.show()
