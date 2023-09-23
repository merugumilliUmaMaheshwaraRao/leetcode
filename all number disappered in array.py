    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
            ind=abs(i)-1
            if nums[ind]>0:
                nums[ind]=-nums[ind]
        
        i=0
        ne=[]
        for n in nums:
            if n>0:
                ne.append(i+1)
            i+=1
            
        return ne
