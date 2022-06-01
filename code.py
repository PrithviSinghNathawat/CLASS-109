from unittest import result
import plotly.figure_factory as pff
import plotly.express as pe
import random
import statistics
import plotly.graph_objects as pgo
diceResult=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceResult.append(dice1+dice2)
mean=sum(diceResult)/len(diceResult)
print(mean)
median=statistics.median(diceResult)
print(median)
mode=statistics.mode(diceResult)
print(mode)
sd=statistics.stdev(diceResult)
print(sd)
firstSdStart,firstSdEnd=mean-sd,mean+sd
secondSdStart,secondSdEnd=mean-(2*sd),mean+(2*sd)
thirdSdStart,thirdSdEnd=mean-(3*sd),mean+(3*sd)
figure=pff.create_distplot([diceResult],['Result'],show_hist=False)
figure.add_trace(pgo.Scatter(x=[mean,mean],y=[0,0.17],mode='lines'))
figure.add_trace(pgo.Scatter(x=[firstSdStart,firstSdStart],y=[0,0.17]))
figure.add_trace(pgo.Scatter(x=[firstSdEnd,firstSdEnd],y=[0,0.17]))
figure.add_trace(pgo.Scatter(x=[secondSdStart,secondSdStart],y=[0,0.17]))
figure.add_trace(pgo.Scatter(x=[secondSdEnd,secondSdEnd],y=[0,0.17]))
figure.add_trace(pgo.Scatter(x=[thirdSdStart,thirdSdStart],y=[0,0.17]))
figure.add_trace(pgo.Scatter(x=[thirdSdEnd,thirdSdEnd],y=[0,0.17]))
figure.show()
listOfDataWithinFirstSd=[result for result in diceResult if result>firstSdStart and result<firstSdEnd]
listOfDataWithinSecondSd=[result for result in diceResult if result>secondSdStart and result<secondSdEnd]
listOfDataWithinThirdSd=[result for result in diceResult if result>thirdSdStart and result<thirdSdEnd] 

print('{}% of data lies within First Standard Deviation'.format(len(listOfDataWithinFirstSd)*100/len(diceResult)))
print('{}% of data lies within Second Standard Deviation'.format(len(listOfDataWithinSecondSd)*100/len(diceResult)))
print('{}% of data lies within Third Standard Deviation'.format(len(listOfDataWithinThirdSd)*100/len(diceResult)))
