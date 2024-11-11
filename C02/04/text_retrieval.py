import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def cosine_search(question, tfidf_vectorizer, top_d=5):
    query_embedded = tfidf_vectorizer.transform([question.lower()]).toarray()
    cosine_scores = cosine_similarity(
        context_embedded, query_embedded).reshape((-1,))

    results = []
    for idx in cosine_scores.argsort()[-top_d:][:: -1]:
        doc_score = {'id': idx,
                     'cosine_score': cosine_scores[idx]}
        results.append(doc_score)

    return results


def corr_search(question, tfidf_vectorizer, top_d=5):
    query_embedded = tfidf_vectorizer.transform([question.lower()]).toarray()
    corr_scores = np.corrcoef(query_embedded[0], context_embedded)[0][1:]

    results = []
    for idx in corr_scores.argsort()[-top_d:][:: -1]:
        doc_score = {'id': idx,
                     'corr_score': corr_scores[idx]}
        results.append(doc_score)

    return results


if __name__ == "__main__":
    data = pd.read_csv("Module_02_Exercise_M02EX04/vi_text_retrieval.csv")
    tfidf_vectorizer = TfidfVectorizer()

    context_embedded = tfidf_vectorizer.fit_transform(
        list(data['text'].str.lower())).toarray()
    question = data.iloc[0]['question']

    cosine_res = cosine_search(question, tfidf_vectorizer, top_d=1)
    for res in cosine_res:
        print("Id: ", res['id'])
        print("Cosine score: ", res['cosine_score'])
        print(data.iloc[res['id'], 2])
        print("============================================\n")

    print("****************************************************")

    corr_res = corr_search(question, tfidf_vectorizer, top_d=1)
    for res in corr_res:
        print("Id: ", res['id'])
        print("Correl score: ", res['corr_score'])
        print(data.iloc[res['id'], 2])
        print("============================================\n")
