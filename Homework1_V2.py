#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
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
    file_names = [fn for fn in os.listdir()
              if any(fn.endswith(ext) for ext in allowed_extensions)]
    file_names.sort()
    chosen_file = st.selectbox("Please select available genome data below!",file_names)
    return chosen_file


# In[10]:


def count_nitrogen_base(seq_num,sequence_length,sequence_string):
    # will count upper and lower case sequences, if do not want lower case remove .upper()
#     text = "Frequency of each nitrogen base in sequence {}:".format(seq_num)
    text = "Frequency of each nitrogen base:"
    for i in range(4):
        nbc[i] = sequence_string.upper().count(nbn[i])
        nbf[i] = float(nbc[i]/sequence_length)
        nbt = "{} = {} ({:.2f}%)".format(nbn[i], nbc[i], nbf[i])
        if i == 3:
            nbt = " and " + nbt
#             nbt = " and {} = {}".format(nbn[i], nbc[i])
        else:
            nbt = " " + nbt + ","
#             nbt = " {} = {},".format(nbn[i], nbc[i])
        text = text + nbt
    st.write(text)
#     C = sequence_string.upper().count('C')
#     G = sequence_string.upper().count('G') 
#     A = sequence_string.upper().count('A')
#     T = sequence_string.upper().count('T')
#     st.write("Frequency of each nucleotide in sequence {}: {} = {}, {} = {}, {} = {}, and {} = {}".
#              format(seq_num, nbn[0], nbc[0], nbn[1], nbc[1], nbn[2], nbc[2], nbn[3], nbc[3]))


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
        count_nitrogen_base((i+1), len(sequence[i]), sequence[i])


# In[ ]:


def sequence_chart():
    fig = plt.figure(figsize=(8,3)) 
    plt.barh(nbn, nbc)
    for index, value in enumerate(nbc):
        plt.text(value, index, str(value))
    num = max(nbc)
    i = 0
    while (num > 9):
#         print( number % 10);
        num = num / 10
        i += 1
    st.write(floor(num))
    st.write(i)
#     plt.xlim(0, 60)
    plt.xlabel('Nitrogen Base Count')
    plt.ylabel('Nitrogen Base Code')
    st.pyplot(fig)


# In[12]:


def main():
    st.title("07311940000046_Agra Bima Yuda_Genomics Computation_Open Genome Data")
    st.divider()
    fasta_parser(file_reader())
    sequence_chart()
    
if __name__ == "__main__":
    main()

