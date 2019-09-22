import json
import numpy as np
import pandas as pd
import time

start = time.time()
json_data=open('data1.json').read()
data = json.loads(json_data)

'''
data = [{'en': 'tall house', 'fr': 'grande maison'},
		{'en': 'blue house', 'fr': 'maison bleu'},
		{'en': 'he is tall', 'fr': 'il est grande'},
		{'en': 'he likes blue', 'fr': 'il aime le bleu'},
        {'en': 'the house', 'fr': 'le maison'}]
'''
#Finding all unique french and english words in the dataset
unique_french = []
unique_english = []
for i in range(len(data)):
    f = data[i]['fr'].split(' ')
    e = data[i]['en'].split(' ')
    for j in range(len(f)):
        if f[j] not in unique_french:
            unique_french.append(f[j])
    for j in range(len(e)):
        if e[j] not in unique_english:
            unique_english.append(e[j])
			
#Initializing t(e|f) uniformly
d = np.ones(shape=(len(unique_french),len(unique_english)))
t = pd.DataFrame(d, columns=unique_english, index=unique_french)
for i in range(len(unique_french)):
    for j in range(len(unique_english)):
        t.iloc[i][j] = t.iloc[i][j]/len(unique_english)
	
#Running EM Algorithm till t(e|f) is converged
for loop in range(50):
    d = np.zeros(shape=(len(unique_french),len(unique_english)))
    count = pd.DataFrame(d, columns=unique_english)
    total = np.zeros(len(unique_french))
    s_total = dict()
    for i in range(len(data)):
        e = data[i]['en'].split(' ')
        for j in e:
            for find in range(len(unique_english)):
                if j == unique_english[find]:
                    ei = find
            s_total[j] = 0
            f = data[i]['fr'].split(' ')
            for k in f:
                for find in range(len(unique_french)):
                    if k == unique_french[find]:
                        fi = find
                s_total[j] = s_total[j] + t.iloc[fi][ei]
        for j in e:
            for find in range(len(unique_english)):
                if j == unique_english[find]:
                    ei = find
            for k in f:
                for find in range(len(unique_french)):
                    if k == unique_french[find]:
                        fi = find
                count.iloc[fi,ei] = count.iloc[fi,ei] + t.iloc[fi,ei]/s_total[j]
                total[fi] = total[fi] + t.iloc[fi,ei]/s_total[j]
    for i in range(len(unique_french)):
        for j in range(len(unique_english)):
            t.iloc[i][j] = count.iloc[i][j]/total[i]
t = np.round(t, decimals=3)


#Alignment of the words
maximums = t.idxmax(axis=0)
mapping = dict()
for i in unique_english:
    mapping[i] = maximums[i]
for i in range(len(data)):
    f = data[i]['fr'].split()
    e = data[i]['en'].split()
    l1 = []
    l2 = []
    for j in e:
        #if mapping[j] in f:
        l1.append(mapping[j])
    for j in l1:
        flag = 0
        for find in range(len(f)):
            if f[find] == j:
                flag = 1
                l2.append(find+1)
        if flag == 0:
            l2.append(0)
    for i in range(len(l2)):
        if l2[i] != 0:
            print('{}->{}'.format(i+1,l2[i]))
    print('\n')
	
finish = time.time()
print(finish-start)