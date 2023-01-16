from nltk.corpus.reader.bnc import BNCCorpusReader
from statistics import mean
from collections import defaultdict
from tqdm import tqdm

genres = ['aca', 'fic', 'news']

for genre in genres:
  print('Genre: ', genre)

  sent_lens = []
  word_lens = []
  pos = defaultdict(int)

  bnc_reader = BNCCorpusReader(root=f'/local/kurs/digphil/swegram/BNC-baby/{genre}/', fileids=r'[A-K]\w*\w*\.xml')

  sents = bnc_reader.tagged_sents()
  print(sents[0]) # for some reason this line prevents the next line from causing an error
  for sent in tqdm(sents):
    l = len(sents)
    for word in sent:
      word_lens.append(len(word[0]))
      if word[1] == 'PUN':      # un-count punctuations from sentence length
        l -= 1
      pos[word[1]] += 1     # count POS tags
    sent_lens.append(len(sent))

  total = sum(pos.values())

  for tag in pos:
    pos[tag] = pos[tag]/total       # calculate share of POS tags
  pos_ratio = sorted(pos.items(), reverse=True, key=lambda x: x[1])


  print('Mean sentence length: ', mean(sent_lens))
  print('Mean word length: ', mean(word_lens))
  print(pos_ratio)



