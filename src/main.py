from Lecture2Vec import Lecture2Vec
from Predictor import Predictor
from konlpy.tag import Twitter
from konlpy.tag import Mecab
import argparse, os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', "--build", type=bool, default=False, help="모델 제작 True/False")
    parser.add_argument('-v', "--vocab", type=str, default="corpus/vocab", help="디렉토리 위치 corpus/<folder_name>")
    parser.add_argument('-c', "--corpus", type=str, default="corpus/train", help="디렉토리 위치 corpus/<folder_name >")
    parser.add_argument('-t', "--token", type=str, default="X", help="토크나이저 사용 여부 True/False")
    parser.add_argument('-d', "--dist", type=bool, default=True, help="vocab, corpus 구분 True/False")
    parser.add_argument('-p', "--pred", type=bool, default=True, help="예측기 사용 여부 True/False")
    parser.add_argument('-n', '--name', type=str, default='data/word_vector.bin', help="워드벡터 저장 위치 data/<binary file name>.bin")
    args = parser.parse_args()

    rows, columns = os.popen('stty size', 'r').read().split()

    print("\nparser statement")
    print("-" * rows)
    print("build:\t", args.build)
    print("vocab:\t", args.vocab)
    print("corpus:\t", args.corpus)
    print("token:\t", args.token)
    print("dist:\t", args.dist)
    print("pred:\t", args.pred)
    print("name:\t", args.name)
    print("\n")

    if (args.build == True):
        print("Build Model")
        model = Lecture2Vec()
        model.build(vocab=args.vocab, corpus=args.corpus, distinct=args.dist, name=args.name)
    
    
    # positive = t.nouns(args.positive)
    # if (args.negative != ""):
    #     negative = t.nouns(args.negative)

    print("\n\n")

    if (args.pred == True):
        print("Predict lecture")
        pred = Predictor(name=args.name)

        if (args.token == 'Twitter'):
            t = Twitter()
        elif (args.token == 'Mecab'):
            t = Mecab()
        else:
            print("No tokenizer")

        infile = open('corpus/vocab/name.txt', 'r')
        lectures = infile.readlines()
        for lecture in lectures:
            token = lecture
            if (args.token == "Twitter" or args.token == "Mecab"):
                print("Using tokenizer: ", args.token)
                token = t.nouns(lecture)
            else:
                print("Using tokenizer: Mecab")
                t = Mecab()
                token = t.nouns(lecture)
            print(lecture, " | ", token, "\n", "-" * 80)
            if (len(token) != 0):
                print(pred.top_rank(positive=token, negative="", threshold=0))
            else:
                print("한글 단어 없음.")
            print("\n")
