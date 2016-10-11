import csv
import random

def load_people(filename):
  with open(filename, 'rb') as csvfile:
    f = csv.reader(csvfile, delimiter=',', quotechar='|')
    people = []
    for row in f:
      # skip header row
      if row[0] in ['First', 'Last', 'Dept']:
        continue
      person = {
        'name': row[0] + ' ' + row[1],
        'first': row[0],
        'last': row[1],
        'department': row[2]
      }
      people.append(person)
  return people

def pair(l):
  pairings = []
  while len(l) > 1:
    a = random.choice(l)
    l.remove(a)
    b = random.choice(l)
    l.remove(b)
    pairings.append(a['name'] + " and " + b['name'])
  return pairings

def printList(l):
  for v in l:
    print v


def main():
  # generate list of active people
  print 'Generating...'
  people = load_people('active.csv')

  # generate list of active people
  print 'Pairing...'
  pairs = pair(people)

  # print
  printList(pairs)
  print 'Enjoy!'

if __name__ == "__main__":
  main()
