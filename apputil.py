from collections import defaultdict
import numpy as pd

class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None 

    def get_term_dict(self):

        terms = self.corpus.split()
        term_dict = defaultdict(list)

        for i in range(len(terms) - 1):
            current_term = terms[i]
            next_term = terms[i + 1]
            term_dict[current_term].append(next_term)

        self.term_dict = term_dict

        return None

    def generate(self, seed_term=None, term_count=15):

        if self.term_dict is None:
            self.get_term_dict()

        if seed_term is not None:
            if seed_term not in self.term_dict:
                raise ValueError("error")
            current_term = seed_term
        else:
            current_term = np.random.choice(list(self.term_dict.keys()))

        generated_terms = [current_term]

        for _ in range(term_count - 1):
            if current_term not in self.term_dict:
                break
            next_options = self.term_dict[current_term]
            next_term = np.random.choice(next_options)
            generated_terms.append(next_term)
            current_term = next_term

        return " ".join(generated_terms)