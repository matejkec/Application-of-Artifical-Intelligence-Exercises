import random 
import datetime 
import codecs

# Definiranje recenice koju zelimo pogoditi, zapisana je u datoteci "Ia_3_text.txt"
with codecs.open("aoai_4_text.txt", 'r', encoding='utf8') as f:
    target = f.read()
    
# Definiranje genetskog skupa, odnosno svih slova i znakova od kojih se može sastojat recenica
geneSet = ''.join(sorted(set(target + " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.")))
    
# Funkcija za stvaranje člana populacije
def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet,sampleSize))
        print(''.join(genes))
    return ''.join(genes) 

# Funkcija koja ocjenjuje vrijednost člana populacije
def get_fitness(guess):
    return sum(1 for expected, actual in zip(target,guess)\
               if expected == actual)

# Funkcija za mutaciju člana populacije
def mutate(parent): 
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == \
    childGenes[index] else newGene 
    return ''.join(childGenes)

# Funckija za prikaz rezultata
def display(guess): 
    timeDiff = datetime.datetime.now() - startTime 
    fitness = get_fitness(guess)
    print("{} \t {} \t {}".format(guess, fitness,\
          timeDiff))

# Algoritam
random.seed()
startTime = datetime.datetime.now()
bestParent = generate_parent(len(target))
bestFitness = get_fitness(bestParent)
while True: 
    child = mutate(bestParent)
    childFitness = get_fitness(child)
    if bestFitness >= childFitness: 
        continue 
    if childFitness >= len(bestParent):
        break 
    bestFitness = childFitness 
    bestParent = child
 
# Prikaz rezultata
display(child)