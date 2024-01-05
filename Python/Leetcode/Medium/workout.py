def groupAnagrams(strs):# List[str]) -> List[List[str]]:
        anagram={}
        for word in strs:
            sorted_word=''.join(sorted(word))
            if sorted_word in anagram:
                anagram[sorted_word].append(word)
            else:
                anagram[sorted_word]=[word]
        return list(anagram.values())

strs = ["eat","tea","tan","ate","nat","bat"]
# strs=[]
print(groupAnagrams(strs))
