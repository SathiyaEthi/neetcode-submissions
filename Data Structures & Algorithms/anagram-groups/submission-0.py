class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_dict={}
        temp_dict={}
        
        for name in strs:
            # name_set=set(name)
            sort_dict2={}
            count=[0] * 26
            for str_name in name:
                print(ord(str_name))
                count[ord(str_name) - ord('a')]+=1
            
            

            key=tuple(count)
            print("key",key)
            if key not in temp_dict:
                temp_dict[key]=[]
            temp_dict[key].append(name)
        return list(temp_dict.values())
        
        
            
            
        
