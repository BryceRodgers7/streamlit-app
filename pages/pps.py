import streamlit as st
from menu import menu_with_redirect
import io
import json
import os
from PIL import Image
import requests
import time
import getpass
from random import randrange

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verify the user's role
if st.session_state.role not in ["user", "admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title("Data Collection and Processing")
st.subheader("Processing, Sanitizing, Tokenizing")

colab = "https://colab.research.google.com/drive/10XLZlovVfBLhaw60EJtBp2BPvRK2Edsf?usp=sharing"
st.write("full jupyter notebook found [here](%s)" % colab)
movie_script = "https://d2bu9v0mnky9ur.cloudfront.net/academy2021/scripts/duneMxFtT98NYwBsMltl20211109/dune_final_shooting_script_6_19_20.pdf"
st.write("#1: obtain the raw data: [here](%s) the final shooting script for Dune 2020." % movie_script)


# File path of the PDF file to display (replace with your own file)
pdf_file = "app/static/dune_one_page.pdf"

# Open the PDF file in binary mode
with open(pdf_file, "rb") as file:
    # Read the PDF file
    pdf_bytes = file.read()
    
# Display the PDF using an iframe
st.markdown(f'<iframe src="data:application/pdf;base64,{pdf_bytes.decode("ISO-8859-1")}" width="700" height="800"></iframe>', unsafe_allow_html=True)

st.write("#2: inspect the data, notice there are 'random' numbers and codes all over the place, plus it has plenty of formatting, deleted scenes and movie-instructions")
divvy_code = '''chp_start_idx_bk1 = [11, 184, 310, 422, 571, 635, 729, 888, 1010, 1065, 1201, 1278, 1514, 1601, 1651, 2031, 2604, 2780, 2832, 3043, 3252]
chp_start_idx_bk2 = [3260, 3334, 3539, 3762, 3976, 4226, 4351, 4510, 4606, 4784, 4907, 5101, 5318, 5616, 5765, 6010 ]
chp_start_idx_bk3 = [6018, 6162, 6279, 6460, 6621, 6743, 7021, 7236, 7396, 7552, 7689, 8055 ]'''

st.code(divvy_code, language="python")

st.write("#3: Sanitize the corpus")
st.write("  lower-case, remove punctuation, remove stop words, remove non-alphanumeric, stem, lemmatize")

st.write("#4: Create TDF matrix")
tdf_matrix_code = '''vocabulary = sorted(set(word for doc in preprocessed_corpus for word in doc.split()))

# start with empty matrix
tdf_matrix = np.zeros((len(preprocessed_corpus), len(vocabulary)), dtype=int)

# scan corpus, fill matrix
for doc_idx, doc in enumerate(preprocessed_corpus):
    for term in doc.split():
        term_idx = vocabulary.index(term)
        tdf_matrix[doc_idx, term_idx] += 1'''
st.code(tdf_matrix_code, language="python")

st.write("#5: Create TF-IDF matrix")
tfidf_matrix_code = '''# Compute Term Frequency matrix
tf_matrix = tdf_matrix / np.sum(tdf_matrix, axis=1, keepdims=True)

# Compute Inverse Document Frequency matrix
num_documents = tdf_matrix.shape[0]
idf_vector = np.log(num_documents / np.count_nonzero(tdf_matrix, axis=0))

# Compute TF-IDF matrix
tfidf_matrix = tf_matrix * idf_vector'''
st.code(tfidf_matrix_code, language="python")

st.write("  we can see that the number of unique words in a corpus will have an impact on the entire matrix (both tdf and tf-idf).")
st.write("  So what if we looked at each chapter as a single document... in a book, or in the trilogy? Calculate a tf-idf matrix for each of the three books, and calculate for the entire trilogy, and compare!")

book1_delta = '''document 1 in book 1 scores were ['gom', 'jabbar', 'paul', 'mother', 'said', 'jessica', 'hand', 'old', 'woman', 'box']
document 1 in trilogy scores were ['paul', 'said', 'mother', 'gom', 'jabbar', 'pain', 'old', 'jessica', 'box', 'woman']
document 1 has delta ['hand', 'pain']'''
st.code(book1_delta, language="python")

st.write("We can see that they mention 9 of the same top 10 words in the first book, but when we examine it as a single chapter out of the entire story (vs just the first book), the more significant word is 'pain' not 'hand'.")
st.divider()
st.write("Contextualizing the difference from the story-perspective; the first chapter is primarily about (spoiler!) young Paul's encounter with an old woman and a mysterious black box.")
st.write("When his hand is in the box, it inflicts great pain upon him. As an exercise in self-control he must keep his hand in the box, or immediately die.")
st.write("The whole trilogy is filled with pain - pain on a galactic scale! But it is written in more than one word... there is 'struggle' and 'torment' etc.")
st.write("Paul exercises self-control throughout the story, so the reader does not forget about the weird gom jabbar episode at the beginning.")
st.write("To the reader who has finished the entire story, the 'pain' of that moment is indeed more relevant than his 'hand'. 	:exploding_head: :astonished:")