import csv
import sys

def read_dna(dna_filename):

    """
    Reads the DNA file

    This function reads the DNA sequence from the given 'dna_filename' file.
    It returns the DNA sequence read from the file as a string.

    Parameters:
        dna_filename                The DNA file name

    Returns:
        str                         A string that is the DNA sequence read from the file.
    """

    # Reference: https://www.pythontutorial.net/python-basics/python-read-text-file/

    with open(dna_filename, 'r') as dna_file:
        contents = dna_file.read()
        dna_file.close()
        return contents


def dna_length(dna_filename):

    """
    Returns the length of a DNA sequence in the file 'dna_filename'

    Parameters:
        dna_filename                The DNA file name

    Returns:
        int                         An integer length of the DNA sequence
    """

    # Reference: https://www.pythontutorial.net/python-basics/python-read-text-file/

    return len(read_dna(dna_filename))


def read_strs(str_filename):

    """
    Reads the STRs from the given 'str_filename' file

    The STR file is a CSV file containing STR repeats for certain people.
    An example of this file looks like this:

        name, AGAT, AATG, TATC
        Alice, 5, 2, 8
        Bob, 3, 7, 4
        Charlie, 6, 1, 5

    This function must read the file using the 'csv' module and return a list of dictionary objects that look like this:

        [
            {'name': 'Alice', 'AGAT': 5, 'AATG': 2, 'TATC': 8},
            {'name': 'Bob', 'AGAT': 3, 'AATG': 7, 'TATC': 4},
            {'name': 'Charlie', 'AGAT': 6, 'AATG': 1, 'TATC': 5}
        ]

    Parameters:
        str_filename                The STR file name

    Returns:
        list of dicts               A list of dictionary objects read from the CSV file
    """

    # Reference: https://www.pythonforbeginners.com/basics/read-csv-into-list-of-dictionaries-in-python

    with open(str_filename, 'r') as str_file:
        contents = csv.DictReader(str_file)
        list_of_dict = list()
        
        for row in contents:
            list_of_dict.append(row)
        
        return(list_of_dict)


def get_strs(str_profile):

    """
    Returns a tuple of (STR, repeats) pairs

    Given a dictionary representation of an STR profile that looks like this:

        {'name': 'Alice', 'AGAT': 5, 'AATG': 2, 'TATC': 8}
    
    Return a list of tuples that looks like this:

        [('AGAT', 5), ('AATG', 2), ('TATC', 8)]

    Note: the repeat is an 'int', not a 'string'.

    Parameters:
        str_profile                 A STR profile in dictionary form

    Return:
        list of tuples              A list of (STR, repeats) pairs
    """

    # Reference: https://datagy.io/python-dictionary-to-list-of-tuples/

    list_of_tuple = list()

    for key in str_profile:

        # Reference: https://www.geeksforgeeks.org/python-string-isalpha-method/

        if str_profile.get(key).isalpha():
            list_of_tuple.append((key, str_profile.get(key)))
        else:
            list_of_tuple.append((key, int(str_profile.get(key))))
    
    del list_of_tuple[0]
    return(list_of_tuple)


def longest_str_repeat_count(str_frag, dna_seq):
    """
    Finds the longest match of a given STR DNA fragment in the given
    DNA sequence.
 
    This function returns the longest repeated occurance of the given
    STR fragment, `str_frag`, in the DNA sequence `dna_seq`. For
    example, given the STR AGAT and the DNA sequence:
 
    AGACGGGTTACCATGACTATCTATCTATCTATCTATCTATCTATCTATCACGTACGTACGTA
    TCGAGATAGATAGATAGATAGATCCTCGACTTCGATCGCAATGAATGCCAATAGACAAAA
 
    this function returns 5.
 
    Hints:
 
    1. You will want to loop over the `dna_seq` character by
      character using a while loop with an index
    2. You may find using string slicing convenient for this
      function. For example, `dna_seq[i:i+4]` will evaluate to a
      substring of `dna_seq` starting from i to i+4 exclusive.
    3. Do not use the `count` string method. It doesn't return the
      longest match, it returns the count. This would also be
      cheating.
 
    Parameters:
        str_frag     A fragment of DNA in a STR profile (e.g., AGAT)
        dna_seq      A DNA sequence
 
    Returns:
        int          The longest repeated occurance of the STR fragment
    """

    i = 0
    repeat = 1
    max_repeat = 0

    while i < len(dna_seq):
        if dna_seq[i:i+4] == str_frag:
            prev = dna_seq[i:i+4]
            temp = dna_seq[i+4:i+8]
            if prev == temp:
                repeat += 1
            elif max_repeat < repeat:
                max_repeat = repeat
                repeat = 1
            i += 4            
        else:
            i += 1
   
    return max_repeat 

def find_match(str_profile, dna_seq):

    """
    Find a match given a specific STR profile
 
    This function compares the repeat values for each STR dna fragment
    X in the given `str_profile` to the count of that same X dna
    fragment in the provided DNA sequence `dna_seq`.
 
    For example, if we have a profile like this (a list of tuples):
 
    [('AGAT', 5), ('AATG', 2), ('TATC', 8)]
 
    We want to determine if the number of repeats for the STR
    fragments AGAT, AATG, and TATC for this profile, which is 5, 2,
    and 8, are the same number of repeats in the DNA sequence. If the
    repeat count in the DNA sequence for AGAT, AATG, and TATC are
    identical to this profile, then we have matched the profile to the
    DNA sequence.
 
    Hints:
 
    1. You want to use the `longest_str_repeat_count` function to
    find the longest count of repeats for each STR fragment in
    the DNA sequence. This will require you to iterate over the
    `str_profile` list.
 
    Parameters:
        str_profile  A list of tuples representing a person's STR
                  profile
 
    Returns:
        boolean      `True` if a match is found; `False` otherwise
    """
    temp = False

    if str_profile[0][1] == longest_str_repeat_count('AGAT', dna_seq) and str_profile[1][1] == longest_str_repeat_count('AATG', dna_seq) and str_profile[2][1] == longest_str_repeat_count('TATC', dna_seq):
        temp = True
   
    return temp

def dna_match(str_filename, dna_filename):
    """
    Compares STRs to a DNA sequence
 
    This function reads the STRs in the `str_filename` file
    and the DNA sequence in the `dna_filename` file and compares
    the STRs to the DNA sequence to determine who the DNA sequence
    likely belongs to.
 
    Parameters:
        str_filename      The STR file name
        dna_filename      The DNA file name
 
    Returns:
        str               A string that is either the person's name in the STR file
                          that matches the DNA sequence in the DNA file or
                          'No match' if a match does not exist.
    """
    str = read_strs(str_filename)
    dna = read_dna(dna_filename)

    if find_match(get_strs(str[0]), dna) == True:
        return str[0]['name']
    elif find_match(get_strs(str[1]), dna) == True:
        return str[1]['name']
    elif find_match(get_strs(str[2]), dna) == True:
        return str[2]['name']
    else:
        return 'No match'

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python dna.py STR_FILE DNA_FILE')
    else:
        temp1 = sys.argv[1] 
        temp2 = sys.argv[2]
        print(dna_match(temp1, temp2))
    

    
