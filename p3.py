import csv 

with open("enjoy_sport_data.csv","r") as csvFile:
    examples =[tuple(line) for line in csv.reader(csvFile)]
    
def more_general(hyp,exg):
    more_general_parts=[]
    for x,y in zip(hyp,exg):
        
        mg= x=="?" or (x!="0" and (x==y or y=="0"))
        more_general_parts.append(mg)
    
    return all(more_general_parts)
   
def consistent(example,hypothesis):
    return more_general(hypothesis,example)
    

def get_domains(examples):
    d=[set() for i in examples[0]]
    for x in examples:
        for i,xi in enumerate(x):
            d[i].add(xi)
            
    return [list(sorted(x)) for x in d]

def g_0(n):
    return ("?",)*n

def s_0(n):
    return ("0",)*n

def min_generalizations(h,x):
    h_new=list(h)
    
    for i in range(len(h)):
        
        if not consistent(x[i:i+1],h[i:i+1]):
            if h[i]=="0":
                h_new[i]=x[i]
            else:
                h_new[i]="?"
    return [tuple(h_new)]
    
    
    
def min_specializations(h,domains,x):
    results=[]
    for i in range(len(h)):
        
        if h[i]=="?":
            for val in domains[i]:
                if x[i]!=val:
                    h_new = h[:i] + (val,) + h[i+1:]
                    results.append(h_new)
                    
        else:
            h_new=h[:i]+("0",)+h[i+1:]
            results.append(h_new)
       
    return results
            
        
    

def candidate_elimination(examples):
#     print(examples)
    domains=get_domains(examples)[:-1]
    
    G=set([g_0(len(domains))])
    S=set([s_0(len(domains))])
    i=0
    
    print("\nG[{0}]".format(i),G)
    print("\nS[{0}]".format(i),S)
    for xcx in examples:
        print("\n",xcx)

        i+=1
        x,cx=xcx[:-1],xcx[-1]
        
        if cx=="Yes":
            G={g for g in G if consistent(x,g)}
            S=generalize_S(x,G,S)
        else:
            S={s for s in S if not consistent(x,s)}
            G=specialize_G(x,domains,G,S)
            
        print("\nG[{0}]".format(i),G)
        print("\nS[{0}]".format(i),S)
        
    return 
     
def generalize_S(x,G,S):
    S_prev=list(S)
    for s in S_prev:
        if s not in S:
            continue
        if not consistent(x,s):
            S.remove(s)
            s_plus=min_generalizations(s,x)
            S.update([s for s in s_plus if any([more_general(g,s) for g in G])])
            S.difference_update([h for h in S if any([more_general(h,h1) for h1 in S if h!=h1])])
    return S
       
def specialize_G(x,domains,G,S):
    G_prev=list(G)
    
    for g in G_prev:
        if g not in G:
            continue
        if consistent(x,g):
            G.remove(g)
            g_minus=min_specializations(g,domains,x)
            G.update([g for g in g_minus if any([more_general(g,s) for s in S])])
            G.difference_update([h for h in G if any([more_general(h1,h) for h1 in G if h!=h1])])
    return G

candidate_elimination(examples)
