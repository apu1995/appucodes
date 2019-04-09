# Leetcode Bitwise And of Numbers in a Range
class Solution(object):
    def msb_pos(self,n):
        pos=-1
        while(n>0):
            n=n>>1
            pos=pos+1
        return pos
    
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res=0
        while (m>0 and n>0):
            msb_m=self.msb_pos(m)
            msb_n=self.msb_pos(n)
            if(msb_m!=msb_n):
                break
            msb_val=1<<msb_m
            res=res+msb_val
            
            m=m-msb_val
            n=n-msb_val
        return res
        