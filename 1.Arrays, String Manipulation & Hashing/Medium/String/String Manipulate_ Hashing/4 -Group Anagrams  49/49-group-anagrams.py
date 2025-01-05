# Efficient Solution
# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)
from typing import List


def group_anagrams(strs):
    anagrams = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

# -------------------------------------------------------------------------

# Alternative Approach: Character Count Key


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        # Dictionary to hold groups of anagrams
        hashmap = {}

        # Function to generate a frequency string that uniquely represents each anagram group
        def get_frequency_string(element):
            freq_list = [0] * 26

            for char in element:
                freq_list[ord(char) - ord('a')] += 1

            frequency_string = []
            char = 'a'
            for position in freq_list:
                frequency_string.append(char)
                frequency_string.append(str(position))
                char = chr(ord(char) + 1)

            return ''.join(frequency_string)

        # Iterate over each element in the input list
        for element in strs:
            frequency_string = get_frequency_string(element)

            if frequency_string not in hashmap:
                hashmap[frequency_string] = []

            hashmap[frequency_string].append(element)

        return list(hashmap.values())
