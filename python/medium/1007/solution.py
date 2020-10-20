from collections import Counter
class Solution:
    def minDominoRotations(self, A, B):
        length = len(A)
        countA = Counter(A)
        countB = Counter(B)
        # print('countA',countA)
        # print('countB',countB)
        mininum = float('inf')
        found = False
        for num,count in countA.items():
            # print('A num',num)
            # print('A count',count)
            
            if num in countB and count + countB[num] >= length:
                # print('B count',countB[num])
                smaller = length - max([count, countB[num]])
                if smaller < mininum:
                    minimum = smaller
                    found = True
        return minimum if found else -1


A = [2, 1, 2, 4, 2, 2]
B = [5, 2, 6, 2, 3, 2]
solution = Solution()
print(solution.minDominoRotations(A, B))
