from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])  # start with first word
        
        for word in words[1:]:
            common &= Counter(word)  # intersection
        
        return list(common.elements())