""""
Project 1 for CS 4740
Fred Callaway, Kang-Li Chen

Note: type annotations are optional, but strongly encouraged for functions
that both team members may be using or writing. Type checking is not normally
enforced at run time, but you can do this if you want with mypy. This is
a very useful tool for debugging.

I think 100 chars is a good column limit. I'm flexible on that though.

This is identical to bigrams.py but with an object oriented structure.
The lazy_property decorator is a way to define an immutable property
of an object using a method. Much cleaner than filling up your __init__
with all that stuff. We will have to adjust if we want to be able to
give the BigramMatrix more data after its initial creation.
"""

import numpy as np
import pandas as pd
from scipy import stats

from typing import List, Dict

from utils import lazy_property




def tokenize(file_name) -> List[str]:
    """Returns a list of tokens in a file."""
    pass
    # kang-li

    # remove cruft
    # tokenize to list

    # start with nltk punkt sentence tokenizer
    # OR just assume {.?!} mark sentence ending

        


class BigramMatrix(object):
    """A matrix for tracking bigram frequncies."""
    def __init__(self, tokens: List[str]):
        self.tokens = tokens


    @lazy_property  # aka a method that caches its result
    def cooccurence_matrix(self) -> Dict[str, Dict[str, int]]:
        """Returns a co-occurrence matrix.

        D['school']['bus'] is the number of times 'bus' follows 'school' in `tokens`"""
        tokens = self.tokens

        unique_tokens = list(set(tokens))
        zeros = np.zeros((len(unique_tokens), len(unique_tokens)))
        matrix = pd.DataFrame(data=zeros, columns=unique_tokens, index=unique_tokens)

        for i in range(len(tokens) - 1):
            matrix[tokens[i]][tokens[i+1]] += 1

        return matrix

        # This could also be done with pandas DataFrame. Doing so will
        # make later computations easier. A DataFrame has mostly the same
        # interface as a dict of dicts anyway, so no reason to worry about
        # it now.

    @lazy_property
    def probability_matrix(self) -> Dict[str, Dict[str, float]]:
        """Converts co-occurrence matrix to negative log probability matrix.

        D['school']['bus'] is p(word_n = 'bus' | word_n-1 = 'school')"""
        dependency = self.cooccurence_matrix

        # negative log probability because log proabilities are negative,
        # and we want to use positive numbers

        # this isn't strictly speaking necessary, but it will prevent 
        # recomputation when we do perplexity. If you're a true
        # baller, you will make this a lazily evaluated data structure.
        coo_matrix = self.cooccurence_matrix
        
        def counts_to_probabilities(series):
            return series / sum(series)  # applies to every element in the series

        return coo_matrix.apply(counts_to_probabilities)

    def predict_next(self, token) -> str:
        """Returns a token from distribution of tokens that follow the given token."""
        words = self.probability_matrix.index.tolist()
        probs = self.probability_matrix[token].tolist()
        
        indices = range(len(words))  # rv_discrete requires that values be integers
        distribution = stats.rv_discrete(values=(indices, probs))
        chosen_index = distribution.rvs()

        return words[chosen_index]


    def generate_sentence(self, initial="") -> str:
        """Returns a sentence.

        Optionally, the beginning of the sentence is given."""
        words = initial.split()
        if not words:
            words.append(self.predict_next('.'))
        for _ in range(20):  # 20 is max sentence length
            next_word = self.predict_next(words[-1])
            words.append(next_word)
            if next_word in '.!?':
                break

        return ' '.join(words)

tokens = 'the dog is fun . i like the dog . a dog is a good friend .'.split(' ')

bm = BigramMatrix(tokens)
print('\n\n')
#print(bm.cooccurence_matrix)
#print(bm.probability_matrix)
print(bm.generate_sentence())