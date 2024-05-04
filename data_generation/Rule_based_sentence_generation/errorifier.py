"""Synthetic data generator."""
import math
import pickle
import random
from numpy.random import choice as npchoice

REPLACE_WFT = pickle.load(open('L1_replaces_WFT.p', 'rb'))
REPLACE_copexp = pickle.load(open('L1_replaces_copexp.p', 'rb'))
REPLACE_syn = pickle.load(open('L1_replaces_syn.p', 'rb'))
REPLACE_tensem = pickle.load(open('L1_replaces_tensem.p', 'rb'))
REPLACE_transliteration = pickle.load(open('L1_replaces_transliteration.p', 'rb'))

class Errorifier:
    """Generate errors in good sentences!"""

    def __init__(self, sentence: str):
        self.original_sentence = sentence.rstrip()
        self.sentence = self.original_sentence
        self.tokenized = None
        self.tokenize()

    def tokenize(self):
        self.tokenized = self.sentence.split()

    def correct(self):
        return self.original_sentence

    def no_error(self):
        return ' '.join(self.tokenized)

    def replace_error(self, redir=True, err_type='syn'):
        if err_type == 'WFT':
            COMMON_REPLACES = REPLACE_WFT
        if err_type == 'Copying expression':
            COMMON_REPLACES = REPLACE_copexp
        if err_type == 'Synonyms':
            COMMON_REPLACES = REPLACE_syn
        if err_type == 'Tense semantics':
            COMMON_REPLACES = REPLACE_tensem
        if err_type == 'Transliteration':
            COMMON_REPLACES = REPLACE_transliteration
        if len(self.tokenized) > 0:
            deletable = [i for i, w in enumerate(self.tokenized) if w in COMMON_REPLACES]
            index = random.choice(deletable)
            word = self.tokenized[index]
            if not COMMON_REPLACES[word]:
                return self.sentence

            # Normalize probabilities
            plist = list(COMMON_REPLACES[word].values())
            plistsum = sum(plist)
            plist = [x / plistsum for x in plist]

            # Choose a bad word
            repl = npchoice(list(COMMON_REPLACES[word].keys()), p=plist)
            self.tokenized[index] = '**' + repl + '**' + ' (' + err_type + ')'

        return ' '.join(self.tokenized)

    def error(self):
        """Introduce a random error."""
        count = npchoice([0,1,2,3,4],p=[0.05,0.07,0.25,0.35,0.28])
        for x in range(count):
            error_probs = [.20,.20,.20,.20,.20]
            error_type = npchoice(['WFT', 'Copying expression', 'Synonyms', 'Tense semantics', 'Transliteration'],p=error_probs)
            self.sentence = self.replace_error(err_type=error_type)
            self.tokenize()

        return self.sentence
