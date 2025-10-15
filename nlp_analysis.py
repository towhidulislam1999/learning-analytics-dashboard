# nlp_analysis.py

from textstat import flesch_reading_ease, flesch_kincaid_grade, gunning_fog, smog_index
import language_tool_python
import re
from collections import Counter

# 1. Readability Analysis
def compute_readability(text: str) -> dict:
    return {
        "flesch_reading_ease": flesch_reading_ease(text),
        "flesch_kincaid_grade": flesch_kincaid_grade(text),
        "gunning_fog": gunning_fog(text),
        "smog_index": smog_index(text)
    }

# 2. Grammar Checking with LanguageTool
tool = language_tool_python.LanguageTool('en-US')

def grammar_check(text: str) -> list:
    matches = tool.check(text)
    issues = []
    for m in matches:
        issues.append({
            "message": m.message,
            "offset": m.offset,
            "length": m.errorLength,
            "suggestion": m.replacements[0] if m.replacements else None
        })
    return issues

# 3. Text Analysis: word count, sentence count, sentiment via simple lexicons
POSITIVE = {"good","great","excellent","happy","love"}
NEGATIVE = {"bad","poor","terrible","sad","hate"}

def analyze_text(text: str) -> dict:
    # Word & sentence counts
    words = re.findall(r"\w+", text)
    sentences = re.split(r"[.!?]+", text.strip())
    # Sentiment score
    sentiment = sum((w.lower() in POSITIVE) - (w.lower() in NEGATIVE) for w in words)
    sentiment = max(-1, min(1, sentiment / len(words))) if words else 0
    # Average word length
    avg_word_len = sum(len(w) for w in words) / len(words) if words else 0
    # Complexity metric
    complexity = avg_word_len / 10
    # Most common words
    freq = Counter(w.lower() for w in words if len(w)>3)
    common = freq.most_common(10)
    return {
        "word_count": len(words),
        "sentence_count": len([s for s in sentences if s.strip()]),
        "sentiment": round(sentiment, 2),
        "avg_word_length": round(avg_word_len, 1),
        "complexity": round(complexity, 2),
        "common_words": common
    }

# 4. Example usage
if __name__ == "__main__":
    sample = "I love learning. This is a great example. But sometimes it is bad."
    print("Readability:", compute_readability(sample))
    print("Grammar Issues:", grammar_check(sample))
    print("Analysis:", analyze_text(sample))
