#-------------------------------------------------------------------------
# AUTHOR: Justin Ha
# FILENAME: db_connection_mongo.py
# SPECIFICATION: middleman helper to provide functions that will directly
# interface with mongoDB
# FOR: CS 4250- Assignment #2
# TIME SPENT: 4pm 10/3/2024
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with
# standard arrays

#importing some Python libraries
from pymongo import MongoClient
import datetime
import string

def connectDataBase():

    # Create a database connection object using pymongo
    DB_NAME = "assignment_2"
    DB_HOST = "localhost"
    DB_PORT = 27017
    try:
        client = MongoClient(host=DB_HOST, port=DB_PORT)
        db = client[DB_NAME]
        return db
    except:
        print("Database not connected successfully")

def createDocument(col, docId, docText, docTitle, docDate, docCat):

    # create a dictionary (document) to count how many times each term appears in the document.
    # Use space " " as the delimiter character for terms and remember to lowercase them.
    text_no_punc = docText.translate(str.maketrans('', '', string.punctuation))
    terms = text_no_punc.split()
    term_count = {}
    for term in terms:
        term = term.lower()
        term_count[term] = term_count.get(term, 0) + 1

    # create a list of dictionaries (documents) with each entry including a term, its occurrences, and its num_chars. Ex: [{term, count, num_char}]
    term_docs = []
    for term in term_count:
        num_char = len(term)
        doc = { "term": term, "count": term_count[term], "num_char": num_char }
        term_docs.append(doc)

    #Producing a final document as a dictionary including all the required fields
    final_doc = {
        "_id": docId,
        "text": docText,
        "title": docTitle,
        "date": datetime.datetime.strptime(docDate, "%Y-%m-%d"),
        "category": docCat,
        "terms": term_docs
    }

    # Insert the document
    col.insert_one(final_doc)

def deleteDocument(col, docId):

    # Delete the document from the database
    col.delete_one({ "_id": docId })

def updateDocument(col, docId, docText, docTitle, docDate, docCat):

    # Delete the document
    col.delete_one({ "_id": docId })

    # Create the document with the same id
    createDocument(col, docId, docText, docTitle, docDate, docCat)

def getIndex(col):

    # Query the database to return the documents where each term occurs with their corresponding count. Output example:
    # {'baseball':'Exercise:1','summer':'Exercise:1,California:1,Arizona:1','months':'Exercise:1,Discovery:3', ...}
    # We are simulating an inverted index here in memory.
    
    pipeline = [
        {
            "$unwind": "$terms" # output a document for every term in each document
        },
        {
            "$group": {
                "_id": {
                    "term": "$terms.term",     #group by a unique combination of term + title
                    "title": "$title"
                },
                "count": {"$sum": "$terms.count"}   #even though there there are no duplicate terms in documents, $group requires fields to be accumulators. In this case, I used $sum
            }
        },
        {
            "$group": {
                "_id": "$_id.term",     #group by term
                "documents": {
                    "$push": {          #push each title:count pair into this list. note: multiple title:count pairs can be pushed here based on term grouping
                        "title": "$_id.title",
                        "count": "$count"
                    }
                }
            }
        },
        {
            "$project": {
                "_id": 0,
                "term": "$_id",
                "documents": 1
            }
        }
    ]
    unformatted_result = col.aggregate(pipeline)
    result = {}
    for doc in unformatted_result:
        doc_count = []
        for entry in doc['documents']:
            doc_count.append(f"{entry['title']}:{entry['count']}")
        result[doc['term']] = (doc_count)
    
    return result