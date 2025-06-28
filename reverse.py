def reverseStr(c, l):
    c = list(c)
    for i in range(0, len(c), 2 * l):
        left = i
        right = min(i + l - 1, len(c) - 1)
        while left < right:
            c[left], c[right] = c[right], c[left]
            left += 1
            right -= 1
    return ''.join(c)

c = "diushids"
l = 2
print(reverseStr(c, l))
