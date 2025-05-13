import streamlit as st
import re

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["📖 Readability", "📏 Gunning-Fog Index", "🧩 APP3"])

# --- Tab 1: Readability Overview ---
with tab1:
    st.markdown("## 📖 What is Readability?")
    st.markdown("""
    **Readability** refers to how easy a piece of text is to read and understand.  
    It is often measured using formulas that take into account factors like:

    - Sentence length  
    - Word complexity (especially multisyllabic words)  
    - Vocabulary richness or **lexical diversity**

    ### 🔹 Lexical Diversity
    Lexical diversity measures how many unique words (types) are used in relation to the total number of words (tokens).

    - Type-Token Ratio (TTR) = Unique words ÷ Total words  
    - A higher TTR suggests richer vocabulary.

    Common readability formulas include:
    - Gunning-Fog Index
    - Flesch-Kincaid
    - SMOG Index
    """)

# --- Tab 2: Gunning-Fog Index Calculator ---
with tab2:
    st.markdown("## 📏 Gunning-Fog Index Calculator")
    st.markdown("Paste your English text below:")

    user_text = st.text_area("Enter text here:", height=200)

    def count_syllables(word):
        """Rough syllable counter using regex and vowel clusters."""
        word = word.lower()
        word = re.sub(r'[^a-z]', '', word)
        return max(1, len(re.findall(r'[aeiouy]+', word)))

    def compute_gunning_fog(text):
        sentences = re.split(r'[.!?]', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        num_sentences = len(sentences)

        words = re.findall(r'\b\w+\b', text)
        num_words = len(words)

        complex_words = [word for word in words if count_syllables(word) >= 3]
        num_complex = len(complex_words)

        if num_sentences == 0 or num_words == 0:
            return None

        avg_sentence_length = num_words / num_sentences
        percent_complex_words = (num_complex / num_words) * 100

        fog_index = 0.4 * (avg_sentence_length + percent_complex_words)
        return round(fog_index, 2)

    if user_text:
        index = compute_gunning_fog(user_text)
        if index is not None:
            st.success(f"📊 Gunning-Fog Index: **{index}**")
            st.caption("A score of 12+ indicates college-level difficulty.")
        else:
            st.warning("Please enter a valid passage.")

# --- Tab 3: Placeholder ---
with tab3:
    st.markdown("### 🧩 APP3")
    st.write("This space is reserved for an additional tool or app.")
