# UMass Fall 2022 Info90S - Project 4 Document Retrieval

Overview

We use search engines every day. Indeed, you are likely to use Google as you do this assignment to search for specifics related to Python (most certainly not to find the solution). But, how do these search engines identify documents on the web that are relevant to the words that you enter into the text box? How is it possible for Google to respond so quickly to your search words? This project asks you to implement a document retrieval program that allows a user to quickly search for words in a large set of documents.

Your program will read in a large set of documents, identify in which documents each word exists, and allow you to search for words efficiently in the same way that Google does this for the web. There are many ways in which this could be done. The approach we are going to use is to read in a collection of documents, assign each document a unique identifier, identify each word in the document, and then associate each word with the document identifier in which it was found.

The program requires three arguments. The first argument is the the URL of the article file to index. The second argument is the command. In this case, it is find, which tells the program to search for the word in the set of documents we read in. The last argument is the words you would like search for in the documents. The output is the documents in which the words "dogs cats" both appeared.
