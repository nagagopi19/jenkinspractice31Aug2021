#list=[0,1,2,3,4,5,7,8,9]
class obj:
    def solve(self,nums):
        arr=[0]*(len(nums)+1)
        for i in nums:
            arr[i]=arr[i]+1
        missing = []
        for i in range (len(arr)):
            if arr[i] == 0 and i!=0:
                missing.append(i)
        return missing
a = obj()
#b= obj()
#print(a.solve([0,1,3,5,7,9]))
print(a.solve([0,1,2,3,4,5,6,8,9]))

