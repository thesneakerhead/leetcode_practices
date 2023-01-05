def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        else:
            dictS,dictT = {},{}
            for i in range(len(s)):
                dictS[s[i]] = 1 + dictS.get(s[i],0) #dict.get(key, default=0) so that if key is not in dict, return 0
                dictT[t[i]] = 1 + dictT.get(t[i],0)
            for c in dictS:
                if dictS[c] != dictT.get(c,0):
                    return False
            return True