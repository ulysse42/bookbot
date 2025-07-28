def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_count(text: str) -> dict:
    char_count_map = {}
    for c in text:
        c_lower = c.lower()
        char_count_map[c_lower] = (
            char_count_map[c_lower] + 1 if c_lower in char_count_map else 1
        )
    return char_count_map


def get_sorted_char_count(char_count: dict) -> list[dict]:
    sorted_char_count = []
    for k, v in char_count.items():
        if k.isalpha():
            sorted_char_count.append({"char": k, "num": v})
    sorted_char_count.sort(reverse=True, key=sort_key_num)
    return sorted_char_count


def sort_key_num(item):
    return item["num"]
