from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def review_to_lists(movie_csv):
# Reading the CSV file
    data = pd.read_csv(movie_csv)

    # Converting specific columns into lists
    reviews = data['review_content'].tolist()

    # Printing the lists
    return reviews

def similarity(review_id, reviews):
    count_vectorizer = CountVectorizer(stop_words='english')
    sparse_matrix = count_vectorizer.fit_transform(reviews)
    doc_term_matrix = sparse_matrix.todense()
    df = pd.DataFrame(
        doc_term_matrix,
        columns=count_vectorizer.get_feature_names_out()
    )
    matrix = cosine_similarity(df, df)
    similar_review = ""
    similar_value = 0
    l = len(reviews)
    for i  in range(0, l):
        value = matrix[review_id, i]
        if similar_value < value < 1:
            similar_review = reviews[i]
            similar_value = matrix[review_id][i]

    return similar_review





