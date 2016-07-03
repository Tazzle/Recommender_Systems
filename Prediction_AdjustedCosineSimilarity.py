from AdjustedCosineSimilarity import adj_cosine_sim


user_item_rating_matrix = {
    'Alice':{'Item1':5, 'Item2':3, 'Item3':4, 'Item4':4},
    'User1':{'Item1':3, 'Item2':1, 'Item3':2, 'Item4':3,'Item5':3},
    'User2':{'Item1':4, 'Item2':3, 'Item3':4, 'Item4':3,'Item5':5},
    'User3':{'Item1':3, 'Item2':3, 'Item3':1, 'Item4':5,'Item5':4},
    'User4':{'Item1':1, 'Item2':5, 'Item3':5, 'Item4':2,'Item5':1}
}


def pred(user, product):

    numerator = sum([round(adj_cosine_sim(item, product) * rating, 2) for item, rating in user_item_rating_matrix[user].iteritems()])

    denominator = sum([round(adj_cosine_sim(item, product),2) for item, rating in user_item_rating_matrix[user].iteritems()])

    #0.05 - expected result unspecified
    print "{0:.2f}".format(numerator/denominator)

pred('Alice', 'Item5')