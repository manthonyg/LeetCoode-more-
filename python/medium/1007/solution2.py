class Solution:
    def minDominoRotations(self, A, B):
        length = len(A)
        minimum = float('inf')
        for i in range(1,7):
            countA = 0
            countB = 0
            for j in range(length):
                print('i',i)
                print('A[j]',A[j])
                print('B[j]',B[j])
                if A[j] != i and B[j] != i:
                    break
                if A[j] == i:
                    countA += 1
                    print('countA', countA)
                if B[j] == i:
                    countB += 1
                    print('countB', countB)
            if countA + countB >= length:
                minimum = length - max([countA, countB]) if length - max([countA,countB]) < minimum else minimum

        return minimum if minimum < float('inf') else -1


A = [1,2,1,1,1,2,2,2]
B = [2,1,2,2,2,2,2,2]
solution = Solution()
print(solution.minDominoRotations(A, B))
            
