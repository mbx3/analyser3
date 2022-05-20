import matplotlib.pyplot as plt


def draw(data,balance):
    y=[i[0] for i in data]
    x=range(1,len(y)+1)
    cols=['r','g']
    c=[cols[i[1]] for i in data]

    fig,(ax1,ax2)=plt.subplots(2,1)
    
    ax1.scatter(x,y,c=c,marker='.')
    ax2.plot(balance)
    plt.show()

