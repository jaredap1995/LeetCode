"""
Design a time-based key-value data structure that can store multiple values 
for the same key at different time stamps and retrieve the key's value at 
a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with 
the value value at the given time timestamp.

String get(String key, int timestamp) 
Returns a value such that set was called previously, 
with timestamp_prev <= timestamp. If there are multiple such values, 
it returns the value associated with the largest timestamp_prev.
 If there are no values, it returns "".

"""

from collections import defaultdict
import bisect

class TimeMap(object):
    def __init__(self):
        self.data=defaultdict(list)

    def set(self, key, value, timestamp):
        self.data[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.data:
            return ""
        
        tuples=self.data[key]
        i=bisect.bisect(tuples, (timestamp, chr(127)))

        if i==0:
            return ""
        else: 
            return tuples[i-1][1]
    
obj=TimeMap()
print(obj)
obj.set("foo", "bar", 1)
param_2=obj.get('foo', 3)
print(param_2)

"""
This seems tricky when you first read it but is generally pretty straightforward.
Initialize your TimeMap object with the 'init' funciton by setting the attribute
'self.data=defaultdict(list) '

Then in the set method we simply call the attribute 
'self.data[key].append((Timestamp,value)).' This updates the data attribute with teh new key
and appends the tuple (timestamp,value) to the list.

In teh 'get' method we check if the key is present, if it is not then we return an empty string.
If teh key exists we access it through the data attribute which is the defaultdict,
Then we set the variable i=bisect.bisect(tuples,(timestamp,chr(127))).'

This determines where to place the key based on its timsetamp,
bisect.bisect looks for rightmost placement and take sthe iterable 'tuples' and 
assess where timestamp would go in teh iterable 'tuples' and returns the index it would
go rightmost.

The chr(127) is there in the edge case of two timestamps that are identical, we want
to place the new one to the right side so we add the largest ASCII charachter to ensure
it gets placed to the right.

If i==0 that would mean that we have ran the get method with a timestamp that is 
smaller than one that currently exists within the TimeMap instance so we return an 
empty string.


"""