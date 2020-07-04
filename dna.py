import csv
import re
import sys

def main():
    if not len(sys.argv) == 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    csv_file = sys.argv[1]
    sequence_file = sys.argv[2]

    dnaDictionary = dict()

    with open(csv_file) as csv_reader:
        csv_reader = csv.reader(csv_reader, delimiter = ',')

        for row in csv_reader:
            dnaToFind = row
            dnaToFind.pop(0)
            break

    with open(sequence_file) as sequence_file_reader:
        sequences = sequence_file_reader.read()

    # Add all the DNA STRs to be find on the dictionary
    for element in dnaToFind:
        dnaDictionary[element] = 0

    # Search for the highest consecutive repetition assuming that there will be no repitition greater than 100
    for keys in dnaDictionary:
        for i in range(100):
            if re.search(keys * i, sequences):
                dnaDictionary[keys] = i

    # Open csv file again to find match
    with open(csv_file) as csv_reader:
        peopleDictionary = csv.DictReader(csv_reader)
        for person in peopleDictionary:
            matches = 0
            for keys in dnaDictionary:
                if dnaDictionary[keys] == int(person[keys]):
                    matches += 1 
            if matches == len(dnaDictionary):
                print(person['name'])
                sys.exit()
        print("No match")






if __name__ == "__main__":
    main()
