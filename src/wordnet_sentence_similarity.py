from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn

class WordnetSentenceSimilarity:
    def _penn_to_wn(self, tag):
        """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
        if tag.startswith('N'):
            return 'n'
        elif tag.startswith('V'):
            return 'v'
        elif tag.startswith('J'):
            return 'a'
        elif tag.startswith('R'):
            return 'r'
        else:
            return None
    
    def _get_synset(self, word, tag):
        try:
            return wn.synsets(word, self._penn_to_wn(tag))[0]
        except:
            return None
    
    def _get_similarity_score(self, synsets1, synsets2):
        score, count = 0.0, 0
        # For each word in the first sentence
        for synset in synsets1:
            # Get the similarity value of the most similar word in the other sentence
            scores = [synset.path_similarity(ss) for ss in synsets2 if synset.path_similarity(ss)]

            # Check that the similarity could have been computed
            if scores:
                score += max(scores)
                count += 1
    
        # Average the values
        return score / count if score else 0

    def sentence_similarity(self, sentence1, sentence2):
        """ compute the sentence similarity using Wordnet """
        # Tokenize and tag
        sentence1 = pos_tag(word_tokenize(sentence1))
        sentence2 = pos_tag(word_tokenize(sentence2))
    
        # Get the synsets for the tagged words and filter out nones.
        synsets1 = [self._get_synset(*pos_word) for pos_word in sentence1 if self._get_synset(*pos_word)]
        synsets2 = [self._get_synset(*pos_word) for pos_word in sentence2 if self._get_synset(*pos_word)]
    
        score = self._get_similarity_score(synsets1, synsets2) + self._get_similarity_score(synsets2, synsets1)

        return score / 2 if score else 0 