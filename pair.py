import csv
import random

path     = 'pairs/'
ext      = '.txt'
maxLines = 10

## LOAD ##

# load all users from a csv file
def load_people(filename):
  with open(filename, 'rb') as csvfile:
    f = csv.reader(csvfile, delimiter=',', quotechar='|')
    people = []
    for row in f:
      # skip header row
      if row[0] in ['First', 'Last', 'Dept']:
        continue

      # create person
      person = {
        'name'      : row[0] + ' ' + row[1],
        'first'     : row[0],
        'last'      : row[1],
        'department': row[2]
      }
      # add person to our list of people
      people.append(person)
  return people

## PAIR ##

# pair all users in a list
def pairAll(l):
  pairings = []

  while len(l) > 1:
    # choose random pairs
    a = random.choice(l)
    l.remove(a)
    b = random.choice(l)
    l.remove(b)

    # if this pairing has been matched recently
    while hasPaired(a,b):
      # choose someone new
      c = random.choice(l)
      l.remove(c)
      # put back other person
      l.append(b)
      b = c

    # save and add the pair to our list
    savePair(a, b)
    pairings.append(a['name'] + ' and ' + b['name'])

  return pairings

# check if two people have already been paired
def hasPaired(a, b):
  afile = getFileName(a)
  return isInFile(afile, b['name'])

def isSameDept(a, b):
  return a['department'] == b['department']

# save each name in respective files
def savePair(a, b):
  afile = getFileName(a)
  bfile = getFileName(b)

  # write or append to respective files
  if fileLongerThan(afile, maxLines):
    writeFile(afile, b['name'] + '\n')
  else:
    appendToFile(afile, b['name'] + '\n')

  if fileLongerThan(bfile, maxLines):
    writeFile(bfile, a['name'] + '\n')
  else:
    appendToFile(bfile, a['name'] + '\n')


## HELPERS ##

# generate the file name for a particular user
def getFileName(a):
  return path + a['first'] + a['last'] + ext

# check if a file is longer than a specified length n
def fileLongerThan(filename, n):
  try:
    lines = sum(1 for line in open(filename))
    if lines > n:
      return True  # more than N lines in the file
    return False  # less than N lines in the file
  except:
    return False  # file not found

# append s to a file
def appendToFile(filename, s):
  with open(filename, 'a') as f:
    f.write(s)

# write s to a file: overwrites existing file
def writeFile(filename, s):
  with open(filename, 'w') as f:
    f.write(s)

# check if s is in a file
def isInFile(filename, s):
  try:
    with open(filename, 'r') as f:
      data = f.read()
      if s in data:
        return True  # s is in data
      return False  # is not in data
  except:
    return False  # file doesn't exist

# print a list of items
def printList(l):
  for v in l:
    print v


## MAIN ##

def main():
  # generate list of active people
  print 'Generating...'
  people = load_people('active.csv')

  # generate list of active people
  print 'Pairing...'
  pairs = pairAll(people)

  # print
  printList(pairs)
  print 'Enjoy!'

if __name__ == "__main__":
  main()
