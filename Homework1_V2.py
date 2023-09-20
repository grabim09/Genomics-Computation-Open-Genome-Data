#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import math
import matplotlib.pyplot as plt
import streamlit as st


# In[8]:


allowed_extensions = ['fasta','fa']
sequence_count = 0
header = []
sequence = []
nbn = ['G', 'C', 'A', 'T']
nbc = [0]*4
nbf = [0]*4


# In[9]:


def file_reader():
    file_names = [fn for fn in os.listdir() if any(fn.endswith(ext) for ext in allowed_extensions)]
    file_names.sort()
    chosen_file = st.selectbox("Please select available genome data below!",file_names)
    return chosen_file


# In[10]:


def count_nitrogen_base(seq_num,sequence_length,sequence_string):
#     text = "Frequency of each nitrogen base in sequence {}:".format(seq_num)
    text = "Nitrogen base frequency:"
    for i in range(4):
#         will count upper and lower case sequences, if do not want lower case remove .upper()
        nbc[i] = sequence_string.upper().count(nbn[i])
        nbf[i] = float(nbc[i]/sequence_length)
        nbt = "{} = {} ({:.2f}%)".format(nbn[i], nbc[i], nbf[i])
        if i == 3:
            nbt = " and " + nbt
        else:
            nbt = " " + nbt + ","
        text = text + nbt
    st.write(text)
#     C = sequence_string.upper().count('C')
#     G = sequence_string.upper().count('G') 
#     A = sequence_string.upper().count('A')
#     T = sequence_string.upper().count('T')
#     st.write("Frequency of each nucleotide in sequence {}: {} = {}, {} = {}, {} = {}, and {} = {}".
#              format(seq_num, nbn[0], nbc[0], nbn[1], nbc[1], nbn[2], nbc[2], nbn[3], nbc[3]))


# In[ ]:


def sequence_chart():
    fig = plt.figure(figsize=(8,2)) 
    plt.barh(nbn, nbc)
    for index, value in enumerate(nbc):
        plt.text(value, index, str(value))
    num = max(nbc)
    i = 0
    while (num > 10):
        num2 = num%10
        num = math.floor(num/10)
        i += 1
#     max_x = (num*10)*(10**(i))
    max_x = ((num*10)+num2+5)*(10**(i-1))
#     st.write("{} {} {} {}".format(num, num2, i, max_x))
    plt.xlim(0, max_x)
    plt.xlabel('Nitrogen Base Count')
    plt.ylabel('Nitrogen Base Code')
    st.pyplot(fig)


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
#         st.write("Sequence {}: {}......{}".format((i+1), sequence[i][0:11], sequence[i][-12:-1]))
#         st.write("Sequence {} Length: {}".format((i+1), len(sequence[i])))
        st.write("Sequence {}: {}......{} with total length of {}".
                 format((i+1), sequence[i][0:11], sequence[i][-12:-1], len(sequence[i])))
        count_nitrogen_base((i+1), len(sequence[i]), sequence[i])
        sequence_chart()


# In[12]:


def main():
    st.title("07311940000046_Agra Bima Yuda_Genomics Computation_Open Genome Data")
    st.divider()
    fasta_parser(file_reader())
    
if __name__ == "__main__":
    main()

