import sys

def make_frequency_dict(text):
    frequency = {}
    for character in text:
        if not character in frequency:
            frequency[character] = 0
        frequency[character] += 1
    return frequency

def sortFreq (freqs) :
    letters = freqs.keys()
    tuples = []
    for let in letters :
        tuples.append((freqs[let],let))
    tuples.sort()
    return tuples

def buildTree(tuples) :
    while len(tuples) > 1 :
        leastTwo = tuple(tuples[0:2])                  # get the 2 to combine
        theRest  = tuples[2:]                          # all the others
        combFreq = leastTwo[0][0] + leastTwo[1][0]     # the branch points freq
        tuples   = theRest + [(combFreq,leastTwo)]     # add branch point to the end
        # tuples.sort()                                  # sort it into place
    return tuples[0]            # Return the single tree inside the list

def trimTree (tree) :
    # Trim the freq counters off, leaving just the letters
    p = tree[1]                                    # ignore freq count in [0]
    if type(p) == type("") : return p              # if just a leaf, return it
    else : return (trimTree(p[0]), trimTree(p[1])) # trim left then right and recombine

def assignCodes (node, pat='') :
    global codes
    if type(node) == type("") :
        codes[node] = pat                # A leaf. set its code
    else  :                              #
        assignCodes(node[0], pat+"0")    # Branch point. Do the left branch
        assignCodes(node[1], pat+"1")    # then do the right branch.

def huffman_encoding(data):
    freqDict = make_frequency_dict(data)
    # print("frequency:", freqDict)

    # sorted_d = sorted(freqDict.items(), key=lambda x: x[1], reverse=True)
    # print("sorted_d:", sorted_d)

    freq = sortFreq(freqDict)
    # print("freq:",freq)

    tree = buildTree(freq)
    # print("tree:", tree)

    tt = trimTree(tree)
    # print("tt:", tt)

    assignCodes(tt)
    # print("code:", codes)

    output = ""
    for ch in data : output += codes[ch]
    # print("output:", output)

    return output, tt

def huffman_decoding(data,tree):
    output = ""
    p = tree
    for bit in data :
        if bit == '0' : p = p[0]     # Head up the left branch
        else          : p = p[1]     # or up the right branch
        if type(p) == type("") :
            output += p              # found a character. Add to output
            p = tree                 # and restart for next character
    return output




if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))