# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n+1): #remember to do n + 1 for the sake of returning a the very last index as well
            if isBadVersion(i):
                return i
        return n
