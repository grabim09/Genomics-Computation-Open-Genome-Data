#!/usr/bin/env python
# coding: utf-8

# In[130]:


import streamlit as st
import os
import numpy as np
import pandas as pd


# In[131]:


included_extensions = ['fasta','fa']
sequence_count = 0
header = []
sequence = []


# In[133]:


def file_reader():
    file_names = [fn for fn in os.listdir()
              if any(fn.endswith(ext) for ext in included_extensions)]
    file_names.sort()
    chosen_file = st.selectbox("Please select available genome data below!",file_names)
    return chosen_file


# In[141]:


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
    st.write("Sequence amount inside the chosen file: " + str(sequence_count) + " Sequence")
    st.divider()
    for i in range(sequence_count):
        st.write("Header {}: {}".format(i, header[i]))
        st.write("Sequence {}: {}...{}".format(i, sequence[i][0:9], sequence[i][-10:-1]))
        c = sequence[i].upper().count('C')
        g = sequence[i].upper().count('G') 
        a = sequence[i].upper().count('A')
        t = sequence[i].upper().count('T')
        st.write("Frequency of each nucleotide in sequence {}: C = {}, G = {}, A = {}, T = {}".format(i, c, g, a, t))
        st.divider()


# In[135]:


def countNucs(instring):
    # will count upper and lower case sequences, if do not want lower case remove .upper()
    c = instring.upper().count('C')
    g = instring.upper().count('G') 
    a = instring.upper().count('A')
    t = instring.upper().count('T')
    st.write("Frequency of each nucleotide: C = {}, G = {}, A = {}, T = {}".format(c, g, a, t))
#     return 'C = {}, G = {}, A = {}, T = {}'.format(c, g, a, t)


# In[137]:


def main():
    st.title("07311940000046_Agra Bima Yuda_Genomics Computation_Open Genome Data")
    fasta_parser(file_reader())
    countNucs(sequence[sequence_count-1])
    
if __name__ == "__main__":
    main()

