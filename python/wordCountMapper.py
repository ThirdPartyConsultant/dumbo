#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys
import random
import string

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    flagFile = open("/tmp/show/"+UID,"a")
    flagFile.write(""+UID+"\n")
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
            print '%s%s%d' % (word, separator, 1)


UID = id_generator() 
if __name__ == "__main__":
    main()



