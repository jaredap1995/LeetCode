"""There are n cars going to the same destination along a one-lane road. 
The destination is target miles away.

You are given two integer array position and speed, 
both of length n, where position[i] is the position of the ith car and speed[i] 
is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, 
but it can catch up to it and drive bumper to bumper at the same speed. 
The faster car will slow down to match the slower car's speed. 
The distance between these two cars is ignored 
(i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. 
Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, 
it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

"""

target = 10
position = [6,8]
speed = [3,2]


class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        print(times)
        ans = 0
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]: ans += 1  # if lead arrives sooner, it can't be caught
            else: times[-1] = lead # else, fleet arrives at later time 'lead'
        return ans + bool(times) # remaining car is fleet (if it exists)

    
print(Solution().carFleet(target, position, speed))




        
