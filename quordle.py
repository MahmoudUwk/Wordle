# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 21:48:53 2022

@author: mahmo
"""
import string
import numpy as np

def dict_freq(dict_in):
    letter_frequency_dict = dict.fromkeys(string.ascii_lowercase,0)
    for letter in string.ascii_lowercase:
        for word_f in dict_in:
            letter_frequency_dict[letter] = letter_frequency_dict[letter] + int(letter in word_f)      
    return letter_frequency_dict
# words = open(dictionary_eng_path, 'r').read()

def ent_dic(filter_words,filter_freq):
    tot_freq = sum(list(filter_freq.values()))
    entropy_weigths = []
    for word in filter_words:
        ent_i = 0
        word_uniqe = set(list(word))
        for ltr in word_uniqe:
            if ltr in string.ascii_lowercase:
                p_i = filter_freq[ltr]/tot_freq
            if p_i !=0:
                ent_i = ent_i - p_i * np.log2(p_i)
        entropy_weigths.append(ent_i)
        
    indeces = np.flip(np.argsort(entropy_weigths))
    words_sorted = [filter_words[ind] for ind in indeces]
    return words_sorted

def get_constraints(letters_out,outpos_ltr,outpos_num,pos_ltr,pos_num):
    letters_out = list(set([ltr for ltr in letters_out]))
    letters_outpos = [ [outpos_ltr[ind],outpos_num[ind]]  for ind in range(len(outpos_ltr))]
    letters_pos = [ [pos_ltr[ind],pos_num[ind]]  for ind in range(len(pos_ltr))]
    letters_in = pos_ltr+outpos_ltr
    letters_in = list(set([ltr for ltr in letters_in]))
    return letters_out,letters_in,letters_outpos,letters_pos

def elinimate(letters_out,letters_in,letters_outpos,letters_pos,words_five_letters):
    filter_words = []
    for word in words_five_letters:
        flag_in = 1
        flag_out = 1
        flag_pos = 1
        flag_outpos = 1
        for ltr in letters_in:
            flag_in  = flag_in * int(ltr in word)
        for ltr in letters_out:
            flag_out = flag_out * (1-int(ltr in word))
        if len(letters_pos) !=0:
            for pair in letters_pos:
                ltr = pair[0]
                pos = pair[1]
                flag_pos = flag_pos * int(word[pos] == ltr)
        if len(letters_outpos) !=0:
            for pair in letters_outpos:
                ltr = pair[0]
                pos = pair[1]
                flag_outpos = flag_outpos * (1-int(word[pos] == ltr))
        word_flag = flag_in * flag_out * flag_pos * flag_outpos
        if word_flag:
            filter_words.append(word)
    return filter_words

#%%
# dictionary_eng_path = 'C:\\Users\\mahmo\\OneDrive\\Desktop\\words_alpha.txt'
dictionary_eng_path = 'C:\\Users\\mahmo\\OneDrive\\Desktop\\usa.txt'
with open(dictionary_eng_path, 'r') as file:
    words = file.read().lower().splitlines()
    
words_five_letters = [word for word in words if len(word)==5 and (1-int("'"  in word))]


five_letter_frequency_dict = dict_freq(words_five_letters)
        
        
best_initial_guess = ent_dic(words_five_letters,five_letter_frequency_dict)
# print('Best initial guess:',best_initial_guess[0:6])
#e s a r o --> arose
#i t l n d u
#arose
#%%
# ['',]
letters_out = ['arselinsmcadgmascld','rselinsch','areinmhagma','aroelomochadogmacold']
outpos_ltr = ['oh','aom','slsocd','sis']
outpos_num = [[1,3],[0,2,0],[3,0,4,1,2,0],[3,1,4]]
pos_ltr = ['o','dogma','scold','ns']
pos_num = [[2],[0,1,2,3,4],[0,1,2,3,4],[3,0]]
filter_words_joint = []
for quord in range(4):
    l_out,l_in,l_outpos,ls_pos = get_constraints(letters_out[quord],outpos_ltr[quord],outpos_num[quord],pos_ltr[quord],pos_num[quord])
    filter_words = elinimate(l_out,l_in,l_outpos,ls_pos,words_five_letters)
    filter_words_joint.append(filter_words)
filter_words_joint_flat = [word for sub_list in filter_words_joint for word in sub_list]
filter_words_joint_flat = list(set(filter_words_joint_flat))
print("List of lists:",filter_words_joint)
filter_freq = dict_freq(filter_words_joint_flat)

guess_word = ent_dic(filter_words_joint_flat,filter_freq)

print("Best guesses:",guess_word[0:6])

#%%    
# import numpy as np
# import matplotlib.pyplot as plt   
# trials = [2,3,4,4,5,5,6,2,5,4,5,4,6,2,4,5,4,4,5,3,4,3,3,4,4,4,3,3,6,3,4,4,4,4,3,6,4,3,3,5,3,4,3,3,4,3,5,3,2,6,3,5,4,3,5,4,4,4,4,4,3,4,4,3,6,5,4,4]
# succ = len(trials)     
# trial_fails = [1,1]
# fails = len(trial_fails)
# succ_ratio = succ / (succ+fails)
        


# n, bins, patches = plt.hist(trials,bins=range(2,8), align='left', rwidth=0.5 )


# plt.xlabel('Number of guesses used')
# plt.ylabel('Count')
# plt.title('Histogram of number of trials used to correctly guess the word')
# # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# # plt.xlim(40, 160)
# # plt.ylim(0, 0.03)
# plt.grid(True)
# plt.show()









