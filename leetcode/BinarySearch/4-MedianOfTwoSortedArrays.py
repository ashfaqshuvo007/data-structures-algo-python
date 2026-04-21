from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O (n + m)
        # mergedArray = nums1 + nums2
        # mergedArray.sort()

        # totalLen = len(mergedArray)

        # if totalLen % 2 == 0:
        #     return (mergedArray[totalLen // 2 - 1] + mergedArray[(totalLen // 2)]) / 2.0
        # else:
        #     return mergedArray[(totalLen // 2)]

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Partitition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # Even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1



if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 3], [2])) # return 2.0
    print(solution.findMedianSortedArrays([1, 2], [3, 4])) # return 2.5

    