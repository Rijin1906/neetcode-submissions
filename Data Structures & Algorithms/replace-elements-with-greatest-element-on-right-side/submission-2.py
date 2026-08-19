class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if len(arr) == 1:
            arr[0] = -1
            return arr

        largest = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j] > largest:
                    largest = arr[j]
            arr[i] = largest
            largest = 0    
        arr[-1] = -1
        return arr
        
                

            