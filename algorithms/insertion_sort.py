def insertion_sort(items, key=lambda item: item):

    result = list(items)

    for index in range(1, len(result)):
        current_item = result[index]
        current_key = key(current_item)
        position = index - 1

        while position >= 0 and key(result[position]) > current_key:
            result[position + 1] = result[position]
            position -= 1

        result[position + 1] = current_item

    return result
