def mini_max(arr, p, q):
    sorted_arr = sorted(arr)
    best_distance = -1
    best_minimax = None

    if sorted_arr[0] > p:
        best_distance = sorted_arr[0] - p
        best_minimax = p

    for i in range(0, len(sorted_arr) - 1):
        start = sorted_arr[i]
        end = sorted_arr[i + 1]

        if start <= q and end >= p:
            point, distance = _find_most_distant_point_in_range(start, end, p, q)
            if distance > best_distance:
                best_minimax = point
                best_distance = distance

    if sorted_arr[-1] < q and (q - sorted_arr[-1]) > best_distance:
        best_minimax = q

    return best_minimax


def _find_most_distant_point_in_range(start, end, p, q):

    mid = (start + end) // 2
    if mid < p:
        return (p, end - p)
    elif mid > q:
        return (q, q - start) 
    else:
        return (mid, mid - start)