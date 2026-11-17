class Solution:
    def topKFrequent(self, nums, k):
        frequency ={}
        for num in nums:
            frequency[num] = frequency.get(num,0)+1
        buckets = [[] for _ in range(len(nums)+1)]
        for num, count in frequency.items():
            buckets[count].append(num)
            result = []
            for i in range(len(buckets)-1,0,-1):
                for num in buckets[i]:
                    result.append(num)
                    if len(result) == k:
                        return result
nums = list(map(int , input ("Enter array elements: ").split())) 
k = int(input("Enter the value of k: "))
solution = Solution()
print(solution.topKFrequent(nums, k))
