from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ===== Brute force solution O(n2) ====== ##
        # results = [0] * len(temperatures)


        # # [73,74,75,71,69,72,76,73]
        # for i in range(0, len(temperatures) - 1):
        #     for j in range(i + 1, len(temperatures)):
        #         # paisi
        #         if temperatures[j] > temperatures[i]:
        #             results[i] = j - i
        #             break

        # return results


        # ===== LINEAR TIME O(n) solution but EXTRA MEMORY O(n) ====== ##
        results = [0] * len(temperatures)
        stack = [] # pair(temp, index)

        for i, t in enumerate(temperatures):
            # while stack !empty and current temp is greater than stack top temp
            while stack and t > stack[-1][0]:
                # get the top pair
                stackT, stackInd = stack.pop()
                results[stackInd] = i - stackInd

            stack.append((t, i))

        return results

if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))

