Lista = ['A', 'Z', 'D', 'G', 'M', 'C', 'W', 'E', 'F', 'B', 'T','Y']
stack = [[0, len(Lista) - 1]]
while stack:
    start, end = stack.pop()
    if start >= end:
        continue
    pivot = Lista[start]
    left = start + 1
    right = end
    while left <= right:
        if Lista[left] <= pivot:
            left += 1
        else:
            Lista[left], Lista[right] = Lista[right], Lista[left]
            right -= 1
    Lista[start], Lista[right] = Lista[right], Lista[start]
    stack.append([start, right - 1])
    stack.append([right + 1, end])

print("Lista ordenada:", Lista)