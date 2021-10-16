#import twint
#from twitter_scraper import get_tweets
import argparse
import logging
import json

import pandas as pd

"""
class TwintScrapper():
    def __init__(self, username : str, start_date : str, end_date : str, output_file : str, lang : str = 'fr', store_csv : bool=True):
        self.config = twint.Config()
        self.config.username = username
        self.config.Lang = lang
        self.config.since = start_date
        self.config.Until = end_date
        self.config.Store_csv = store_csv
        self.Output = output_file


    def search(self):
        twint.run.Search(config=self.config)
"""
if __name__ == '__main__':
    ##set the logging
    logging.basicConfig(level=logging.DEBUG)

    ## Get the argument from command line

    #   define some arguments used in the scrapping
    parser = argparse.ArgumentParser(description='Scrap data from a twitter profile')
    parser.add_argument('--username', type=str, help='the username of the twitter profile to scrap')
    parser.add_argument('--pages', type=int, help='the number of pages', default=1)
    parser.add_argument('--output', type=str, help='the path to the output file')

    #   parse the arguments
    logging.info('Parsing the arguments ...')
    args = parser.parse_args()

    logging.debug(f"args : {args}")

    #start scrapping
    liste = []
    with open('financial-tweets2.json', 'rb') as data_file:
        for idx, line in enumerate(data_file):
            logging.debug(line)
            tmp = json.load(line.strip())
            liste.append(tmp)

    df = pd.DataFrame(liste)
    df.to_csv('financial_tweet.csv')


    logging.info(f"End Scrapping, the result is in {args.output}")

