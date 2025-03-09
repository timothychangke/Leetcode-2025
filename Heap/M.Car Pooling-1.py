class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        travels = []
        p = 0
        for i in range(len(trips)):
            travels.append([trips[i][1], trips[i][0]])
            travels.append([trips[i][2], -trips[i][0]])
        travels.sort()
        print(travels)
        for t in travels:
           p += t[1]
           if p > capacity: return False
        return True
    
    """ 
    class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Find the maximum end location to size our array properly
        arr = [0] * (max(trip[2] for trip in trips) + 1)

        # Mark passenger pick-ups and drop-offs
        for (value, left, right) in trips:
            arr[left] += value   # Pick up passengers
            arr[right] -= value  # Drop off passengers

        # Running sum to track capacity usage
        curr = 0
        for i in range(len(arr)):
            curr += arr[i]
            if curr > capacity:
                return False

        return True

    """