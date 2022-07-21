class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for i in points:
            value = abs(((i[0] - 0 ) ** 2 + (i[1] - 0) ** 2))
            heap.append([value, i[0], i[1]])
            
        heapq.heapify(heap)
        
        while len(ans) < k:
            value, x, y = heapq.heappop(heap)
            ans.append([x,y])
            
        return ans