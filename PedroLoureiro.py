def PedroSort(arr):

    n = len(arr)

    # Detecta intervalo pequeno
    menor = arr[0]
    maior = arr[0]

    for i in range(1, n):
        if arr[i] < menor:
            menor = arr[i]
        if arr[i] > maior:
            maior = arr[i]

    # Counting Sort
    if menor >= 0 and maior <= 100:

        count = [0] * 101

        for num in arr:
            count[num] += 1

        k = 0

        for i in range(101):
            while count[i] > 0:
                arr[k] = i
                k += 1
                count[i] -= 1

        return arr

    quicksort(arr, 0, n - 1)

    return arr


def quicksort(arr, low, high):

    while low < high:

        if high - low < 16:
            insertion(arr, low, high)
            return

        pivot = partition(arr, low, high)

        if pivot - low < high - pivot:
            quicksort(arr, low, pivot - 1)
            low = pivot + 1
        else:
            quicksort(arr, pivot + 1, high)
            high = pivot - 1


def partition(arr, low, high):

    mid = (low + high) // 2

    # mediana de três
    if arr[mid] < arr[low]:
        arr[mid], arr[low] = arr[low], arr[mid]

    if arr[high] < arr[low]:
        arr[high], arr[low] = arr[low], arr[high]

    if arr[high] < arr[mid]:
        arr[high], arr[mid] = arr[mid], arr[high]

    pivot = arr[mid]

    arr[mid], arr[high - 1] = arr[high - 1], arr[mid]

    i = low
    j = high - 1

    while True:

        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[high - 1] = arr[high - 1], arr[i]

    return i


def insertion(arr, low, high):

    for i in range(low + 1, high + 1):

        key = arr[i]
        j = i - 1

        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key