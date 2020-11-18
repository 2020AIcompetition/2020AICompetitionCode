import pandas as pd
import jieba.analyse
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from collections import defaultdict
import math
import operator

#大纲词汇txt
dict_path = 'F:\\Compition-buaa\\page\\dict_list.txt'
#每篇文章一个txt
passage_path = 'F:\\Compition-buaa\\page\\2.txt'

def dict_list(dict_path):
    dict_file = open(dict_path,encoding='utf-8')
    dict_list = []
    for i in dict_file.readlines():
        try:
            word = i.split('\t')[0]
            dict_list.append(word.lower())
        except error:
            print("error",word)
            break
    return dict_list



def passage_info(passage_path,dict_list):
    import re
    def remove(text):
        remove_chars = '[0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
        return re.sub(remove_chars, '', text)

    f = open(passage_path, encoding='utf8')
    count_st = 0
    count_wd = 0
    difficult_wd = 0
    difficult_level = 0
    w = 0.33333
    difficult_word_list = []
    word_list = []
    sentence = []
    for line in f.readlines():
        sentence = sentence + sent_tokenize(line)
        word_list = word_list + word_tokenize(line)
        word_list = [remove(i) for i in word_list if (remove(i) != '')&(len(i)>2)]
        count_st = len(sentence)
        count_wd = len(word_list)
    f.close()
    word_list = [i.strip(",").strip('"').lower() for i in word_list]
    for i in word_list:
        if i not in dict_list:
            difficult_word_list.append(i)
    difficult_len = len(difficult_word_list)
    difficult_sent_count = len([len(word_tokenize(i)) for i in sentence if len(word_tokenize(i))>30])
    difficult_level = difficult_sent_count/len(sentence)*w + difficult_len/count_wd*w + len(sentence)/100*w
    return count_st,count_wd,word_list,sentence,difficult_word_list,difficult_len,difficult_level



dict = dict_list(dict_path)
count_st,count_wd,word_list,sentence,difficult_word_list,difficult_len,difficult_level = passage_info(passage_path,dict)


