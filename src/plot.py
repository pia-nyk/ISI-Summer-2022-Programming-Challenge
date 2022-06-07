import plotly.graph_objects as go
from scrape import Scraper
from preprocess import Preprocessor
import sys


class Plotter:
    def __init__(self, country, articles):
        self.sentiment_analysis = None
        self.scraper = Scraper(page='https://www.aljazeera.com',
                               url='https://www.aljazeera.com/where/' + country, articles=articles)
        self.processor = Preprocessor()
        self.country = country
        self.articles = articles

    def get_sentiment_analysis_dict(self):
        self.scraper.store_data_to_json_file()
        self.sentiment_analysis = self.processor.preprocess_articles()

    def plot(self):
        x_axis = ['Article ' + str(i) for i in range(1, self.articles + 1)]
        fig = go.Figure(data=[
            go.Bar(name='Positive', x=x_axis, y=[self.sentiment_analysis[i]['pos'] for i in range(0, self.articles)]),
            go.Bar(name='Negative', x=x_axis, y=[self.sentiment_analysis[i]['neg'] for i in range(0, self.articles)])
        ])
        fig.update_layout(
            title_text='Sentiment Analysis of ' + str(self.articles) + ' latest AlJazeera articles for ' + self.country.upper(),
            xaxis_title="Articles",
            yaxis_title="Score")
        # Change the bar mode
        fig.update_layout(barmode='group')
        fig.show()


if __name__ == '__main__':
    # arguments taken while calling the script
    country = sys.argv[1]
    articles = int(sys.argv[2])

    plotter = Plotter(country, articles)
    plotter.get_sentiment_analysis_dict()
    plotter.plot()
