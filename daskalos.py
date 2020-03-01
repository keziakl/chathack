'''
the start of something new:
the daskalos class implements the (Chathack) chatbot
'''

import wikipedia as wiki
import re
import numpy as np
import random
from nltk.stem.porter import *
import spacy


class Daskalos:
    def __init__(self):
        self.name = 'philosophicalbot'
        self.past_convo_topics = {} #dictionary with conversation topics and the amount of times they've appeared
        self.important_points = {} #dictionary with (the most sentiment) points made by user and their sentiment
        self.nlp = spacy.load('en_core_web_sm')
        self.set_of_non_wiki_search_words = {"I", "me", "you"}
        self.abbreviations ={} #dictionary with abbreviation key and list of meanings (NLP:natural language processing) also clarifications -- think: I saw Evelyn yesterday: who is evelyn? find a way to assign probabilities or clarifications to unknown nouns "I was working on my NLP project yesterday" "NLP?" "Yeah Natural language processing" "oh I've worked on that too!"
    
    def greeting(self):
        return "Hello, how are you?"
    
    def intro(self):
        return "I am Dask, your personal philosophical and enriching conversation partner."
    
    def goodbye(self):
        return "Goodbye"
    
    def process(self, line):
        doc = self.nlp(line)
        noun_phrases = self.get_noun_phrases(doc)
        #if noun_phrases #contains unknown word
        return str(self.retrieve_info(noun_phrases))
    
    def retrieve_info(self, key_words): #key_words is a list of parsed words that might be relevant (aka get rid of filler/stop words)
        poss_articles_of_key_words = []
        for word in key_words:
            if word not in self.set_of_non_wiki_search_words:
                poss_articles_of_key_words.append(wiki.search(word))
        return poss_articles_of_key_words
    
    '''
    Helper methods for the spaCy software
    '''
    def get_noun_phrases(self, doc):
        np = [chunk.text for chunk in doc.noun_chunks]
        return np
'''
TODO:
- sentiment analysis of the sentences so that you can measure how important they are/how riled up the person is
- recognize famous quotes (search wikipedia for them not sure how to search for specific quotes)
- predict what's the argument (most important noun)
- create a sentence that argues something/ brings same/diff pov (func: same_pov creator vs diff_pov_creator)
- fact checker: check whether a sentence is true or not (MLK killed JFK)
- how to deal with "I" (respond with "you" or ignore)
- phrase reocognizer: in "I was reading an article on NLP and it said that Twitter is a good measure of the stock market" you want to talk about "Twitter is a good measure of the stock market" --> search that statement in wikipedia or google to find articles, etc.
- SASS: example convo:
    A: I was reading an article on NLP and it said that Twitter is a good measure of the stock market
    B: Wow you're always reading nerd
    A: Thanks, bud.
    A: I'm joking with you. I also heard about that from the NYT. They said that public opinion determines the rise of prices and consumerism in the US.
    Notes: store "Twitter is a good measure of the stock market", "NLP" (implement spidering from wiki, using links in the relevant article?)
- argument handler: this impacts "me" rephrase to "this impacts you" (rephrase with regex I know that this )
- function spider: find article then use a link/relevant article to bring up new topic
- if can't find relevant article (maybe sentence like "i miss you a lot" or "hello") do regex of repeating

Advanced: if they mispell/don't use right grammar/don't cap or punctua

LOOK UP:
- side convos in chatbots
- search google or wiki by quotes
- finding unknown/vague nouns

spaCy use:
- named entity recognition for nouns
- dependecy parsing for finding what to search wikipedia

'''
