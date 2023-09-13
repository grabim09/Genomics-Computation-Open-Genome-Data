#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st
import os


# In[8]:


allowed_extensions = ['fasta','fa']
sequence_count = 0
header = []
sequence = []


# In[9]:


def file_reader():
    file_names = [fn for fn in os.listdir()
              if any(fn.endswith(ext) for ext in allowed_extensions)]
    file_names.sort()
    chosen_file = st.selectbox("Please select available genome data below!",file_names)
    return chosen_file


# In[10]:


def count_nucleotide(seq_num,sequence_string):
    # will count upper and lower case sequences, if do not want lower case remove .upper()
    c = sequence_string.upper().count('C')
    g = sequence_string.upper().count('G') 
    a = sequence_string.upper().count('A')
    t = sequence_string.upper().count('T')
    st.write("Frequency of each nucleotide in sequence {}: C = {}, G = {}, A = {}, T = {}".format(seq_num, c, g, a, t))


# In[11]:


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
        st.write("Sequence {}: {}......{}".format((i+1), sequence[i][0:11], sequence[i][-12:-1]))
        st.write("Sequence {} Length: {}".format((i+1), len(sequence[i])))
        count_nucleotide((i+1), sequence[i])


# In[12]:


def main():
    st.title("07311940000046_Agra Bima Yuda_Genomics Computation_Open Genome Data")
    st.divider()
    fasta_parser(file_reader())
    
if __name__ == "__main__":
    main()

