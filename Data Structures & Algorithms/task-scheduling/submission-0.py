class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        freq_list = list(freq.values())
        neg_freq_list = [item * (-1) for item in freq_list]
        heapq.heapify(neg_freq_list)
        
        queue = deque()
        while neg_freq_list or queue:
            time += 1
            while queue and time >= queue[0][1]:
                heapq.heappush(neg_freq_list, queue[0][0])
                queue.popleft()
            if neg_freq_list:
                freq_item = heapq.heappop(neg_freq_list)
                if freq_item+1 < 0:
                    queue.append([freq_item + 1, time + n + 1])
            else:
                continue
        return time
