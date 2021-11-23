import json
import os
import urllib.request

import kenlm


class Decontractor:
    def __init__(self):
        """
        Initialize the decontraction class.
        """
        self.module_path = os.path.dirname(os.path.realpath(__file__))
        self.model_path = os.path.join(self.module_path, "3-gram.pruned.3e-7.binary")
        self.data_path = os.path.join(self.module_path, "contractions_data.json")
        if not os.path.exists(self.model_path):
            self.download_model()
        self.model = kenlm.Model(self.model_path)
        self.contractions = json.load(open(self.data_path))

    def download_model(self):
        """
        Downloads the data for the decontraction class.
        """
        model_url = "https://github.com/Wikidump/rel/releases/download/decontractions-lm-1/3-gram.pruned.3e-7.binary"
        with urllib.request.urlopen(model_url) as f:
            with open(self.model_path, "wb") as f_out:
                f_out.write(f.read())

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
