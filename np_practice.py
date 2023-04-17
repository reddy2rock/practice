import numpy as np

data = np.array(
    [
    [0., 2., np.nan, np.nan, np.nan, np.nan, 0.39, 0.21, 0.54],
    [1., 0., 0.74, 0.22, 0.22, np.nan, np.nan, np.nan, np.nan],
    [2., 0., 0.65, 0.48, 0.79, np.nan, np.nan, np.nan, np.nan],
    [3., 1., np.nan, np.nan, np.nan, 0.76, 0.64, 0.99, 0.87]
    ]
    )

def getAnswer(answer, pass_array):
    for num in pass_array:
        answer.extend(num)
    return answer
    

def solution(data):
    a, b, c = data[data[:,1]==0], data[data[:,1]==1], data[data[:,1]==2]
    
    a_real = a[:,~np.isnan(a[0,:])]
    b_real = b[:,~np.isnan(b[0,:])]
    c_real = c[:,~np.isnan(c[0,:])]
    
    a_pass = a_real[a_real[:,2]*0.3 + a_real[:,3]*0.3 + a_real[:,4]*0.4 >= 0.8][:,0]
    b_pass = b_real[b_real[:,2]*0.5 + (b_real[:,3]*0.3 + b_real[:,4]*0.4 + b_real[:,5]*0.3)*0.5 >= 0.75][:,0]
    c_pass = c_real[c_real[:,2]*0.3 + c_real[:,3]*0.4 + c_real[:,4]*0.3 >= 0.75][:,0]
    
    answer = np.concatenate((a_pass, b_pass, c_pass)).tolist()
        
    return answer

print(solution(data))

