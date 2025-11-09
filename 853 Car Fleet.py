class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = zip(position, speed)
        combined = sorted(combined)
        a, b =  zip(*combined)
        position = list(a)
        speed = list(b)
        
        time = [0] * len(position) #time is how long it takes to get there
        for i in range(len(time)):
            time[i] = (target - position[i]) / speed[i] 
        #use time as a stack to manipulate the order
        slowest = 0 #longest time to travel
        fleets = 0
        while len(time) > 0:
            curr = time.pop()
            if(slowest < curr): #new slowest 
                fleets = fleets + 1
                slowest = curr
        return fleets
