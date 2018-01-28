
# coding: utf-8

# ### Problem Statement
# 
# Implement a function longestWord() that takes a list of words and returns the longest
# one.

# In[7]:


def longestWord(wordlist):
    longest_word = None
    for x in wordlist:
        longest_word_length = len(longest_word) if longest_word != None else 0
        if len(x) > longest_word_length:
            longest_word = x
    return longest_word
    


# In[11]:


longestWord(["Ramaraju","Buddharaju","venkata"])


# In[13]:


longestWord([])

