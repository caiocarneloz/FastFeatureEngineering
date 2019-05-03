import pandas as pd

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
    
    features_list_arithmetic = []
    
    for operator, result in {'add':'sum', 'sub':'diff', 'div':'quo', 'mul':'prod', 'abs_diff':'abs_diff'}.items():
        
        
        if(result in col_dict.keys()):
            col_list = col_dict[result]
        
            for l in col_list:
                total = operation(operator, df[l[0]], df[l[1]])
                for col in range(2,len(l)):
                    total = operation(operator, total, df[l[col]]) 
                df[result+'_'+'_'.join(l)] = total
                features_list_arithmetic.append(result+'_'+'_'.join(l))
                
            
    
    
    features_list_onehot = []
    
    for col in col_dict['onehot']:
        labels = df[col].unique()
        labels = labels[~pd.isnull(labels)]
        
        for l in labels:
            features_list_onehot.append(col+'_'+str(l))
            df[col+'_'+str(l)] = (df[col] == l).astype(int)
            
        if(df[col].isnull().values.any()):
            df[col+'_'+'NaN'] = (df[col].isna()).astype(int)
            features_list_onehot.append(col+'_'+'NaN')
                
            
    
    
    features_list_norm = []
    
    for col in col_dict['norm']:
        df['norm_'+col] = df[col]-df[col].mean()/df[col].std()
        features_list_norm.append('norm_'+col)
    
    features_dict = {}
    features_dict['arithmetic'] = features_list_arithmetic
    features_dict['onehot'] = features_list_onehot
    features_dict['normalized'] = features_list_norm
    
    return df, features_dict


    
df = pd.DataFrame(pd.np.empty((10, 0)) * pd.np.nan)
df['end_time'] = 50
df['start_time'] = 20
df.loc[0:3,'type'] = 'first'
df.loc[3:8,'type'] = 'last'
df['size'] = range(0,10)

col_dict = {}
col_dict['diff'] = [['end_time','start_time'], ['start_time','end_time']]
col_dict['sum'] = [['end_time','start_time']]
col_dict['quo'] = [['end_time','start_time']]
col_dict['prod'] = [['end_time','start_time']]
col_dict['abs_diff'] = [['end_time','start_time']]
col_dict['onehot'] = ['type']
col_dict['norm'] = ['size']