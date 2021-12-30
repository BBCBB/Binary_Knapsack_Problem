randef=input('wou1ld you like to generate a random problem or a predefined one is ok? 1 or other: ')
if randef=='1':
    n=int(input('Please enter the number of items you would like to fit in the knapsack: '))+1
    import random
# Problem Generator Function
    def Problem_Generator(n):
        w=[]                                   #weight of items
        v=[]                                   #value of each item
        for i in range(1,n):
            w.append(random.randint(2,10))
            v.append(random.randint(25,45))
            sum_items=sum(w)                   # sum of the items' weight
            C=int(0.85*sum_items)              # option 1 to generate C
        #     C=float('inf')                   # option 2 to generate C
        # while sum_items<C:    
        #     C=random.randint(18,35)                             

        return [C,w,v]
    Problem=Problem_Generator(n)
    C=Problem[0]
    w=Problem[1]
    v=Problem[2]
    n=n-1

else:
    C= 99 
    w= [12, 8, 5, 10, 4, 10, 8, 3, 10, 2, 7, 10, 10, 5, 6, 3, 6, 8, 5, 4] 
    v= [37, 26, 26, 42, 44, 38, 41, 34, 29, 40, 29, 27, 39, 43, 31, 38, 30, 34, 37, 41]
    n=20

select=[0]*n

def DP(C, w, v, n): 
    DPT = [[0 for r in range(C+1)] for r in range(n)] 
    for i in range(n): 
        for j in range(C+1): 
            if w[i] <= j: 
                DPT[i][j] = max(v[i] + DPT[i-1][j-w[i]],DPT[i-1][j]) 
            else: 
                DPT[i][j] = DPT[i-1][j] 
             
    pos = C
    for t in range(n-1, -1, -1):
        if t==0 and DPT[0][pos]>0:
            select[t]=1
        elif DPT[t][pos] > DPT[t-1][pos]:
            select[t]= 1
            pos=pos-w[t]
    return [DPT[n-1][C],select]
Objective=DP(C, w, v, n)[0]
decision_vector=DP(C, w, v, n)[1]
print('\n The decision vector of the problem:\n {}'.format(decision_vector))
print('\n Objective Function Value is " {} " '.format(Objective))

