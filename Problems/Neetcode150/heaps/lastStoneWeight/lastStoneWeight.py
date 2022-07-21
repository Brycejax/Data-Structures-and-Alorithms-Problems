class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heap = []
        for i in stones:
            heap.append(i * -1)
        
        heapq.heapify(heap)
        
        while len(heap) > 1:
            rock1 = heapq.heappop(heap) * -1 #y
            rock2 = heapq.heappop(heap) * -1 #x
            
            if rock2 != rock1:
                rock1 -= rock2
                heapq.heappush(heap, rock1 * -1)
                    
        return heap[0] * -1 if heap else  0