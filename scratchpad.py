#!/usr/bin/env python3

import os
import sys

import helpers
from analyzer import Analyzer
from termcolor import colored
import string


def main():

    # ensure proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: ./tweets @screen_name")

    # queries Twitter’s API for a user’s most recent 50 tweets
    screen_name = sys.argv[1].lstrip('@')

    tweets = helpers.get_user_timeline(screen_name, 50)
    if tweets is None:
        sys.exit("Usage: ./tweets @screen_name")
    else:

        # analyzes the sentiment of each of those tweets
        positives = os.path.join(sys.path[0], "positive-words.txt")
        negatives = os.path.join(sys.path[0], "negative-words.txt")
        analyzer = Analyzer(positives, negatives)

        # outputs each tweet’s score and text, colored in green if positive, red if negative, and yellow otherwise
        for tweet in tweets:
            score = analyzer.analyze(tweet)
            if score > 0.0:
                print(colored(" {} {}", "green").format(score, tweet))
            elif score < 0.0:
                print(colored("{} {}", "red").format(score, tweet))
            else:
                print(colored(" {} {}", "yellow").format(score, tweet))


if __name__ == "__main__":
    main()
