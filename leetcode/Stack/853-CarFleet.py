from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndSpeed = [(p, s) for p, s in zip(position, speed)]
        posAndSpeed.sort(reverse=True)
        result = []
        #? Comments are from first attempt. This is faster and cleaner than the first attempt, which is commented out.
        # print(posAndSpeed)
        # [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]
        #  Target = 12
        for p, s in posAndSpeed:
            time = (target - p) / s
            # result.append((target - p) / s)
            # if len(result) >= 2 and result[-1] <= result[-2]:
            #     result.pop()
            if not result or time > result[-1]:
                result.append(time)
        return len(result)

if __name__ == "__main__":
    solution = Solution()
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    result = solution.carFleet(target, position, speed)
    print(result)
