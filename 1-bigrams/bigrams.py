""""
Project 1 for CS 4740
Fred Callaway, Kang-Li Chen


Notes:
Type annotations are optional, but strongly encouraged for functions
that both team members may be using or writing. Type checking is not normally
enforced at run time, but you can do this if you want with mypy. This is
a very useful tool for debugging.

I've written this out in a functional rather than object oriented
design. This has the advantage of making input and output clear
which is good for cooperation. But there's a natural object oriented
way to do this as well, which I've architected as well. I'm not sure
which version I like better...

I think 100 chars is a good column limit. I'm flexible on that though.
"""

from typing import List, Dict


def tokenize(file_name) -> List[str]:
    """Returns a list of tokens in a file."""
    pass
    # start with nltk punkt sentence tokenizer
    # OR just assume {.?!} mark sentence ending


def cooccurence_matrix(tokens: List[str] ) -> Dict[str, Dict[str, int]]:
    """Returns a co-occurrence matrix.

    D['school']['bus'] is the number of times 'bus' follows 'school' in `tokens`"""
    pass
    # This could also be done with pandas DataFrame. Doing so will
    # make later computations easier. A DataFrame has mostly the same
    # interface as a dict of dicts anyway, so no reason to worry about
    # it now.


def log_probability_matrix(coo_matrix: Dict[str, Dict[str, int]]
                           ) -> Dict[str, Dict[str, float]]:
    """Converts co-occurrence matrix to negative log probability matrix.

    D['school']['bus'] is p(word_n = 'bus' | word_n-1 = 'school')"""
    pass
    # negative log probability because log proabilities are negative,
    # and we want to use positive numbers

    # this isn't strictly speaking necessary, but it will prevent 
    # recomputation when we do perplexity. If you're a true
    # baller, you will make this a lazily evaluated data structure.


def predict_next(lp_matrix, token) -> str:
    """Returns a token from distribution of tokens that follow the given token."""
    pass


def bigram_probability(lp_matrix, token1, token2) -> float:
    """Returns probability of token2 following token1."""
    pass


def generate_sentence(lp_matrix, initial="") -> str:
    """Returns a sentence.

    Optionally, the beginning of the sentence is given."""
    pass