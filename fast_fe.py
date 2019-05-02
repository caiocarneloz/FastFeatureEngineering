import pandas as pd
import numpy as np









'diff'
'abs_diff'
'sum'
'div'
'onehot'
'norm'

def operation(res, a, b):
    
    if res == 'add':
        return a+b
    if res == 'sub':
        return a-b
    if res == 'div':
        return a/b
    if res == 'mul':
        return a*b
    if res == 'abs_diff':
        return abs(a-b)
    
    return False
    

def fast_fe(df, col_dict):
    
    features_dict = {}
    
    for operator, result in {'add':'sum', 'sub':'diff', 'div':'quo', 'mul':'prod', 'abs_diff':'abs_diff'}.items():
        
        features_list = []
        if(result in col_dict.keys()):
            col_list = col_dict[result]
        
            for l in col_list:
                total = operation(operator, df[l[0]], df[l[1]])
                for col in range(2,len(l)):
                    total = operation(operator, total, df[l[col]]) 
                df[result+'_'+'_'.join(l)] = total
                features_list.append(result+'_'+'_'.join(l))
                
            
            features_dict[result] = features_list
    
    
    
#    
#    features_list = []
#    col_list = col_dict['sum']
#
#    for l in col_list:
#        diff = df[l[0]] + df[l[1]]
#        for col in range(2,len(l)):
#            diff += df[l[col]]
#        df['sum_'+'_'.join(l)] = diff
#        features_list.append('sum_'+'_'.join(l))
#        
#    
#    features_dict['sum'] = features_list
#    
#    
#    features_list = []
#    col_list = col_dict['div']
#
#    for l in col_list:
#        diff = df[l[0]] / df[l[1]]
#        for col in range(2,len(l)):
#            diff /= df[l[col]]
#        df['div_'+'_'.join(l)] = diff
#        features_list.append('div_'+'_'.join(l))
#        
#    
#    features_dict['div'] = features_list
#    
    

        
        
        

        
df = pd.DataFrame(pd.np.empty((10, 0)) * pd.np.nan)
df['end_time'] = 50
df['start_time'] = 20
col_dict = {}
col_dict['diff'] = [['end_time','start_time']]
col_dict['sum'] = [['end_time','start_time']]
col_dict['quo'] = [['end_time','start_time']]
col_dict['prod'] = [['end_time','start_time']]
col_dict['abs_diff'] = [['end_time','start_time']]