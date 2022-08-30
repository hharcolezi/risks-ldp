import numpy as np

# [1] Arcolezi et al (2021) "Random Sampling Plus Fake Data: Multidimensional Frequency Estimates With Local Differential Privacy" (ACM CIKM).

def SB_RSpFD_UE_Zero(total_reports, p, q, d, k, n):
    """
    Estimation on the number/frequency of times each value has been reported.
    input: all LDP+fake encoded reports 'total_reports', probabilities p and q, 
    number of attributes d, number of values of this attribute k, and number of users n
    output: estimated frequency
    """
   
    Nb_S = sum(total_reports) #how many times each value has been reported
    
    est =  np.array(d*(Nb_S  - n*q) / (n*(p-q))).clip(0) #estimation clipped in 0 for re-normalization
    
    freq_est = est / sum(est) #re-normalized estimated frequency
    
    return freq_est

def SB_RSpFD_GRR(total_reports, p, q, lst_val, d, k, n):
    """
    Estimation on the number/frequency of times each value has been reported [1].
    input: all LDP+fake reports 'total_reports', probabilities p and q, domain values 'lst_val', 
    number of attributes d, number of values of this attribute k, and number of users n
    output: estimated frequency
    """

    Ni = {val:0 for val in lst_val}

    for val in total_reports: #how many times each value has been reported
        Ni[val]+=1

    for key in Ni.keys(): #estimated number of times with Eq. (4)
        val =  ( (Ni[key] * d * k) - n * (d - 1 + q*k)) / (n*k*(p-q)) 
        if val > 0:
            Ni[key] = val
        else: # if negative, we'll clip to 0 and re-normalize.
            Ni[key] = 0
            
    total = sum(Ni.values()) #for re-normalization
    for key in Ni.keys():
        Ni[key] = Ni[key]/total
    return np.array(list(Ni.values()))
    
def SB_RSpFD_UE(total_reports, p, q, d, k, n):
    """
    Estimation on the number/frequency of times each value has been reported [1].
    input: all LDP+fake encoded reports 'total_reports', probabilities p and q, 
    number of attributes d, number of values of this attribute k, and number of users n
    output: estimated frequency
    """
   
    Nb_S = sum(total_reports) #how many times each value has been reported
       
    #estimated number with Eq. (10) clipped in 0 for re-normalization
    est = np.array(((Nb_S * d * k) - n * (q*k + (p-q)*(d-1) + q*k*(d-1))) / (n*k*(p-q))).clip(0)
    
    #re-normalized estimated frequency
    freq_est = est / sum(est)
    
    return freq_est
