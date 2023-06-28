def row_recurs(word: str):
    if len(word) == 0:
        return ""

    return word[-1] + row_recurs(word[:-1])

print(row_recurs("Hello"))