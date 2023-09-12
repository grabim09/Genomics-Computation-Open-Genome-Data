#!/usr/bin/env python
# coding: utf-8

# In[143]:


import streamlit as st
import os
import numpy as np
import pandas as pd


# In[144]:


included_extensions = ['fasta','fa']
sequence_count = 0
header = []
sequence = []


# In[145]:


def file_reader():
    file_names = [fn for fn in os.listdir()
              if any(fn.endswith(ext) for ext in included_extensions)]
    file_names.sort()
    chosen_file = st.selectbox("Please select available genome data below!",file_names)
    return chosen_file


# In[146]:


def countNucs(sequence_number,sequence_string):
    # will count upper and lower case sequences, if do not want lower case remove .upper()
    c = sequence_string.upper().count('C')
    g = sequence_string.upper().count('G') 
    a = sequence_string.upper().count('A')
    t = sequence_string.upper().count('T')
    st.write("Frequency of each nucleotide in sequence {}: C = {}, G = {}, A = {}, T = {}".format((i+1), c, g, a, t))


# In[147]:


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
                count += 1
            else:
                seq += line
        if seq:
            sequence.append(seq)
    sequence_count = count
    st.write("Sequence amount inside the chosen file: " + str(sequence_count) + " Sequence")
    for i in range(sequence_count):
        st.divider()
        st.write("Header {}: {}".format((i+1), header[i]))
        st.write("Sequence {}: {}...{}".format((i+1), sequence[i][0:9], sequence[i][-10:-1]))
        countNucs((i+1), sequence[i])


# In[148]:


def main():
    st.title("07311940000046_Agra Bima Yuda_Genomics Computation_Open Genome Data")
    fasta_parser(file_reader())
    
if __name__ == "__main__":
    main()

