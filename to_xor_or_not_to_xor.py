N = int(input())
ls = list(map(int, input().split()))
'''answer = 0
for i in range(N):
    answer += answer ^ ls[i]
print(answer)'''


def maximum_xor_subsequence(arr):
    # Function to find the maximum XOR subsequence

    # Sort the array by the highest bit length first
    arr.sort(reverse=True, key=lambda x: x.bit_length())

    # This will store the maximum XOR value we can get
    max_xor = 0

    # Iterate over the array to build the maximum XOR subsequence
    for num in arr:
        # Try to maximize max_xor with the current number
        max_xor = max(max_xor, max_xor ^ num)

    return max_xor


print(maximum_xor_subsequence(ls))
