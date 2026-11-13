def longest_substring(s):

    # Edge Case: Empty String
    if len(s) == 0:
        return 0

    seen = {}

    left = 0

    max_len = 0

    for right in range(len(s)):

        ch = s[right]

        # Duplicate found inside current window
        if ch in seen and seen[ch] >= left:

            left = seen[ch] + 1

        # Store latest index
        seen[ch] = right

        # Current window length
        current_len = right - left + 1

        if current_len > max_len:
            max_len = current_len

    return max_len


s = input("Enter string: ").strip()

print(longest_substring(s))