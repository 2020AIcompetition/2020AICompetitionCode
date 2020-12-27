import pandas as pd
# df1  = pd.DataFrame([1,2],
#                     [3,5])
# df2  = pd.DataFrame([2,3],
#                     [7,8])
# df = pd.merge(df1, df2,)
# print(df)
# print(df1.index)
# print("dddd")
#pd.get_dummies()
import numpy as np
import wordcloud as wc

import numpy as np
real_exam = pd.read_excel(r"C:\Users\Administrator\Desktop\RealExam.xlsx")
#print(real_exam.head)

word_cloud_data = real_exam.iloc[:45,3:4].to_string()
#word_cloud_data = word_cloud_data.to_string()
print(type(word_cloud_data))
txt = "I love Summer"
wc_ = wc.WordCloud(background_color= 'white', max_words=200\
                  )
wc_.generate(word_cloud_data)
print(wc)
wc_.to_file("wc.png")

# 推荐考研文章
economist = pd.read_excel(r"C:\Users\Administrator\Desktop\Economist.xlsx")

res = pd.merge(real_exam,economist, on = ['keywords'])
#print(res)

key_words_real = economist['keywords'].str.split(',', expand = True).to_string()
wc_key = wc.WordCloud( background_color= 'white',max_words=200, stopwords=['year','week','people','time'\
                                                                      'american','america','world'])
wc_key.generate(key_words_real)
wc_key.to_file("wc_key1.png")
#print(key_words_real)
print(type(economist['keywords'].str.split(',', expand = True)))
#key_words_real.str.split(',', expand = True)

key_words_econ = real_exam['keywords'].str.split(',', expand = True).to_string()
wc_key_econ = wc.WordCloud( background_color='white',max_words=200,stopwords=['year','week','people','time'\
                                                                      'american','america','world'])
wc_key_econ.generate(key_words_real)
wc_key_econ.to_file("wc_key_econ1.png")

m1 = economist['keywords'].str.split(',', expand = True)
m1['paperid'] = economist['newsId']
m2 = real_exam['keywords'].str.split(',', expand = True)
reco_artical = pd.merge(m2, m1, on= [0])
print(reco_artical)

