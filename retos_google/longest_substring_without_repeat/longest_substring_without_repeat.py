def lengthOfLongestSubstring(s):
    p1 = p2 = 0
    st = set()
    max_length = 0
    
    while p2 < len(s):
        if s[p2] not in st:
            st.add(s[p2])
            max_length = max(max_length, len(st))
            p2 += 1
        else:
            st.remove(s[p1])
            p1 += 1
    
    return max_length

response = lengthOfLongestSubstring("abcabcbb")
print(response)

response2 = lengthOfLongestSubstring("jdkafnlcdsalkxcmpoiuytfccv")
print(response2)