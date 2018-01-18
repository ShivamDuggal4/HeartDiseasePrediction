
from cleaning_data import x,y,xx,yy






#multinomial naive bayes starts

from sklearn.naive_bayes import MultinomialNB
clf=MultinomialNB()
clf.fit(x,y)
t=clf.score(xx,yy)
print t*100

#multinomial naive bayes ends





















'''
#gaussian naive bayes starts

from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()
gnb.fit(x,y)

t=gnb.score(xx,yy)
print t*100

#gaussian naive bayes ends
'''
