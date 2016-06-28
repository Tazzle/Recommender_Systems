from __future__ import division
from PearsonCorrelationCoefficient import sim, avg

user_item_rating_matrix = {
    'Alice':{'Item1':5, 'Item2':3, 'Item3':4, 'Item4':4},
    'User1':{'Item1':3, 'Item2':1, 'Item3':2, 'Item4':3, 'Item5':3},
    'User2':{'Item1':4, 'Item2':3, 'Item3':4, 'Item4':3,'Item5':5},
    'User3':{'Item1':3, 'Item2':3, 'Item3':1, 'Item4':5,'Item5':4},
    'User4':{'Item1':1, 'Item2':5, 'Item3':5, 'Item4':2,'Item5':1}
}

def pred(user_a, user_b, user_c, item_to_predict):

    avg_rating_a = avg([v for k,v in user_item_rating_matrix[user_a].iteritems()])
    avg_rating_b = avg([v for k,v in user_item_rating_matrix[user_b].iteritems()])
    avg_rating_c = avg([v for k,v in user_item_rating_matrix[user_c].iteritems()])

    #getting 0.71 for sim(a,c). This should be 0.70 according to the book. 
    #other values are as expected
    similarity_a_b = float(sim(user_a, user_b))
    similarity_a_c = float(sim(user_a, user_c))

    numerator_a_b = (similarity_a_b) * (user_item_rating_matrix[user_b][item_to_predict] - avg_rating_b)
    numerator_a_c = (similarity_a_c) * (user_item_rating_matrix[user_c][item_to_predict] - avg_rating_c)

    numerator =  numerator_a_b + numerator_a_c
    denominator = similarity_a_b + similarity_a_c

    item_rating_prediction = avg_rating_a + (numerator / denominator) 

    #result - returns 4.87
    print "{0:.2f}".format(item_rating_prediction)


#predict a rating for Alice for Item5 based on the ratings of her two nearest neighbours (User1, and User2) for Item5
#the nearest neighbours were identified using the Pearson Correlation Coefficient formula in PearsonCorrelationCoefficient.py
pred('Alice', 'User1', 'User2', 'Item5')

