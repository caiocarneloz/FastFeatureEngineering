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

def getColumnsByType(df, column_type):
    
    return list(df.select_dtypes(include=[column_type]).columns)