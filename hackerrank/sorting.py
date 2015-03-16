def sort_last_elem(arr):
    v  = arr[-1]
    for empty_cell in range(len(arr) - 1, -1, -1):
        if not empty_cell:
            arr[empty_cell] = v
            yield arr
            return
        elif arr[empty_cell - 1] <= v:
            arr[empty_cell] = v
            yield arr
            return
        else:
            arr[empty_cell] = arr[empty_cell - 1]
            yield arr
