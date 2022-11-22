def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    list_first_lower = list(first_string.lower())
    list_second_lower = list(second_string.lower())

    if first_string == "" and second_string == "":
        return (second_string, second_string, False)

    return (
        merge_sort(list_first_lower),
        merge_sort(list_second_lower),
        merge_sort(list_first_lower) == merge_sort(list_second_lower),
    )


def merge_sort(array):
    # join método pega todos os itens em um iterável e os une em uma string.
    if len(array) <= 1:
        return "".join(array)

    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return "".join(merge(left, right, array.copy()))


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged
