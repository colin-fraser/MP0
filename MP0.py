import random 
import os
import string
import sys
import re
from collections import Counter

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

delimiters = " |\t|,|;|\.|\?|\!|-|:|@|\[|\]|\(|\)|\{|\}|_|\*|\/|\n"

test_in = """Billy_Reeves
Smorz
Nationalist_Left_-_Youth
Ancient_Greek_units_of_measurement
Jiuting_(Shanghai_Metro)
Blodgett,_MO
Baekjeong
Matt_Brinkman
National_Vietnam_Veterans_Art_Museum
Optique_et_Precision_de_Levallois
Tempo_(chess)
Nitrosyl_tetrafluoroborate
Bay_of_Whales
Barton_Myers
Sam_Pitroda
Text_normalization
Densetsu_no_Stafy"""

def listify(s, indexes, delimiters=delimiters):
    lines = s.split('\n')
    titles = [lines[i] for i in indexes]
    l = [re.split(delimiters, k) for k in titles]
    out = []
    for item in l:
        out += item
    return [item.lower() for item in out if item]

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

def process(userID):
    indexes = getIndexes(userID)
    raw_in = sys.stdin.read()
    processed_in = listify(raw_in, indexes)
    ret = handle_tokens(processed_in)
    for word in ret:
        print word

def compare(a, b):
    if a[1] > b[1]:
        return -1
    elif a[1] < b[1]:
        return 1
    else:
        if a[0] < b[0]:
            return -1
        elif a[0] == b[0]:
            return 0
        return 1

def handle_tokens(tokens):
    tokens = [t for t in tokens if t not in stopWordsList]
    counts = Counter(tokens)
    mc = counts.most_common(20)
    mc.sort(compare)
    ret = [k[0] for k in mc]
    return ret


process(sys.argv[1])