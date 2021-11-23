import json
import os

import kenlm


class Decontractor:
    def __init__(self):
        """
        Initialize the decontraction class.
        """
        module_path = os.path.dirname(os.path.realpath(__file__))
        self.model = kenlm.Model(os.path.join(module_path, "3-gram.pruned.3e-7.binary"))
        self.contractions = json.load(open(os.path.join(module_path, "contractions_data.json")))

    def __call__(self, text: str) -> str:
        """
        Decontracts a text.
        :param text: The text to be decontracted.
        :return: The decontracted text.
        """
        for contraction in self.contractions:
            if contraction not in text:
                continue
            con_count = text.count(contraction)
            for _ in range(con_count):
                old_perplexity = 1e4
                for expansion in self.contractions[contraction]:
                    toscore_text = text.replace(contraction, expansion, 1)
                    perplexity = self.model.perplexity(toscore_text.upper())
                    if perplexity < old_perplexity:
                        lowest_perplexity = toscore_text
                        old_perplexity = perplexity
                text = lowest_perplexity
        return text
