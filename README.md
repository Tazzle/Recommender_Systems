#####Translation of formulae from 'Recommender Systems: An Introduction' into Python.

**Reference**: (Felfernig, A. et al., _Recommender Systems: An Introduction_, New York, Cambridge University Press, 2011)

---



#####PearsonCorrelationCoefficient.py:   
Page 14, Formula 2.1, Pearson's Correlation Coefficient. Identify if one user has similar tastes to another.

**Corregendum:** 
"_When computing the similarity of two users in Equation 2.1, 
only the co-rated items should be used to determine the averages (and the similarity) of the respective users._"  
Source: [http://www.recommenderbook.net/media/corrigenda.pdf]  

---



#####Prediction_PearsonCorrelationCoefficient.py:  
Page 16, Formula 2.3, Predicting a user's rating for an item based on the ratings of the user's nearest neighbours for that item.