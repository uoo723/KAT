from Lecture2Vec import Lecture2Vec
from Predictor import Predictor
from konlpy.tag import Twitter
import sys

if __name__ == "__main__":
    # model = Lecture2Vec(university=sys.argv[1], campus=sys.argv[2])
    # model.build(corpus=sys.argv[3], distinct=int(sys.argv[4]))
    pred = Predictor(distinct=2)
    t = Twitter()
    positive = t.nouns(sys.argv[1])
    negative = []
    if (len(sys.argv) == 3):
        negative = t.nouns(sys.argv[2])
    print(pred.top_rank(positive=positive, negative=negative, threshold=0))
