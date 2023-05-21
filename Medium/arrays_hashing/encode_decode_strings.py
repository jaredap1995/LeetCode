"""Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and 
is decoded back to the original list of strings.

"""

def encode(strs):
    return ''.join('%d:%s' % (len(s), s) for s in strs)
    
str.find

def decode(s):
    strs = []
    i = 0
    while i < len(s):
        j = s.find(':', i)  # Find the next separator
        if j < 0: break
        length = int(s[i:j])
        i = j + 1 + length
        strs.append(s[j+1:i])
    return strs, length
    


strs = ["Hello", "World", 'toot']
test = encode(strs)
result=decode(test)
print(test)
print(result)


"""This is a tougher one for sure. The encoder is straightforward, we use string formatting 
and join to put the strings together on a space with the colon charachter as the joining charachter. 
However, instead of just putting together the words (because that may not work if the join 
charachter is in the string) we actually include the length of the string (len(s)).
%d indiacates that rthe value will be an integer while %s indicates it will be a string.


The decoder creates the list where teh strings will be stored and starts at 0.
j finds the index at which the first seperator charachter exists (index 1 in this example).
If j=-1 (less than 0) we break because it means teh charachter was not found in teh string.
Because in the encoder we passed the len(s) before the word and sep charachter (:), we can find
the length of the first word to be decoded by indexing through the string from the beginning [i]
to the index of the first sep charachter (j). hence the line 'length=int(s[i:j])'.
Now we know the length of the first word (here 5) and we know the sep charachter is 1 
charachter long, so we set 'i' the value of where we start looking for the next string 
equal to 'j+length+1'
"""


