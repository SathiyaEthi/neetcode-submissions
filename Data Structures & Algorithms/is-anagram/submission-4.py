class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt=0
        name_s,name_t = set(s),set(t)
        if len(s) != len(t):
            return False
        name_d,name_t={},{}
        
        for name in s:
            name_d[name]=name_d.get(name,0)+1
        for name in t:
            name_t[name]=name_t.get(name,0)+1
        print(name_d,name_t)
        
        if name_d==name_t:
            return True
        else:
            return False
            
            

                # return True
        # for namet in t:
        #     cnt+=1
        #     
        # print(name_t,name_s)
        # if name_s==name_t:
        #     return True
        # else:
        #     return False            # name_l.value()
        