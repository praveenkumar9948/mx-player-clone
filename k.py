# def max_coal_collection(mat):
#     n = len(mat)
#     m = len(mat[0])

#     # Initialize the dp array
#     dp = [[0] * m for _ in range(n)]

#     # Fill the dp array using the dynamic programming expression
#     for j in range(m):
#         for i in range(n):
#             dp[i][j] = mat[i][j] + max(dp[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0,
#                                         dp[i][j-1] if j-1 >= 0 else 0,
#                                         dp[i+1][j-1] if i+1 < n and j-1 >= 0 else 0)

#     # The maximum coal collection will be the maximum value in the last column of dp
#     max_coal = max(dp[i][-1] for i in range(n))

#     return max_coal

# # Example usage:
# input_matrix_1 = [
#     [1, 5, 12],
#     [2, 4, 4],
#     [0, 6, 4],
#     [3, 0, 0]
# ]

# input_matrix_2 = [
#     [1, 3, 1, 5],
#     [2, 2, 4, 1],
#     [5, 0, 2, 3],
#     [0, 6, 11, 2]
# ]

# output_1 = max_coal_collection(input_matrix_1)
# output_2 = max_coal_collection(input_matrix_2)

# print("Output for Input Matrix 1:", output_1)
# print("Output for Input Matrix 2:", output_2)


# # //.,bn,mnmn
def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Reconstruct the LCS
    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs = s1[i-1] + lcs
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs

# Example usage
s1_1, s2_1 = "abccba", "abddba"
lcs_1 = longest_common_subsequence(s1_1, s2_1)
print("Longest Common Subsequence:", lcs_1)  # Output: "abba"

s1_2, s2_2 = "zfadeg", "cdfsdg"
lcs_2 = longest_common_subsequence(s1_2, s2_2)
print("Longest Common Subsequence:", lcs_2)  # Output: "fdg"

