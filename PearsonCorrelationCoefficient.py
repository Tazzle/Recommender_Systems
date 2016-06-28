from math import sqrt

#page 14, Formula 2.1, Pearson's Correlation Coefficient

#data matrix
#TODO:
#In the book Alice has a column for Item5 with no rating, need to add the empty Item5 to the matrix without throwing off result.
user_item_rating_matrix = {
    'Alice':{'Item1':5, 'Item2':3, 'Item3':4, 'Item4':4},
    'User1':{'Item1':3, 'Item2':1, 'Item3':2, 'Item4':3, 'Item5':3},
    'User2':{'Item1':4, 'Item2':3, 'Item3':4, 'Item4':3,'Item5':5},
    'User3':{'Item1':3, 'Item2':3, 'Item3':1, 'Item4':5,'Item5':4},
    'User4':{'Item1':1, 'Item2':5, 'Item3':5, 'Item4':2,'Item5':1}
}

def avg(l):
    return sum(l, 0.0) / len(l)


def get_user_average(user_a, user_b):
#corregendum in book - chapter 2, section 2.1.1, page 15. "When computing the
#similarity of two users in Equation 2.1, only the co-rated items should be used to
#determine the averages (and the similarity) of the respective users"
#source - http://www.recommenderbook.net/media/corrigenda.pdf
#thus, not getting the average of all ratings per user here

    avg_a  = avg([v for k,v in user_item_rating_matrix[user_a].iteritems() if k in user_item_rating_matrix[user_b]])
    avg_b = avg([v for k,v in user_item_rating_matrix[user_b].iteritems() if k in user_item_rating_matrix[user_a]])

    return(avg_a, avg_b)


#parameter a, and parameter b should be usernames
#taken from the keys in user_item_rating_matrix above
def sim(user_a, user_b):

    #get users' average ratings
    avg_rating_user_a, avg_rating_user_b = get_user_average(user_a, user_b)

    #numerator
    #assuming that the keys in both dictionaries are the same
    #for each key, multiply the values from both dictionaries together
    #return a dictionary with the original keys as the keys, and the new multiplied values as values
    multiplied_values = {k : (v - avg_rating_user_a) * (user_item_rating_matrix[user_b][k] - avg_rating_user_b) for k, v in user_item_rating_matrix[user_a].items() if k in user_item_rating_matrix[user_b]}
    numerator = sum(multiplied_values.values())

    #denominator
    val_minus_avg_squared_user_a = {k : ((v - avg_rating_user_a) **2) for k, v in user_item_rating_matrix[user_a].items() if k in user_item_rating_matrix[user_b]}
    val_minus_avg_squared_user_b = {k : ((v - avg_rating_user_b) **2) for k, v in user_item_rating_matrix[user_b].items() if k in user_item_rating_matrix[user_a]}

    #needs clearer variable names
    result_user_a = sum(val_minus_avg_squared_user_a.values())
    result_user_b = sum(val_minus_avg_squared_user_b.values())
       
    denominator = sqrt(result_user_a)*sqrt(result_user_b)

    #result - returns 0.85
    return ("{0:.2f}".format(numerator / denominator))


#find the similarity between the interests of Alice, and User1, based on the items they have both rated
sim('Alice', 'User4')

#sim('Alice', 'User1'): 0.85
#sim('Alice', 'User2'): 0.71 (bug - should be 0.70)
#sim('Alice', 'User3'): 0.00
#sim('Alice', 'User4'): -0.79

#Pearson's Correlation Coefficient returns a number between -1 and 1
#the closer the result is to 1, the higher the similarity between the two users
#conversely, the closer the result is to -1, the lower the similarity between two users
#in this case, Alice's two Nearest Neighbours are User1, and User2
#Alice's tastes are dissimilar to User1, and User4













