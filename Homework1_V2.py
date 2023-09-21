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
nbc = []
nbf = []
nbwc = []
nbwf = []
gcwc = []
gcwf = []
atwc = []
atwf = []


# In[9]:


def file_reader():
    file_names = [fn for fn in os.listdir() if any(fn.endswith(ext) for ext in allowed_extensions)]
    file_names.sort()
    chosen_file = st.selectbox("Please select available genome data below!",file_names)
    return chosen_file


# In[ ]:


def sequence_info(seq_num):
    st.write("Header {}: {}".format((seq_num+1), header[seq_num]))
    st.write("Sequence {}: {}......{}".format((seq_num+1), sequence[seq_num][0:11], sequence[seq_num][-12:-1]))
    st.write("Sequence {} Length: {}".format((seq_num+1), len(sequence[seq_num])))


# In[10]:


def count_nitrogen_base(seq_num,sequence_length,sequence_string):
    text = "Frequency of each nitrogen base in sequence {}:".format(seq_num+1)
#     text = "Nitrogen base frequency:"
    c = [0]*4
    f = [0]*4
    for i in range(4):
#         will count upper and lower case sequences, if do not want lower case remove .upper()
        c[i] = sequence_string.upper().count(nbn[i])
        f[i] = float((c[i]/sequence_length)*100)
        nbt = "{} = {} ({:.2f}%)".format(nbn[i], c[i], f[i])
#         nbc[i] = sequence_string.upper().count(nbn[i])
#         nbf[i] = float((nbc[i]/sequence_length)*100)
#         nbt = "{} = {} ({:.2f}%)".format(nbn[i], nbc[i], nbf[i])
        if i == 3:
            nbt = " and " + nbt
        else:
            nbt = " " + nbt + ","
        text = text + nbt
    nbc.append(c)
    nbf.append(f)
    st.write(text)
#     C = sequence_string.upper().count('C')
#     G = sequence_string.upper().count('G') 
#     A = sequence_string.upper().count('A')
#     T = sequence_string.upper().count('T')
#     st.write("Frequency of each nucleotide in sequence {}: {} = {}, {} = {}, {} = {}, and {} = {}".
#              format(seq_num, nbn[0], nbc[0], nbn[1], nbc[1], nbn[2], nbc[2], nbn[3], nbc[3]))


# In[ ]:


def sequence_chart(seq_num):
    fig = plt.figure(figsize=(16,2)) 
    plt.barh(nbn, nbc[seq_num])
    for index, value in enumerate(nbc[seq_num]):
        plt.text(value, index, str(value))
    num = max(nbc[seq_num])
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


# In[ ]:


def density(seq_num):
    win_len = 501
    left = round((win_len - 1) / 2)
    right = left
    n = len(sequence[seq_num])
    c = [0]*4
    f = [0]*4
    wc = []
    wf = []
    wgcc = []
    wgcf = []
    watc = []
    watf = []
    method = 1
    if method == 0:
        cnt = win_len
        m = left
        while m < n-right:
            for i in range(4):
                c[i] = sequence[seq_num].upper().count(nbn[0],m-l,m+r)
                f[i] = float((c[i]/cnt)*100)
            wc.append(c)
            wf.append(f)
            gcc.append(c[0] + c[1])
            gcf.append(f[0] + f[1])
            atc.append(c[2] + c[3])
            atf.append(f[2] + f[3])
#             gcc[m+left] = sequence[0].upper().count(nbn[0],l,r) + sequence[0].upper().count(nbn[1],l,r)
#             gcf[m+left] = float((gcc[m]/c)*100)
#             atc[m+left] = sequence[0].upper().count(nbn[2],l,r) + sequence[0].upper().count(nbn[3],l,r)
#             atf[m+left] = float((atc[m]/c)*100)
            m += 1
    else:
        for m in range(n):
            l = 0 if m - left < 0 else m - left
            r = n if m + right > n-1 else m + right
            cnt = r - l + 1
            for i in range(4):
                c[i] = sequence[seq_num].upper().count(nbn[i],l,r)
                f[i] = float((c[i]/cnt)*100)
            wc.append(c)
            wf.append(f)
            wgcc.append(c[0] + c[1])
            wgcf.append(f[0] + f[1])
            watc.append(c[2] + c[3])
            watf.append(f[2] + f[3])
        nbwc.append(wc)
        nbwf.append(wf)
        gcwc.append(wgcc)
        gcwf.append(wgcf)
        atwc.append(watc)
        atwf.append(watf)
#             gcc[m] = sequence[0].upper().count(nbn[0],l,r) + sequence[0].upper().count(nbn[1],l,r)
#             gcf[m] = float((gcc[m]/cnt)*100)
#             atc[m] = sequence[0].upper().count(nbn[2],l,r) + sequence[0].upper().count(nbn[3],l,r)
#             atf[m] = float((atc[m]/cnt)*100)
    col1, col2 = st.columns(2)
    with col1:
        fig = plt.figure(figsize=(8,2))
        for i in range(4):
            plt.plot(nbwf[seq_num][i], label = nbn[i])
#         plt.plot(nbwf[seq_num][], label = "GC Content")
#         plt.plot(atwf[seq_num], label = "AT Content")
        plt.legend()
        plt.xlabel("Position")
        plt.ylabel("Content (%)")
        st.pyplot(fig)
    with col2:
        fig = plt.figure(figsize=(8,2)) 
        plt.plot(gcwf[seq_num], label = "GC Content")
        plt.plot(atwf[seq_num], label = "AT Content")
        plt.legend()
        plt.xlabel("Position")
        plt.ylabel("Content (%)")
        st.pyplot(fig)


# In[11]:


def fasta_parser(file):
    # Reset variable
    nbc = []
    nbf = []
    nbwc = []
    nbwf = []
    gcwc = []
    gcwf = []
    atwc = []
    atwf = []
    # Stuff
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
    # Stuff
    col1, col2 = st.columns([3,1])
    with col1:
        st.write("Sequence amount inside the chosen file: " + str(sequence_count) + " Sequence")
    with col2:
        mult = st.checkbox("Show all sequence", value = True if sequence_count == 1 else False, disabled = True if sequence_count == 1 else False)
    if sequence_count > 1:
        if mult:
            i = 0
            j = sequence_count-1
        else:
            i = st.slider("Choose sequence", 1, sequence_count, value = 1, disabled = mult) - 1
            j = i
    else:
        i = 0
        j = 0
#     window = st.radio("Choose window type",["Quarter", "Percentage", "Documentary :movie_camera:"],
#     captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])
    while i <= j:
        st.divider()
        sequence_info(i)    
        count_nitrogen_base(i, len(sequence[i]), sequence[i])
        sequence_chart(i)
        density(i)
        i += 1
#     nbwc = [0]*len(sequence[0])
#     gcc = [0]*len(sequence[0])
#     gcf = [0]*len(sequence[0])
#     atc = [0]*len(sequence[0])
#     atf = [0]*len(sequence[0])
#     win_len = 501
#     left = round((win_len - 1) / 2)
#     right = left
#     n = len(sequence[0])
#     for m in range(n):
#         l = 0 if m - left < 0 else m - left
#         r = n if m + right > n-1 else m + right
#         c = r - l + 1
#         gcc[m] = sequence[0].upper().count(nbn[0],l,r) + sequence[0].upper().count(nbn[1],l,r)
#         gcf[m] = float((gcc[m]/c)*100)
#         atc[m] = sequence[0].upper().count(nbn[2],l,r) + sequence[0].upper().count(nbn[3],l,r)
#         atf[m] = float((atc[m]/c)*100)
#     fig = plt.figure(figsize=(16,4)) 
#     plt.plot(gcf, label = "GC Content")
#     plt.plot(atf, label = "AT Content")
#     plt.legend()
#     st.pyplot(fig)


# In[12]:


def main():
    st.set_page_config(layout = "wide")
    st.title("07311940000046_Agra Bima Yuda_Genomics Computation_Open Genome Data")
    st.divider()
    fasta_parser(file_reader())
    
if __name__ == "__main__":
    main()

