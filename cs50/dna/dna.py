import csv, sys


def main():

    # TODO: Check for command-line usage
    if (len(sys.argv) != 3):
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    dna = []

    # TODO: Read database file into a variable
    with open(sys.argv[1], mode='r') as database:
        reader = csv.reader(database)
        dna = list(reader)


    # TODO: Read DNA sequence file into a variable
    sequence = open(sys.argv[2]).read()
    matches = []

    # TODO: Find longest match of each STR in DNA sequence
    for i in range(1, len(dna[0])):
        matches.append(longest_match(sequence, dna[0][i]))

    # TODO: Check database for matching profiles
    suspect = 'No Match'
    suspect_counter = 0

    for i in range(1, len(dna)):
        for j in range(len(matches)):
            if matches[j] == int(dna[i][j+1]):
                suspect_counter += 1

        if suspect_counter == len(matches):
            suspect = dna[i][0]
            break
        else:
            suspect_counter = 0
    print(suspect)
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
