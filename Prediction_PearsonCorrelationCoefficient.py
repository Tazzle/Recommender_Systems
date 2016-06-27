from __future__ import division
from PearsonCorrelationCoefficient import sim, avg

user_item_rating_matrix = {
    'Alice':{'Item1':5, 'Item2':3, 'Item3':4, 'Item4':4},
    'User1':{'Item1':3, 'Item2':1, 'Item3':2, 'Item4':3, 'Item5':3},
    'User2':{'Item1':4, 'Item2':3, 'Item3':4, 'Item4':3,'Item5':5},
    'User3':{'Item1':3, 'Item2':3, 'Item3':1, 'Item4':5,'Item5':4},
    'User4':{'Item1':1, 'Item2':5, 'Item3':5, 'Item4':2,'Item5':1}
}

#predict a rating for Item5 for Alice based on her 2 Nearest Neighbours (User1, and User2)
def pred(user_a,user_b, user_c):

    avg_rating_a = avg([v for k,v in user_item_rating_matrix[user_a].iteritems()])
    avg_rating_b = avg([v for k,v in user_item_rating_matrix[user_b].iteritems()])
    avg_rating_c = avg([v for k,v in user_item_rating_matrix[user_c].iteritems()])

    matrix_minus_alice = {k : v for k,v in user_item_rating_matrix.iteritems() if k is not user_a}

    similarity_a_b = float(sim(user_a, user_b))
    similarity_a_c= float(sim(user_a, user_c))

    #bug - getting 0.71 instead of 0.70 for sim(a,c)

    numerator_a_b = sum([(similarity_a_b * (v - avg_rating_b)) for k,v in matrix_minus_alice[user_b].iteritems()])
    numerator_a_c = sum([(similarity_a_c * (v - avg_rating_c)) for k,v in matrix_minus_alice[user_c].iteritems()])

    denominator_a_b = sum([similarity_a_b for x in matrix_minus_alice])
    denominator_a_c = sum([similarity_a_c for x in matrix_minus_alice])

    item_rating_prediction = avg_rating_a + ((numerator_a_b + numerator_a_c)/(denominator_a_b+denominator_a_c))

    print item_rating_prediction


pred('Alice', 'User1', 'User2')

