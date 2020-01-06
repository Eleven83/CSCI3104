def makeWizardMoney(A):
    M=[]
    maxProfitSoFar = 0
    minVal = A[0]
    for i in range(len(A)-1):
        if A[i] > minVal:
            M.append(minVal)
        else:
            M.append(A[i])
            minVal=A[i]
    for j in range(len(A)-1):
        if A[j] > M[j]:
            maxProfitSoFar=A[j]-M[j]       
    #return (M)
    return maxProfitSoFar

A=[8,9,3,4,14,12,15,19,7,8,12,11]
print (makeWizardMoney(A))