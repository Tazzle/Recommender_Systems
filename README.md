#####Translation of formulae from 'Recommender Systems: An Introduction' into Python.

**Reference**: (Felfernig, A. et al., _Recommender Systems: An Introduction_, New York, Cambridge University Press, 2011)

---



#####PearsonCorrelationCoefficient.py:   
Page 14, Equation 2.1, Pearson's Correlation Coefficient. Identify if one user has similar tastes to another.

**Corregendum:** 
"_When computing the similarity of two users in Equation 2.1, 
only the co-rated items should be used to determine the averages (and the similarity) of the respective users._"  
Source: [http://www.recommenderbook.net/media/corrigenda.pdf]  

---


#####Prediction_PearsonCorrelationCoefficient.py:  
Page 16, Equation 2.3, Predict a user's rating for an item based on the ratings of the user's nearest neighbours for that item.

---

#####CosineSimilarity.py:  
Page 19, Equation 2.5, The Cosine Similarity Measure. Identify if one item is similar to another.


---

#####AdjustedCosineSimilarity.py:  
Page 19, Equation 2.7, The Adjusted Cosine Similarity Measure. Takes the differences in average rating behaviour of the users into account, unlike the basic cosine similarity measure.


---

#####Prediction_AdjustedCosineSimilarity.py:
Page 20, Equation 2.9, Predict a user's rating for an item based on the user's ratings for items that are similar to that item.

---

#####SingularValueDecomposition.py:
Page 28, Equation 2.10,  Transpose user_item_rating_matrix (with 'Alice' row removed). Perform SVD on resulting matrix.



