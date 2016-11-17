# input1: 04 Bascket_of_8 2005-2014 Documents - Non-Empty Abstracts - Contents - AB Cleaned
# input2: 05 stoplist.txt
# output1: 07 Bascket_of_8 2005-2014 Documents - Non-Empty Abstracts - Contents - cleaned
# output2: 08 LSI - similarities
# output3: 09 countdegree
import time
import re
import logging
from nltk import stem
from gensim import corpora, models, similarities
import os
os.chdir('C:\Users\moqri\Desktop')
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
porter = stem.porter.PorterStemmer()
cleanedfile='07 Bascket_of_8 2005-2014 Documents - Non-Empty Abstracts - Contents - cleaned.txt'
def docclean():
    documents=open('04 Bascket_of_8 2005-2014 Documents - Non-Empty Abstracts - Contents - AB Cleaned.txt')
    f= open ('05 stopList.txt')
    stoplist = set(f.read().replace("\n", " ").split())
    documents_clean0 = [[re.sub('[.!,;?()\W\d]+', '', word) for word in document.lower().split()] for document in documents]
    documents_clean = [[porter.stem(word) for word in document if word not in stoplist] for document in documents_clean0]
    with open(cleanedfile, 'w') as f:
        for line in documents_clean:f.write("%s\n" % ' '.join(line))

#docclean()
documents = open(cleanedfile)
documents_clean = [[word for word in document.split() ] for document in documents]
dictionary = corpora.Dictionary(documents_clean)
dictionary.filter_extremes(no_below=5)
dictionary.compactify() 
print dictionary

open('dictionary.txt', 'w').write(str(dictionary.token2id).replace(',', '\n'))


class MyCorpus(object):
    def __iter__(self):
        for line in open(cleanedfile):
            # assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(line.split())
corpus= MyCorpus() 
corpora.MmCorpus.serialize('deerwester.mm', corpus);corpus = corpora.MmCorpus('deerwester.mm')

tfidf = models.tfidfmodel.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=100) 
corpus_lsi=lsi[corpus_tfidf]

#lda=models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=10,chunksize=100, passes=10) 
#corpus_lda=lda[corpus]


def ls():
    index = similarities.MatrixSimilarity(corpus_lsi) 
    with open(cleanedfile, 'r') as f:
        lines = f.read().splitlines()
        sims = open('08 LSI - similarities.csv', 'w')
        countdegree= open('09 LSI - degreecount.csv', 'w')
        sims.write('source,target,weight,type\n')
        for i in range(0,2427):
            doc=lines[i]    
            vec_bow = dictionary.doc2bow(doc.split())
            vec_tran = lsi[tfidf[vec_bow]]
            simsinx = index[vec_tran]
            count=0;
            #for j in range(0,len(simsinx)):
                #if simsinx[j]>.5: 
                    #count=count+1
            #countdegree.write(str(i+1)+','+str(count-1));countdegree.write('\n')
            for j in range(i+1,len(simsinx)):
                if simsinx[j]>.49:                                        
                    sims.write(str(i+1)+','+str(j+1)+','+str(simsinx[j])+',undirected');sims.write('\n')

                        
def tf():
    index = similarities.MatrixSimilarity(corpus_tfidf) 
    with open(cleanedfile, 'r') as f:
        lines = f.read().splitlines()
        sims = open('similarities.csv', 'w')
        sims.write('source,target,weight,type,count\n')
        for i in range(i,2427):
            doc=lines[i]    
            vec_bow = dictionary.doc2bow(doc.split())
            vec_tran = tfidf[vec_bow]
            simsinx = index[vec_tran]
            for j in range(0,len(simsinx)):
                if simsinx[j]>.15: sims.write(str(i+1)+','+str(j+1)+','+str(simsinx[j])+',undirected');sims.write('\n')

def ld():
    index = similarities.MatrixSimilarity(corpus_lda) 
    with open(cleanedfile, 'r') as f:
        lines = f.read().splitlines()
        sims = open('similaritiesLDA.csv', 'w')
        sims.write('source,target,weight,type\n')
        for i in range(i,2427):
            doc=lines[i]    
            vec_bow = dictionary.doc2bow(doc.split())
            vec_tran = lda[tfidf[vec_bow]]
            simsinx = index[vec_tran]
            for j in range(0,len(simsinx)):
                if simsinx[j]>.2: sims.write(str(i+1)+','+str(j+1)+','+str(simsinx[j])+',undirected');sims.write('\n')
ls()
