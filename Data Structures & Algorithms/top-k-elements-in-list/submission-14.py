class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict={}
        bucket = [[] for _ in range(0,len(nums)+1)]
        
        for i in nums:
            freq_dict[i] = freq_dict.get(i,0)+1
        

        for i , v in freq_dict.items():

            bucket[v].append(i)
        
        output=[]
        for i in range(len(bucket)-1,0,-1):
            
            for item in bucket[i]:
                output.append(item)
                
                if k == len(output):
                    return output
        
        
        # return [item for subitem in output for item in subitem]

              