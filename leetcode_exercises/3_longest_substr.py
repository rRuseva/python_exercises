"""
Longest Substring Without Repeating Characters:
Given a string s, find the length of the longest substring without duplicate characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
"""


def length_of_longest_substring(s: str) -> int:
    substrings = {}
    longest_substr = 0
    for i, ch in enumerate(s):
        print(f"i: {i}, ch: {ch}")
        char_index = {}
        start_ch = ch
        char_index[start_ch] = i
        substr_len = 1
        for j in range(i+1, len(s)):
            print(f"j: {j}, s[j]: {s[j]}, char_index: {char_index}")
            if char_index.get(s[j], None) is None:
                char_index[s[j]] = j
                substr_len += 1
            else:
                print(f"Duplicate found for character: {s[j]} at index: {i+j}")
                break
            print("- - - - -")
        print(f"substring from index {i} is {substr_len}, longest substring so far: {longest_substr}")
        if substr_len > longest_substr:
            longest_substr = substr_len
            print(f"Longest substring so far: {longest_substr} starting at index: {i}")
        substrings[i] = longest_substr
        print("- - "*19)
    print(f"All substrings: {substrings}")
    return longest_substr


if __name__ == "__main__":
    s = "abcabcbb"

    print(f"string: {s}")
    print(f"length of longest substring: {length_of_longest_substring(s)}")
