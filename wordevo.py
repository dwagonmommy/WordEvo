import random
import sys
optimal = "Computer Science is awesome"
i = 1
while i < len(sys.argv):
    optimal = optimal + sys.argv[i] + " "
    i+= 1
print optimal
popsize = len(optimal)**2
popsize = popsize / 2
if popsize % 2 ==1 :
    popsize = popsize + 1
if popsize > 1000:
    popsize = 800
if popsize < 4:
    popsize = 4
print "popsize",popsize
dnasize = len(optimal)
mutatechance = 1



def fitness(word):
    fitness = 0
    for x in xrange(len(optimal)):
        fitness += abs(ord(optimal[x]) - ord(word[x]))
    return fitness

def sortfit(x):
    return fitness(x)

def choice(pop):
    ret = int(popsize*.2)
    parents = pop[:ret]
    random_select = .05
    for i in pop:
        if random_select > random.random():
            parents.append(i)
    parent_len=len(parents)
    m = random.randint(0,parent_len-1)
    return parents[m]

def mutate(indv):
    temp = list(indv)
    for i in xrange(len(indv)):
        n = random.randint(0,100)
        if n < mutatechance:
            temp[i] = chr(random.randint(32,126))
    indv = "".join(temp)
    return indv

def crossover(ind1,ind2):
    return ind1[:(dnasize/2)] + ind2[dnasize/2:] , ind2[:dnasize/2] + ind1[dnasize/2:]
        


population = []
for i in xrange(popsize):
    word = ""
    for x in xrange(dnasize):
        m = random.randint(32,126)
        word += chr(m)
    population.append(word)

population = sorted(population,key=sortfit)
g = 0

while population[0] != optimal:
    newp = []
    for i in xrange(popsize/2):
        ind1 = choice(population)
        ind2 = choice(population)
        ind1,ind2 = crossover(ind1,ind2)
        ind1 = mutate(ind1)
        ind2 = mutate(ind2)
        newp.append(ind1)
        newp.append(ind2)
    population = newp
    population = sorted(population,key=sortfit)
    g += 1
    print population[0]
print population[0]