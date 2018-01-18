from cleaning_data import x,y,xx,yy


from sklearn import tree
clf=tree.DecisionTreeClassifier(criterion="entropy",min_samples_leaf=10)   #criterion="entropy", max_depth=16,min_samples_leaf=10,min_samples_split=10       
clf=clf.fit(x,y)                             # applying decision tree on training set

ans=list()

for i in range(len(xx)):                      # applying tree on test set and storing results labels in ans 
	ans.append(clf.predict([xx[i]]))

for i in range(len(ans)):
	ans[i]=ans[i].tolist()                # converting ans from numpy format to list format ( 2D list)

for i in range(len(ans)):                     # converting each element of ans from list to int type
	t=ans[i]
	t=int(t[0])
	ans[i]=t

cnt=0

for i in range(len(ans)):                    # cnt represents how many labels in ans dont match with corresponding labels in yy
	if ans[i]!=yy[i]:
		cnt+=1
		

acc=len(ans)-cnt                              # calculating accuracy
acc=acc*100
acc=(float)(acc)/(float)(len(ans))

print acc


