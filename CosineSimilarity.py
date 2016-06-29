from math import sqrt

user_item_rating_matrix = {
    'Alice':{'Item1':5, 'Item2':3, 'Item3':4, 'Item4':4},
    'User1':{'Item1':3, 'Item2':1, 'Item3':2, 'Item4':3,'Item5':3},
    'User2':{'Item1':4, 'Item2':3, 'Item3':4, 'Item4':3,'Item5':5},
    'User3':{'Item1':3, 'Item2':3, 'Item3':1, 'Item4':5,'Item5':4},
    'User4':{'Item1':1, 'Item2':5, 'Item3':5, 'Item4':2,'Item5':1}
}

#calculate the cosine similarity of item_a, and item_b
def cosine_sim(item_a, item_b):

    dot_product = [(dict[item_a] * dict[item_b]) for row, dict in user_item_rating_matrix.iteritems() if item_a and item_b in dict.keys()]

    numerator = sum(dot_product)

    #euclidian length of the vector
    item_a_euc_len = sqrt(sum([dict[item_a]**2 for row, dict in user_item_rating_matrix.iteritems() if item_a and item_b in dict.keys()]))
    item_b_euc_len = sqrt(sum([dict[item_b]**2 for row, dict in user_item_rating_matrix.iteritems() if item_a and item_b in dict.keys()]))

    cosine_similarity = numerator / (item_a_euc_len * item_b_euc_len)
    
    #result - 0.99
    print round(cosine_similarity,2)


cosine_sim('Item1', 'Item5')