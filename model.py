import string
import nltk
import re
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
                    if token in cleanlist:  # Count words while looping over the text
                        self.wordcount[token] += 1
                    else:
                        self.wordcount[token] = 1
                    cleanlist.append(token)
            cleanlist.append(endmark)
        return cleanlist
    def wordsintext(self,w):
        nr_of_words = 0
        for x in self.tokens:
            if x == w:
                nr_of_words +=1
        return nr_of_words
    

    def p_raw(self, w, w_n):
        aantalw = BigramModel.wordsintext(w)
        aantalw_n = BigramModel.wordsintext(w_n)
        chance_of_w_n = (aantalw_n / aantalw) * 100
        return chance_of_w_n

    def p_smooth(self,w, w_n):
        w_n_smooth = BigramModel.wordsintext(w_n)
        if w_n_smooth == 0:
            w_n_smooth == w_n_smooth + 1
        else: 
            w_n_smooth == w_n_smooth
            
        aantalw = BigramModel.wordsintext(w)
        aantalw_n = w_n_smooth
        chance_of_w_n = (aantalw_n / aantalw) * 100
        return chance_of_w_n

    def successors(self, w):
      #  if re.search(r"\bhim\b", line.lower())
      w_i = []
     elist_wi_ci = []
      d = re.findall()e
      for result in d:
          list_wi_ci.append(( d[result], BigramModel.p_raw(w, d[result])))

              
          
      return list_wi_ci
              
#Return a list of pairs (w_i, c_i) , where w_i is a token that
#might follow w , and c_i is its raw (unsmoothed) bigram
#probability, P_r(w_i | w) . Tokens with zero probability need
#not be included in the result.
        
    
    def perplexity(self, sent):
        pass


