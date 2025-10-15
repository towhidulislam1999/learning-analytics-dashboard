"""Text analyzer module for NLP functions"""

# ============================================
# TEXT ANALYZER CLASS (from earlier)
# ============================================
class TextAnalyzer:
    def __init__(self):
        self.positive_words = ['good', 'great', 'excellent', 'happy', 'love', 
                              'wonderful', 'amazing', 'fantastic', 'enjoy', 
                              'interesting', 'valuable', 'beneficial']
        self.negative_words = ['bad', 'poor', 'terrible', 'sad', 'hate', 
                               'awful', 'horrible', 'difficult', 'boring', 
                               'useless', 'frustrating']
    
    def analyze_text(self, text):
        words = [w for w in text.split() if w.strip()]
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        
        word_count = len(words)
        sentence_count = len(sentences)
        avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0
        
        # Sentiment
        sentiment = 0
        for word in words:
            word_lower = word.lower().strip('.,!?')
            if word_lower in self.positive_words:
                sentiment += 0.1
            if word_lower in self.negative_words:
                sentiment -= 0.1
        sentiment = max(-1, min(1, sentiment))
        
        # Complexity
        avg_word_length = sum(len(w) for w in words) / len(words) if words else 0
        complexity = avg_word_length / 10
        
        # Flesch score (simplified)
        flesch_score = 206.835 - (1.015 * avg_sentence_length) - (84.6 * (avg_word_length / 2.5))
        flesch_score = max(0, min(100, flesch_score))
        
        # Readability level
        if flesch_score >= 90:
            readability_level = "Elementary School"
        elif flesch_score >= 80:
            readability_level = "Middle School"
        elif flesch_score >= 60:
            readability_level = "High School"
        elif flesch_score >= 30:
            readability_level = "College"
        else:
            readability_level = "Graduate"
        
        return {
            'word_count': word_count,
            'sentence_count': sentence_count,
            'avg_sentence_length': round(avg_sentence_length, 1),
            'sentiment': round(sentiment, 2),
            'complexity': round(complexity, 2),
            'avg_word_length': round(avg_word_length, 1),
            'flesch_score': round(flesch_score, 1),
            'readability_level': readability_level
        }

