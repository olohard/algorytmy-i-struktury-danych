class Solution:
    def isAnagram(self, a, b):
        if sorted(a) == sorted(b):
            return True

        else:
            return False

if __name__ == '__main__':
    a = "karma"
    b = "marka"

    if Solution().isAnagram(a, b):
        print("The two strings are anagram of each other")

    else:
        print("The two strings are not anagram of each other")