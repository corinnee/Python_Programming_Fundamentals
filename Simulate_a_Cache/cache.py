import math
import array
##  07/04/2020 cache.py by Corinne Batho-Newton ( cb830 )
##  This program reads text file and simulates a cache with LRU
##  replacement to the details and inputs given.


##  - Cache(note_array) takes the input of the text file as an array and
##    simulates the cache, printing the index and tag of the address 
##    currently being processed.
def Cache(note_array):

##    define cache description values
    info = note_array[0].split(' ')

    w = int(info[0])                    # the number of bits in one word.
    c = int(info[1])                    # the number of data bytes in the cache.
    b = int(info[2])                    # the number of bytes in one cache block.
    k = int(info[3].replace('\n',''))   # the number of lines in a block

    noOfBlocks = c/b                    # the number of blocks in the cache
    indexBits = math.log(noOfBlocks,2)  # the number of index bits
    lineBytes = b/k                     # number of bytes in a line
    offsetBits = math.log(lineBytes,2)  # number of offset bits
    length = len(note_array)

##  converts all addresses to binary and adds them to a list.
    binaryList = []
    i = 1
    while i < length :
        binary = bin(int(note_array[i]))
        binaryList.append(binary)
        i+= 1

##  Initialises the cache and it's blocks, filling all empty lines in
##  block with 'e'.
    cache = []
    output = ''
    i = 0
    while i < noOfBlocks:
        cache.append([i])
        l = 0
        while l <= k:
            cache[i].append('e')
            l+= 1
        i+= 1

##  - Each address in binary list added to the cache with LRU replacement.
    for binary in binaryList:

##      remove offset bits.
        if offsetBits != 0:
            binary = bin(int(binary,2) >> int(offsetBits))

##      determine int value of index
        if indexBits == 0:
            index = 0
        else:
            x = (binary[-int(indexBits):]).replace('b','0')
            index = int(x,2)
            
        tag = int(binary,2) >> int(indexBits)   ## determines in value of tag
        block = cache[index]                    ## gets current block from cache
        print('index: ', index, ' tag: ', tag)

        line = findInBlock(block,tag,cache)     ## gets position of tag in block if present

##      - if not in block, add 'M' to output then add tag to first empty line
##        in block or to end of the block, removing the first tag in block.
        if line == 0:
            output += 'M'
            firstEmptyLine = findFirstEmpty(block)
            if firstEmptyLine == 0:
                del block[1]
                block.append(tag)
            else:
                block[firstEmptyLine] = tag

##      - if tag is in block, add 'C' to output, then remove from block and add
##        to the first empty line, or the end of the block.
        else:
            output += 'C'
            firstEmptyLine = findFirstEmpty(block)
            if firstEmptyLine == 0:
                del block[line]
                block.append(tag)
            else:
                del block[line]
                block[firstEmptyLine-1] = tag
                block.append('e')

    print("Output :", output)

                
##  - findFirstEmpty(block)
##    finds the first empty line in the block given. Returns index of
##    first 'e' in block or 0 if there are no empty lines.      
def findFirstEmpty(block):
    i = 0
    found = False
    while i < len(block) and found == False:
        if block[i] == 'e':
            found = True
        else:
            i += 1
    if found == True:
        return i
    else:
        return 0


##  - findInBlock(block,tag,cache)
##    finds the tag in the block, returning index of it's position if
##    present, or 0 if it is not present.
def findInBlock(block,tag,cache):
    i = 1
    found = False
    while i < len(block) and found == False:
        if block[i] == tag:
            found = True
        else:
            i += 1
    if found == True:
        return i
    else:
        return 0


##  - ReadFile(filename)
##    Returns contents of file as an array.
def ReadFile(filename):
    file = open(filename, "r")
    note_array = []
    for line in file:
        note_array.append(line)    
    file.close()
    return note_array

def Main():
    filename = input("Enter file name: ")
    note_array = ReadFile(filename)
    Cache(note_array)
    again = input("Run again? (y/n): ")
    if again == 'y':
        Main()
    elif again != 'n':
        Main()
Main()
