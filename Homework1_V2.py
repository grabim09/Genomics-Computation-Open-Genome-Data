#!/usr/bin/env python
# coding: utf-8

# In[60]:


import numpy as np
import pandas as pd
import streamlit as st


# In[69]:


sequence_count = 0
header = []
sequence = []


# In[73]:


def fasta_parser(file):
    count = 0
    with open(file, 'r') as fasta_file:
        seq = ""
        for line in fasta_file:
            line = line.strip()
            if line.startswith(">"):
                header.append(line)
                if seq:
                    sequence.append(seq)
                seq = ""
#                 sequence_count += 1
                count += 1
            else:
                seq += line
        if seq:
            sequence.append(seq)
#     print(str(sequence_count) + " Sequence")
#     for i in range(sequence_count):
#         print("Header:", header[i])
#         print("Sequence:", sequence[i])
    sequence_count = count
    st.write("Sequence Amount: " + str(sequence_count) + " Sequence")
    for i in range(sequence_count):
        st.write("Header {}: {}".format(i, header[i]))
        st.write("Sequence {}: {}".format(i, sequence[i]))


# In[74]:


def countNucs(instring):
    # will count upper and lower case sequences, if do not want lower case remove .upper()
    c = instring.upper().count('C')
    g = instring.upper().count('G') 
    a = instring.upper().count('A')
    t = instring.upper().count('T')
    st.write('C = {}, G = {}, A = {}, T = {}'.format(c, g, a, t))
#     return 'C = {}, G = {}, A = {}, T = {}'.format(c, g, a, t)


# In[76]:


def main():
    st.title("07311940000046_Agra Bima Yuda_Genomics Computation_Homework 1")
    st.selectbox(
        "Please select available genome data below!",
        ("A", "B", "Mobile phone"))
#     st.divider()
    fasta_parser("M14707.1[1..7478].fa")
    countNucs(sequence[sequence_count-1])
    
if __name__ == "__main__":
    main()


# In[ ]:




