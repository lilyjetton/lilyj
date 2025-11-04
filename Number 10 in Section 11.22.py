def main() -> None:
    """Main fucntion that solves the problem
    """
    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    old = "o"
    new = "a"
    ss = replace(s, old, new)
    print(s)
    print(ss)

def replace(s, old, new) -> str:
    """Replaces all occurrences of old with new in each word of s"""
    words = s.split()
    new_words = []

    for word in words:
        modified = ""
        i = 0
        while i < len(word):
            if word[i:i+len(old)] == old:
                modified += new
                i += len(old)
            else:
                modified += word[i]
                i += 1
        new_words.append(modified)

    s = " ".join(new_words)
    return s

if __name__ == "__main__":
    main()
