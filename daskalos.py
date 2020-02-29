'''
the start of something new:
the daskalos class implements the (Chathack) chatbot
'''

#library for HTTP requests
import requests
#library for parsing HTML
from bs4 import BeautifulSoup
import re
import string
import numpy as np
import random
from nltk.stem.porter import *


class Daskalos:
    def __init__(self):
        self.name = 'philosophicalbot'
    
    def greeting(self):
        return "Hello, how are you?"
    
    def intro(self):
        return "I am Dask, your personal philosophical and enriching conversation partner."
    
    def goodbye(self):
        return "Goodbye"
    
    def process(self, line):
        return ("processed" + line)
    
