import streamlit as st
import re

def count_words(text):
    # Split the text by any whitespace and count the parts
    return len(re.findall(r'\w+', text))

def count_sentences(text):
    # Split the text by sentence delimiters and count the parts
    return len(re.findall(r'[.!?]+', text)) + 1

def main():
    st.title('Text Summary Tool')
    
    # Create multiple tabs
    tabs = st.tabs(["Word Count", "Other", "Application 3", "Application 4", "Application 5"])

    with tabs[0]:  # Word Count tab
        st.header("🔍 Word and Sentence Counter")
        st.caption("This application will display the number of words and sentences in your text. After pasting your text in the box below, hit 'Control + Enter' key to see the result. [2024.11.01]")
        user_input = st.text_area("Paste your text here:", height=300)
        
        if user_input:
            word_count = count_words(user_input)
            sentence_count = count_sentences(user_input)
            st.write("✏️ Here's the text count summary:")

            st.write(f"〽️ **Word Count**: {word_count}")
            st.write(f"〽️ **Sentence Count**: {sentence_count}")

    with tabs[1]:  # Other Features tab
        st.header("Other Features")
        st.write("More features can be implemented here.")

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

if __name__ == '__main__':
    main()
