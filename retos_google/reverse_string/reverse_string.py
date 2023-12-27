def reverse_string(s: [str]) -> None:
        pointer = 0
        pointer_end = len(s) - 1
        while pointer < pointer_end:
                s[pointer],s[pointer_end]=s[pointer_end],s[pointer]
                pointer += 1
                pointer_end -= 1
        return s



# Example 1:

letters = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
result = reverse_string(letters)
print(result)

# Example 2:

letters2 = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
result2 = reverse_string(letters2)
print(result2)
