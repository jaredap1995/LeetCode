def solution(words):
    n = len(words)
    if len(words) == 1:
        return True
    
    #Create frequency array to store the frequency of each letter
    freq = [0]*26

    for word in words:
        for char in word:
            # Use unicode representation of chrachter and add its appearance to array
            freq[ord(char)-ord('a')] += 1

    for val in freq:
        # If the value in frequency divided by n has a remainder ==> there is a charachter that cannot be evenly distributed
        if val % n != 0: return False
    
    return True
    
