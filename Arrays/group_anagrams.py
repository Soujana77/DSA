class Solution:
    def groupAnagrams(self, strs):

        groups = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())


# Taking input from the user
strs = input("Enter words separated by spaces: ").split()

# Creating an object
obj = Solution()

# Calling the method
result = obj.groupAnagrams(strs)

# Displaying the output
print("Grouped Anagrams:", result)