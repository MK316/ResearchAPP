import streamlit as st
import textstat
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

    user_text = st.text_area("✏️ Enter your text here:", height=200)

    def compute_gunning_fog_verbose(text):
        sentences = re.split(r'[.!?]', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        num_sentences = len(sentences)

        words = re.findall(r'\b\w+\b', text)
        num_words = len(words)

        # Identify complex words (3+ syllables)
        complex_words = [word for word in words if textstat.syllable_count(word) >= 3]
        num_complex = len(complex_words)

        if num_sentences == 0 or num_words == 0:
            return None, 0, 0, 0, []

        avg_sentence_length = num_words / num_sentences
        percent_complex_words = (num_complex / num_words) * 100
        fog_index = 0.4 * (avg_sentence_length + percent_complex_words)

        return round(fog_index, 2), num_sentences, num_words, num_complex, complex_words

    if user_text:
        fog, num_sents, num_words, num_complex, complex_words = compute_gunning_fog_verbose(user_text)

        st.markdown(f"""
        <h3 style='color:green;'>THE GUNNING FOG INDEX IS <span style='color:red;'>{fog}</span></h3>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        - The number of major punctuation marks, e.g., <span style='color:red;'>[.]</span>, was **{num_sents}**  
        - The number of words was **{num_words}**  
        - The number of 3+ syllable words, <span style='color:blue;'>highlighted in blue</span>, was **{num_complex}**
        """, unsafe_allow_html=True)

        # Highlight complex words in blue within the text
        def highlight_complex_words(text, complex_words):
            def replacer(match):
                word = match.group(0)
                if word.lower() in [w.lower() for w in complex_words]:
                    return f"<span style='color:blue; font-weight:bold;'>{word}</span>"
                return word

            return re.sub(r'\b\w+\b', replacer, text)

        highlighted_text = highlight_complex_words(user_text, complex_words)

        st.markdown("---")
        st.markdown("#### ✨ Text with 3+ syllable words highlighted:")
        st.markdown(f"<div style='line-height: 1.8;'>{highlighted_text}</div>", unsafe_allow_html=True)
