import string
import nltk
import re
import math
class BigramModel:

    def __init__(self, tokens):
        self.tokens = tokens
        self.wordcount = {}
        self.cleanlist = self.clean_tokens()
    def clean_tokens(self):
        startmark = "<s>"
        endmark = "</s>"
        cleanlist = []
        for sentence in self.tokens:
            cleanlist.append(startmark)
            for token in sentence:
                token.strip(string.punctuation)
                token.lower()
                if token != "":     # Only continue for tokens that are not empty (due to remove of punctuation)
                    if token in self.wordcount:  # Count words while looping over the text
                        self.wordcount[token] += 1
                    else:
                        self.wordcount[token] = 1
                    cleanlist.append(token)
            cleanlist.append(endmark)
        return cleanlist
    
    #telt aantal woorden:
    def wordsintext(self,w):
        nr_of_words = 0
        for x in self.tokens:
            if x == w:
                nr_of_words +=1
        return nr_of_words
    
    def calc_bigram_frequencies(self, bigramcount):
        total = 0
        for bigram in bigramcount:
            total += bigramcount[bigram]
        freqtable = {}
        for bigram in bigramcount:
            freqtable[bigram] = bigramcount[bigram]/total
            
        return freqtable
    def count_bigrams(self, sentences):
        """
        Calculates frequencies for all bigrams in all sentences. returns a 3D-array
        where words are linked to frequencies.
        """
        bigramcount = {}
        for sentence in sentences:
            for word in sentence[:-1]: # Not looping over the last word ("</s>") since there is no second word
                if sentence[word, word+1] in bigramcount:
                    bigramcount[[word,word+1]] += 1
                else:
                    bigramcount[[word,word+1]] = 1
        return bigramcount
    
    def p_raw(self, w, w_n):
        aantalw = BigramModel.wordsintext(w)
        x = self.count_bigrams(self.cleanlist)
        aantalw_en_w_n = x[[w, w_n]]
        chance_of_w_n = (aantalw_en_w_n / aantalw)
        return chance_of_w_n
    
    def p_smooth(self,w, w_n):
        x = self.count_bigrams(self.cleanlist)
        aantalw_en_w_n = x[[w, w_n]] + 1
        aantalw = BigramModel.wordsintext(w) + 1            
        #elke count 1 bij optellen, ook wanneer iets meerdere keren voorkomt
        chance_of_w_n = (aantalw_en_w_n / aantalw)
        return chance_of_w_n

    def successors(self, w):
        wi_ci_list = []
        for z in self.tokens:
            if self.p_raw(w, z) != 0:
                x = self.p_raw(w, z)
                if (z,x) in wi_ci_list:
                    wi_ci_list = wi_ci_list
                else:
                    wi_ci_list.append((z,x))
            
        return wi_ci_list
              
#Return a list of pairs (w_i, c_i) , where w_i is a token that
#might follow w , and c_i is its raw (unsmoothed) bigram
#probability, P_r(w_i | w) . Tokens with zero probability need
#not be included in the result.
        
    
    def perplexity(self, sent):
        #er moet van sent nog tokens gemaakt worden en vervolgens van de tokens
        #sentences zoals in clean_tokens:
        sent_tokenized = sent.split()?
        
        sent_sentences = sent...?
        calc = 0
        for x in sent_tokenized:
            calc *= 1/(self.p_smooth(sent_tokenized[x], sent_tokenized[x + 1]))
        perplxity = pow(calc, (1/self.count_bigrams(sent_sentences)))
        return perplxity
            
        #sent is een voorbeeld bigram
        
