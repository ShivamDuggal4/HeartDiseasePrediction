def selectImpAttributes(array):
    for i in range(len(array)):
        for j in [1,2,5,6,7,8,9,10,11,12]:
            array[i][j]=0
        

def equalWidth(array):
        for j in range(len(array[0])):

                minimum=100
                maximum=0
                if j in [0,3,4,7,9]:
                        for i in range(len(array)):
                                minimum=min(minimum,array[i][j])
                                maximum=max(maximum,array[i][j])
                        
                        intervalWidth=(maximum-minimum)/5

                        for i in range(len(array)):
                                if array[i][j]<=minimum+intervalWidth:
                                        array[i][j]=1
                                elif array[i][j]<=minimum+2*intervalWidth:
                                        array[i][j]=2
                                elif array[i][j]<=minimum+3*intervalWidth:
                                        array[i][j]=3
                                elif array[i][j]<=minimum+4*intervalWidth:
                                        array[i][j]=4
                                elif array[i][j]<=minimum+5*intervalWidth:
                                        array[i][j]=5
                                
                                


from cleaning_data import x,y,xx,yy
from sklearn.cluster import KMeans
from sklearn import tree


km=KMeans(n_clusters=5)
km.fit(x)


x0=list()
x1=list()
x2=list()
x3=list()
x4=list()

y0=list()
y1=list()
y2=list()
y3=list()
y4=list()


for i in range(len(x)):
    prediction=km.predict(x[i])
    prediction=int(prediction)
    if prediction==0:
        x0.append(x[i])
        y0.append(y[i])
    elif prediction == 1:
        x1.append(x[i])
        y1.append(y[i])
    elif prediction == 2:
        x2.append(x[i])
        y2.append(y[i])
    elif prediction == 3:
        x3.append(x[i])
        y3.append(y[i])
    elif prediction == 4:
        x4.append(x[i])
        y4.append(y[i])


#print len(x0),len(x1),len(x2),len(x3),len(x4)
        
#multinomial naive bayes starts

from sklearn.naive_bayes import MultinomialNB
clf0=tree.DecisionTreeClassifier(criterion="entropy",min_samples_leaf=10)
clf1=tree.DecisionTreeClassifier(criterion="entropy",min_samples_leaf=10)
clf2=tree.DecisionTreeClassifier(criterion="entropy",min_samples_leaf=10)
clf3=tree.DecisionTreeClassifier(criterion="entropy",min_samples_leaf=10)
clf4=tree.DecisionTreeClassifier(criterion="entropy",min_samples_leaf=10)

clf0.fit(x0,y0)
clf1.fit(x1,y1)
clf2.fit(x2,y2)
clf3.fit(x3,y3)
clf4.fit(x4,y4)

cnt=0

for i in range(len(xx)):
    prediction=km.predict(xx[i])
    prediction=int(prediction)
    if prediction==0:
        pred_naive=clf0.predict(xx[i])
    elif prediction==1:
        pred_naive=clf1.predict(xx[i])
    elif prediction==2:
        pred_naive=clf2.predict(xx[i])
    elif prediction==3:
        pred_naive=clf3.predict(xx[i])
    elif prediction==4:
        pred_naive=clf4.predict(xx[i])
    if pred_naive==yy[i]:
        cnt+=1


accuracy=cnt*100/len(xx)
print accuracy
#multinomial naive bayes ends


    
