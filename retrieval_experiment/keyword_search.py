def keyword_score(query, document):
    list_query = []
    list_document = []
    query_list = query.lower().split()
    document_list = document.lower().split()
    for word in query_list:
        if (word in list_query) == False:
            list_query.append(word)
    for word in document_list:
        if (word in list_document) == False:
            list_document.append(word)
    tally = 0
    for word in list_query:
        if (word in list_document) == True:
            tally = tally + 1
    return tally

print(keyword_score("logs logs error", "error logs logs logs"))
print(keyword_score("container stopped", "the service exited"))
print(keyword_score(""," error logs"))
print(keyword_score("logs error",""))
print(keyword_score("error,","error"))
print(keyword_score("error", "error,"))
print(keyword_score("",""))
print(keyword_score("LOGS lOgs logS", "ErrOR Logs LOGS"))