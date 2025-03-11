import re
from collections import Counter

class TextAnalyzer:
    """A simple text analyzer that provides word frequencies and sentence count."""

    def __init__(self, text):
        self.text = text

    def count_sentences(self):
        """Counts the number of sentences in the text."""
        return len(re.findall(r"[.!?]+", self.text))

    def word_frequencies(self):
        """Returns a dictionary with word frequencies."""
        words = re.findall(r"\b\w+\b", self.text.lower())
        return dict(Counter(words))

    def most_common_words(self, n=5):
        """Returns the N most common words in the text."""
        return Counter(self.word_frequencies()).most_common(n)

if __name__ == "__main__":
    sample_text = "Hello world! This is a test. This test is just an example."
    analyzer = TextAnalyzer(sample_text)
    print(f"Sentence count: {analyzer.count_sentences()}")
    print(f"Word frequencies: {analyzer.word_frequencies()}")
    print(f"Most common words: {analyzer.most_common_words()}")
