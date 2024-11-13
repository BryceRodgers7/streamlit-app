import streamlit as st
from menu import menu_with_redirect
from PIL import Image
import base64
from random import randrange

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()


st.title("Data Collection and Processing")
st.subheader("Processing, Sanitizing, Tokenizing")

colab = "https://colab.research.google.com/drive/10XLZlovVfBLhaw60EJtBp2BPvRK2Edsf?usp=sharing"
st.write("Complete jupyter notebook found [here](%s)" % colab)
movie_script = "https://d2bu9v0mnky9ur.cloudfront.net/academy2021/scripts/duneMxFtT98NYwBsMltl20211109/dune_final_shooting_script_6_19_20.pdf"
st.write("#1: Obtain the raw data: [here](%s) (the final shooting script for Dune 2020)." % movie_script)
st.write("Notice there are random numbers and alphanumeric codes on every page, plus plenty of formatting, deleted scenes, and movie-instructions")
st.image(".static/dune_one_page.png", caption="One page of the Dune script")
st.write("When we extract the raw text from it, the random noise looks even worse.")
st.write("If we want to make another TF-IDF matrix, we'll have to clean up this data until it's nothing but words.")

st.write("#2 Divide the corpus into documents - since this is a movie script, divvy by scene code should be made an option.")
st.write("This requires manually examining/processing the data in order to identify all of the scene codes.")

st.write("#3: Sanitize the corpus")
st.write("  lower-case, remove punctuation, remove stop words, remove non-alphanumeric, stem, lemmatize")
st.write("This corpus has some text that should be removed outright. We begin step #3 in production by removing/replacing it, however in practice we may want to perform some sanitizing steps earlier, even before divvy.")
st.write("This makes manual examination of the text in practice much easier.")
st.write("We just have to be careful not to clean up the page numbers or scene codes until after we had a chance to use them to perform the divvy.")
fix_cases_code = '''# remove revision-notes from dataset
pattern = r'Salmon Rev\. \(\d{2}\/\d{2}\/\d{4}\)'
preprocessed_text = re.sub(pattern, "", preprocessed_text)
pattern = r'Salmon Rev\. \(\d{2}\/\d{2}\/\d{2}\)'
preprocessed_text = re.sub(pattern, "", preprocessed_text)

pattern = r'Buff Rev\. \(\d{2}\/\d{2}\/\d{4}\)'
preprocessed_text = re.sub(pattern, "", preprocessed_text)
pattern = r'Buff Rev\. \(\d{2}\/\d{2}\/\d{2}\)'
preprocessed_text = re.sub(pattern, "", preprocessed_text)

pattern = r'Golden Rev\. \(\d{2}\/\d{2}\/\d{4}\)'
preprocessed_text = re.sub(pattern, "", preprocessed_text)
pattern = r'Golden Rev\. \(\d{2}\/\d{2}\/\d{2}\)'
preprocessed_text = re.sub(pattern, "", preprocessed_text)

# remove the following from the dataset:
preprocessed_text = preprocessed_text.replace("FADE TO BLACK", "")
preprocessed_text = preprocessed_text.replace("THE END", "")
preprocessed_text = preprocessed_text.replace("(MORE)", "")

# fix following typos in the dataset
preprocessed_text = preprocessed_text.replace("terrain.We", "terrain. We")'''
st.code(fix_cases_code, language="python")

st.write("#4: Create TDF matrix  SAME AS PREVIOUS PAGE")
tdf_matrix_code = '''vocabulary = sorted(set(word for doc in preprocessed_corpus for word in doc.split()))

# start with empty matrix
tdf_matrix = np.zeros((len(preprocessed_corpus), len(vocabulary)), dtype=int)

# scan corpus, fill matrix
for doc_idx, doc in enumerate(preprocessed_corpus):
    for term in doc.split():
        term_idx = vocabulary.index(term)
        tdf_matrix[doc_idx, term_idx] += 1'''
st.code(tdf_matrix_code, language="python")

st.write("#5: Create TF-IDF matrix SAME AS PREVIOUS PAGE")
tfidf_matrix_code = '''# Compute Term Frequency matrix
tf_matrix = tdf_matrix / np.sum(tdf_matrix, axis=1, keepdims=True)

# Compute Inverse Document Frequency matrix
num_documents = tdf_matrix.shape[0]
idf_vector = np.log(num_documents / np.count_nonzero(tdf_matrix, axis=0))

# Compute TF-IDF matrix
tfidf_matrix = tf_matrix * idf_vector'''
st.code(tfidf_matrix_code, language="python")