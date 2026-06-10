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
    try:
        with open("sample.txt", "r") as file:
            content = file.read()

        results = analyze_text(content)

        print("Total Characters:", results["total_characters"])
        print("Total Words: ", results["total_words"])
        print("Unique Words: ", results["unique_words"])

    except FileNotFoundError:
        print("Error! The file 'sample.txt' was not found.")