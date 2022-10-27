def remove_non_ints(all_chars):
    str_list = []
    for char in all_chars:
        if char.isdigit() or char == ".":
            str_list.append(char)

    return "".join(str_list)
