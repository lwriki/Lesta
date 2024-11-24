def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    # Создаем временные массивы
    left_subarray = arr[left:mid + 1]
    right_subarray = arr[mid + 1:right + 1]
    
    i = 0  # Индекс первого подмассива
    j = 0  # Индекс второго подмассива
    k = left  # Индекс для объединенного массива

    # Объединяем временные массивы обратно в arr[left:right+1]
    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            arr[k] = left_subarray[i]
            i += 1
        else:
            arr[k] = right_subarray[j]
            j += 1
        k += 1

    # Копируем оставшиеся элементы, если есть
    while i < len(left_subarray):
        arr[k] = left_subarray[i]
        i += 1
        k += 1

    while j < len(right_subarray):
        arr[k] = right_subarray[j]
        j += 1
        k += 1

def timsort(arr):
    min_run = 32  # Минимальный размер подмассива для сортировки вставками

    # Сортируем подмассивы размером min_run
    for start in range(0, len(arr), min_run):
        end = min(start + min_run - 1, len(arr) - 1)
        insertion_sort(arr, start, end)

    size = min_run
    while size < len(arr):
        for left in range(0, len(arr), size * 2):
            mid = min(len(arr) - 1, left + size - 1)
            right = min((left + 2 * size - 1), (len(arr) - 1))

            if mid < right:
                merge(arr, left, mid, right)

        size *= 2

# Пример использования
arr = [5, 3, 8, 6, 2, 7, 4, 1]
timsort(arr)
print("Отсортированный массив:", arr)
