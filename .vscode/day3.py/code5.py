class Solution(object):
    def strStr(self, haystack, needle):
        res=needle in haystack
        if res:
            return haystack.index(needle)
        return -1
#find the occurance of the index of the string