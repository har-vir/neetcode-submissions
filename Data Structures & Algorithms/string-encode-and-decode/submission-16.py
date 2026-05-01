class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "empty"

        ans = ""
        for s in strs:
            ans += str(len(s))
            ans += ","
        ans = ans[:-1] + "#"

        for s in strs:
            ans += s
        
        return ans

    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        if s == "":
            return [""]

        count, words, word = [], 0, ""

        num = ""
        for idx in range(len(s)):
            strs = s[idx]
            if strs == "#":
                words = idx + 1
                count.append(int(num))
                break
            if strs == ",":
                count.append(int(num))
                num = ""
                continue
            num += strs

        ans = []
        for c in count:
            for idx in range(int(c)):
              word += s[words]
              words += 1
            ans.append(word)
            word = ""
        
        return ans

            
              
