import json
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from tqdm import tqdm
from time import sleep

class Preprocessor:
    def __init__(self):
        nltk.download('wordnet')
        nltk.download('omw-1.4')
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.lem = WordNetLemmatizer()
        self.stopwords = stopwords.words("english")
        self.sid_obj = SIA()

    def preprocess_articles(self):
        sentiment_analysis = []
        # get all the article content
        f = open("../output/news.json")
        news = json.load(f)['top_news']
        for i in tqdm(range(len(news))):
            sleep(.1)
            article = news[i]
            content = article['content']
            words = self.tokenizer.tokenize(content)
            filtered_words = []
            for w in words:
                if w.lower() not in self.stopwords and w.isalpha():
                    filtered_words.append(self.lem.lemmatize(w.lower(), "v"))
            sentence = " ".join(filtered_words)
            sentiment_dict = self.sid_obj.polarity_scores(sentence)
            sentiment_analysis.append(sentiment_dict)
        return sentiment_analysis
