import streamlit as st
import re

# Functions to count words and sentences
def count_words(text):
    return len(re.findall(r'\w+', text))

def count_sentences(text):
    return len(re.findall(r'[.!?]+', text)) + 1

def remove_line_breaks(text):
    return re.sub(r'[\r\n]+', ' ', text)

# Set up the Streamlit interface
st.title('Text Summary Tool')

# Create multiple tabs
tabs = st.tabs(["Word Count", "Remove Line Breaks", "Application 3", "Application 4", "Application 5"])

with tabs[0]:  # Word Count tab
    st.header("🔍 Word and Sentence Counter")
    st.caption("This application will display the number of words and sentences in your text. After pasting your text in the box below, hit 'Control + Enter' key to see the result.")
    user_input = st.text_area("Paste your text here:", height=300)
    
    if user_input:
        word_count = count_words(user_input)
        sentence_count = count_sentences(user_input)
        st.write("✏️ Here's the text count summary:")
        st.write(f"〽️ **Word Count**: {word_count}")
        st.write(f"〽️ **Sentence Count**: {sentence_count}")

with tabs[1]:  # Remove Line Breaks tab
    st.header("🔄 Remove Line Breaks")
    st.caption("Paste your text here and see it transformed without line breaks, making it easier to copy without formatting.")
    user_input = st.text_area("Paste your text here to remove line breaks:", height=300)
    
    if user_input:
        processed_text = remove_line_breaks(user_input)
        st.write("📝 Here's your text without line breaks:")
        st.text_area("Copy the text below:", processed_text, height=300, key='processed')

# Placeholder tabs for future applications
with tabs[2]:
    st.header("Application 3")
    st.write("Details for Application 3 will be added here.")

with tabs[3]:
    st.header("Application 4")
    st.write("Details for Application 4 will be added here.")

with tabs[4]:
    st.header("Application 5")
    st.write("Details for Application 5 will be added here.")
