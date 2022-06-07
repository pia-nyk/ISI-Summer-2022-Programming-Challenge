# ISI-Summer-2022-Programming-Challenge

<b> Description </b><br/>
This is the solution repository for ISI's Summer 2022 Programming Challenge.
<br/>

<b> Scraping & JSON file creation </b><br/>
Collection of latest articles from <a> https://www.aljazeera.com/where/mozambique/ </a> has been accomplished using <b>BeautifulSoup</b> library in Python3. The collected articles have been saved in json format & a sample of which can be found in /output/news.json
<br/>
The json file contains an array of articles, each consisting of the following key value pairs:
<ul>
  <li> <b>title</b>: title of the news article </li>
  <li> <b>headline</b>: summary line of the news article </li>
  <li> <b>published date</b>: date when the article was posted on the site </li>
  <li> <b>url</b>: link to the complete news article </li>
  <li> <b>img</b>: main image for the news article </li>
  <li> <b>img_caption</b>: caption for the main image of the news article </li>
  <li> <b>content</b>: the complete news article </li>
</ul>

<br/>
<b>Data Preprocessing & Sentiment Analysis</b><br/>
For sentiment analysis, the content part of each article from the json file has been used. After tokenization of the sentences using <b>RegexTokenizer</b> from <b>nltk</b> library, data has been cleaned bu removing punctuation, stop words & digits. The tokens have been lemmatized by <b>WordNetTokenizer</b> from <b>nltk</b> library in Python3. Sentiment Analysis has been performed on the tokens using <b>SentimentIntentAnalyzer</b> module from <b>nltk</b> library in Python3.
<br/><br/>

<b>Results</b><br/>
The sentiment analysis module used, provides 4 components for each of the sentences (pos, neg, neu, compound) called polarity scores. Polarity scores for the top 10 articles from <a> https://www.aljazeera.com/where/mozambique/ </a> can be seen as below. 
![alt text](https://github.com/pia-nyk/ISI-Summer-2022-Programming-Challenge/blob/master/output/Sentiment%20Analysis.png?raw=true)

<br/>
To tag a sentiment to the article based on the above scores, the rule followed is Anything below a compound score of -0.05 we tag as negative and anything above compound score of 0.05 we tag as positive.

![alt text](https://github.com/pia-nyk/ISI-Summer-2022-Programming-Challenge/blob/master/output/Percent%20of%20Sentiments.png?raw=true)

<br/><br/>
<b> Additions </b><br/>
The script also has the ability to analyze any number of articles (upto 14 as there are 14 pre-loaded articles on the AlJazeera home page for a country) for any of the countries, from the AlJazeera website.

<br/><br/>
<b> Steps to reproduce </b><br/>
Clone the repo

```console
$ git clone https://github.com/pia-nyk/ISI-Summer-2022-Programming-Challenge.git
```
```console
$ cd ISI-Summer-2022-Programming-Challenge
```
Install all required dependencies
```console
$ pip3 install -r requirements.txt
```
Go to the src folder in the cloned repo
```console
$ cd src
```
Call the script with country name & number of articles required
```console 
$ python3 plot.py mozambique 10
```

<b>Plotly</b> chart will open on a new webpage in your browser.





