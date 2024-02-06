#Import libraries
import streamlit as st
from textblob import TextBlob
from newspaper import Article


def analyze_sentiment(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    
    text = article.summary
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    
    return text, sentiment

def main():
    st.set_page_config(page_title="Sentiment Analysis😃😐😡")
    st.header("Sentiment Analysis😃😐😡") 

    # url uploader 
    url_input = st.text_input("Upload your Website Url:")
    if st.button("Upload 📥"):
        with st.spinner("Processing..."):
            st.write("Your Website:", url_input)

            # Analyze sentiment
            summary, sentiment = analyze_sentiment(url_input)

            # Display the summary and sentiment
            st.text_area("Summary of your website:", value=summary, height=250)
            sentiment_emoji = "😃" if sentiment > 0 else "😐" if sentiment == 0 else "😡"
            st.text_input("Sentiment Analysis Result:", value=f"{sentiment_emoji} Score: {sentiment}")

if __name__ =='__main__':
    main()
