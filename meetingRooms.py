# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1
import heapq
def minMeetingRooms(self, intervals:):
    intervals.sort(key=lambda x: x[0])
    minRooms = 0
    heap = []
    for itv in intervals:
        while heap and heap[0] <= itv[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, itv[1])
        minRooms = max(minRooms, len(heap))
    return minRooms
