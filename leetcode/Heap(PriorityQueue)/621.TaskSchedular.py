
#* 621. Task Schedular - MEDIUM

'''
You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

Return the minimum number of CPU cycles required to complete all tasks.

#? Example 1:

Input: tasks = ["X","X","Y","Y"], n = 2
Output: 5
Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

#? Example 2:

Input: tasks = ["A","A","A","B","C"], n = 3
Output: 9
Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

'''

from collections import deque
from typing import Counter, List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #* Aproach 1: MaxHeap implementation with counts of Each task
        #* Time: O(m), m = no. of tasks | O(1) since 26 alphabets
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time


        #* Aproach 2: Using English alphabets and alphanumeric values
        #* Time: O(n) | Space: O(1) 
        ##* WAY Faster on Leetcode
        # counts = [0] * 26
        # for task in tasks:
        #     counts[ord(task) - ord('A')] += 1
        
        # maxVal = max(counts)
        # maxCount = counts.count(maxVal)

        # return max(((maxVal - 1) * (n + 1)) + maxCount,len(tasks))
