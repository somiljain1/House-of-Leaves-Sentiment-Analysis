from sentiment import sentiment
import matplotlib.pyplot as plt
import numpy as np
list_=["1-68","69-136","137-204","205-272","273-340","341-408","409-476","477-end"]
list_2=['1143','2286','3429','4572','5715','6858','8001','9144']
direc="C:\\Users\Shwaita\\Downloads\\Navidson txt\\"#Navidson txt"+"\\"
plt.axis([0, 7, -1, 1])
plt.suptitle('House of Leaves Sentiment Analysis', fontsize=14, fontweight='bold')
plt.xlabel("House of Leaves Sections")
plt.ylabel("Sentiment")
a=0;
i=list(range(0,8))
values=[]
for x in list_2:
    filename=direc+"HoL_"+x+'.txt'
    print(filename)
    y=sentiment(filename)
    values.append(y)
    plt.scatter(a, y)
    #plt.plot(i, y,linewidth=2)
    a=a+1
plt.plot(i,[0]*8,'--')
plt.plot(i, values,'k')
plt.show()