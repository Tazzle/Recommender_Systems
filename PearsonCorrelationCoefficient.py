from math import sqrt

#page 14, Formula 2.1, Pearson's Correlation Coefficient

#data matrix
#TODO:
#Alice has to have an Item5 with no value
#User1 has to have an Item5 with value of 3
user_item_rating_matrix = {
    'Alice':{'Item1':5, 'Item2':3, 'Item3':4, 'Item4':4},
    'User1':{'Item1':3, 'Item2':1, 'Item3':2, 'Item4':3},
    'User2':{'Item1':4, 'Item2':3, 'Item3':4, 'Item4':3,'Item5':5},
    'User3':{'Item1':3, 'Item2':3, 'Item3':1, 'Item4':5,'Item5':4},
    'User4':{'Item1':1, 'Item2':5, 'Item3':5, 'Item4':2,'Item5':1}
}

#pseudocode to get the similarity sim(a,b) of users a and b 

#numerator:
#for each product in products
#   (rating of user a for the current product - avg. rating of user a) * (rating of user b for the current product - avg. rating of user b)

#denomenator:
#for each product in products
#   sqrt((rating of user a for the current product - avg. rating of user a)**2) * sqrt((rating of user b for the current product - avg. rating of user b)**2)

#result = numerator / denomenator
#example in the book has result of 0.85 when running a similarity between Alice and User1

#math functions
def avg(l):
    return sum(l, 0.0) / len(l)

def get_user_average(user):
    rating_average = []
    for key, value in user_item_rating_matrix[user].iteritems():
        if value is not None:
            rating_average.append(value)
    return avg(rating_average)


#similarity function
#parameter a, and parameter b should be usernames
#taken from the keys in user_item_rating_matrix above
def sim(a, b):
    avg_rating_user_a = get_user_average(a)
    avg_rating_user_b = get_user_average(b)

    #numerator
    numerator = 0
    #assuming that the keys in both dictionaries are the same
    #for each key, multiply the values from both dictionaries together
    #return a dictionary with the original keys as the keys, and the new multiplied values as values
    testdict = {k : (v  * avg_rating_user_a) * (user_item_rating_matrix[b][k] * avg_rating_user_b) for k, v in user_item_rating_matrix[a].items() if k in user_item_rating_matrix[b]}
    numerator = sum(testdict.values())
    print numerator

    #denomenator - TODO
    

sim('Alice', 'User1')











