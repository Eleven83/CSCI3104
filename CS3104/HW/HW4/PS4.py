import random, sys, urllib.request, numpy, webbrowser
import matplotlib.pyplot as plt
import pandas as pd


def readParseHash():
    #store and open the url to collect the name data
    url = 'http://www2.census.gov/topics/genealogy/1990surnames/dist.all.last'
    nameInput = urllib.request.urlopen(url)

    #Uniformly random 50% of the names will be used 
    nameData = [line for line in nameInput if random.random() >= .5]

    #Parsing the lines to get just the last names
    lastNames = [i.split(b" ", 1)[0] for i in nameData]

    #Create an array to hold the size of each name
    nameLength = [len(i) for i in lastNames]
    size = len(lastNames)
    buckets = []
    
    #Iterate through the list of names counting each frequency
    for i in range (0, size):
        count = 0
        #ASCII values need to be shifted by 64 bits 
        count = nameLength[i] * 64
        nameSum = numpy.frombuffer(lastNames[i], "uint8").sum()
        lastNames[i] = nameSum - count

        x = lastNames[i] % 200
        buckets.append(x)
    #Send the output to a new file
    with open('namesOutput.txt','w') as names:
        for frequency in buckets:
            print(frequency, file=names)

def drawPlot():
    pltInfo = pd.read_csv('namesOutput.txt')
    
    pltInfo.hist(bins=200, color='g')
    #plt.xlim([0,200])
    
    plt.xlabel("Bucket Value")
    plt.ylabel("Number of Names")
    
    # giving a title to my graph
    plt.title("Hash Histogram")
    
    plt.show()
    
    plt.savefig("PS4Histogram.png")

readParseHash()
drawPlot()