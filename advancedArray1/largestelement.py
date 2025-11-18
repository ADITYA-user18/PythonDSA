


def largest(arr):
    first_larger = 0
    second_larger = 0
    for  i in range(len(arr)):
        if arr[i] > first_larger:
            first_larger = arr[i]
    for i in range(len(arr)):
        if arr[i] != first_larger and arr[i] > second_larger:
            second_larger = arr[i]

    return first_larger



c = largest([2,58,5,586554,65564,88488,58,9,85,85,848865455,85,2,6854864555555555555555])
print(c)