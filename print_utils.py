def print_intro():
    print("============ BOOKBOT ============")


def print_outro():
    print("============= END ===============")


def print_word_count(word_count: int):
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")


def print_target(file_name: str):
    print(f"Analyzing book found at {file_name}...")


def print_sorted_char_count(sorted_char_count: list[dict]):
    print("--------- Character Count -------")
    for char_count_dict in sorted_char_count:
        print(f"{char_count_dict["char"]}: {char_count_dict["num"]}")
