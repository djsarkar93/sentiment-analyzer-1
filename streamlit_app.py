import sentiment_analyzer
import streamlit as st



if __name__ == '__main__':
    st.set_page_config(page_title='Sentiment Analyzer', page_icon=':robot_face:')

    st.title("Sentiment Analysis using NLTK WordNet Lemmatizer")
    st.caption("Made by [Dibyajyoti Sarkar](https://www.linkedin.com/in/djsarkar93)")
    st.divider()

    text = st.text_area("Enter Your Text Here:")
    if st.button("Analyze"):
        polarity = sentiment_analyzer.analyze(text)
        if polarity > 0.75:
            st.success('Happy: :blush:')
        elif polarity < 0.3:
            st.warning('Sad: :disappointed:')
        else:
            st.info('Confused: :confused:')
        
        st.success(f'Polarity Score: {polarity}')
