import csv

path = 'pairs/'
ext  = '.txt'

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

# load all users from a csv file
def undo(people):
  names = ''
  for person in people:
    with open(getFileName(person), 'r') as f:
      names = f.read().split('\n')[:-2]
      names.append('')
      names = '\n'.join(names)
    writeFile(getFileName(person), names)

## HELPERS ##

# generate the file name for a particular user
def getFileName(a):
  return path + a['first'] + a['last'] + ext

# write s to a file: overwrites existing file
def writeFile(filename, s):
  with open(filename, 'w') as f:
    f.write(s)

## MAIN ##

def main():
  people = load_people('active.csv')
  undo(people)

if __name__ == "__main__":
  main()
