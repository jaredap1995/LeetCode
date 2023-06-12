"""Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory."""


Input = ["h","e","l","l","o"]
Output=["o","l","l","e","h"]

def reverseString(s):
    i=0
    j=len(s)-1
    while i < j:
        temp=s[i]
        s[i]=s[j]
        s[j]=temp
        i+=1
        j-=1
    return s

print(reverseString(Input))


def reverseString_incorrect(s):
    i=0
    j=-1
    length=len(s)
    while i < length:
        s[i]=s[j]
        i+=1
        j-=1
    return s


"""My original answer above was close, but the problem with my original approach was that as soon as we got to the 
middle of teh string we had already replaced the beginning of the string, meaning we could not fully 
reverse it.


In the correct answer we do something very similar, however instead of using negative indexing we use
positive indexing (to avoid replacing values that have alreayd been replaced) and we also use
a temp variable that stores the inital value of letter so we can swap it correctly later on."""
