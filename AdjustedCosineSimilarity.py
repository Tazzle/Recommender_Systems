from PearsonCorrelationCoefficient import avg
from math import sqrt

user_item_rating_matrix = {
    'Alice':{'Item1':5, 'Item2':3, 'Item3':4, 'Item4':4},
    'User1':{'Item1':3, 'Item2':1, 'Item3':2, 'Item4':3,'Item5':3},
    'User2':{'Item1':4, 'Item2':3, 'Item3':4, 'Item4':3,'Item5':5},
    'User3':{'Item1':3, 'Item2':3, 'Item3':1, 'Item4':5,'Item5':4},
    'User4':{'Item1':1, 'Item2':5, 'Item3':5, 'Item4':2,'Item5':1}
}

def user_avg_rating(user):

    return avg(user_item_rating_matrix[user].values())


def adj_cosine_sim(item_a, item_b):

    #3.68
    numerator = sum([(rating[item_a] - user_avg_rating(user)) * (rating[item_b] - user_avg_rating(user)) for user, rating in user_item_rating_matrix.iteritems() if item_a and item_b in rating.keys()])
    
    #euclidian length of each vector
    euc_len_item_a = sqrt(sum([round((rating[item_a] - user_avg_rating(user))**2,2) for user, rating in user_item_rating_matrix.iteritems() if item_a and item_b in rating.keys()]))
    euc_len_item_b = sqrt(sum([round((rating[item_b] - user_avg_rating(user))**2,2) for user, rating in user_item_rating_matrix.iteritems() if item_a and item_b in rating.keys()]))

    #4.57
    denominator = euc_len_item_a * euc_len_item_b
    
    #0.80
    print "{0:.2f}".format(numerator/denominator)


adj_cosine_sim('Item1', 'Item5')