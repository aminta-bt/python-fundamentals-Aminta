"""WORD & CHARACTER COUNTER
Reads sample.txt and calculates the total number of words, characters & unique words.
"""

def analyze_text(text):
    words = text.split()
    unique_words = set(word.lower() for word in words)

    return {
        "total_characters": len(text),
        "total_words": len(words),
        "unique_words": len(unique_words),
    }

if __name__ == "__main__":
    with open("sample.txt", "r") as file:
        content = file.read()

    results = analyze_text(content)
    print(results)