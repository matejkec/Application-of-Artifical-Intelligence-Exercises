import random 
import datetime 

numbers = [1,2,3,4,5,6,7,8,9]
operations = ['+', '-']
expectedTotal = 23 
optimalLengthSolution = [4, '+', 3, '-', 2, '+', 8, '+', 7, '+', 4, '-', 1]
minNumbers = (1 + len(optimalLengthSolution)) / 2
#print("minNumbers = " + str(minNumbers))
maxNumbers = 8 * minNumbers 
#print("maxNumbers = " + str(maxNumbers))
startTime = datetime.datetime.now()
#Heart of the genetic programming is the evaluate function
def create(numbers, operations, minNumbers, maxNumbers):
    genes = [random.choice(numbers)]
    #print("genes = " + str(genes))
    count = random.randint(minNumbers, 1 + maxNumbers)
    #print("choice = " + str(count))
    while count > 1: 
        count -= 1
        genes.append(random.choice(operations))
        genes.append(random.choice(numbers))
    return genes

def evaluate(genes):
    result = genes[0]
    #print("result = " + str(result))
    for i in range(1, len(genes),2):
        operation = genes[i]
#        print("operation = " + str(operation))
        nextValue = genes[i+1]
#        print("nextValue = " + str(nextValue))
        if operation == '+':
            result += nextValue 
#            print("result += nextValue = " + str(result))
        elif operation == '-':
            result -= nextValue 
#            print("result -= nextValue = " + str(result))
    return result

def get_fitness(genes, expectedTotal):
    result = evaluate(genes)
    print("result = " + str(result))
    if result != expectedTotal: 
        fitness = expectedTotal - abs(result - expectedTotal)
        print("fitness = " + str(fitness))
    else: 
        fitness = 1000 - len(genes)
        print("fitness = " + str(fitness))
    return fitness

def mutate(genes,numbers, operations, minNumbers, maxNumbers):
    numberCount = (1 + len(genes))/2
#    print("numberCount = " + str(numberCount))
    appending = numberCount < maxNumbers and random.randint(0,100) == 0
#    print("appending = " + str(appending))
    if appending: 
        genes.append(random.choice(operations))
        genes.append(random.choice(numbers))
#        print("genesappending = " + str(genes))
        return genes
    removing = numberCount > minNumbers and random.randint(0,20) == 0
#    print("removing = " + str(removing))
    if removing: 
        index = random.randrange(0, len(genes) - 1)
        del genes[index]
        del genes[index]
        print("genesremoving = " + str(genes))
        return genes
    index = random.randrange(0, len(genes))
 #   print("index = " +str(index))
 #   print("genes[indexold] = " + (str(genes[index])))
    genes[index] = random.choice(operations) if (index & 1) == 1 else random.choice(numbers)
 #   print("genes[indexnew]  = " + str(genes[index]))
 #   print("genesmutateing = " + str(genes))
    return genes

def display(candidate,fitness, startTime):
    timeDiff = datetime.datetime.now() - startTime 
    print("{0}\t{1}\t{2}".format(
            ''.join(map(str,candidate)),
            fitness,
            timeDiff))
    
bestParent = create(numbers, operations, minNumbers, maxNumbers)
print("bestParent = " + str(bestParent))
evalParent = evaluate(bestParent)
print("evalParent = " + str(evalParent))
parentFitness = get_fitness(bestParent, expectedTotal)
print("parentFitness = " + str(parentFitness))
display(bestParent, parentFitness, startTime)

while True: 
    child = mutate(bestParent, numbers, operations, minNumbers, maxNumbers)
    print("child = " + str(child))
    evalChild = evaluate(child)
    childFitness = get_fitness(child, expectedTotal)
    display(child, childFitness, startTime)
    if evalChild == expectedTotal:
        break
    bestParent = child  