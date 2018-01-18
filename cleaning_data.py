def equalWidth(x):
        for j in range(len(x[0])):

                minimum=100
                maximum=0
                if j in [0,3,4,7,9]:
                        for i in range(len(x)):
                                minimum=min(minimum,x[i][j])
                                maximum=max(maximum,x[i][j])
                        
                        intervalWidth=(maximum-minimum)/5

                        for i in range(len(x)):
                                if x[i][j]<=minimum+intervalWidth:
                                        x[i][j]=1
                                elif x[i][j]<=minimum+2*intervalWidth:
                                        x[i][j]=2
                                elif x[i][j]<=minimum+3*intervalWidth:
                                        x[i][j]=3
                                elif x[i][j]<=minimum+4*intervalWidth:
                                        x[i][j]=4
                                elif x[i][j]<=minimum+5*intervalWidth:
                                        x[i][j]=5
                                
                                


f=open('D:\shamit\coding\python and ml projects\heart disease prediction\\x.csv')

x=[line.split(',') for line in f]      # reading data(values of attributes) in x to create 2D list

for i in range(len(x)):                #  stripping \n from the last attribute of each row
	x[i][12]=x[i][12].rstrip()

for i in range(len(x)):                # converting value of each attribute from string to float type
	for j in range(len(x[i])):
		x[i][j]=float(x[i][j])

f=open('D:\shamit\coding\python and ml projects\heart disease prediction\y.csv')  # perfoming same steps with ans labels

y=[line.split(',') for line in f]

for i  in range(len(y)):
	y[i]=y[i][0].rstrip()

for i in range(len(y)):
	y[i]=int(y[i])

for i in range(len(y)):
        if y[i]>0:
                y[i]=1



equalWidth(x)     #descritizing continuous data



        
xx=list()
yy=list()

for i in range(len(x)-1,200,-1):           # creating test sets and training sets
	xx.append(x[i])
	yy.append(y[i])
	del(x[i])
	del(y[i])


