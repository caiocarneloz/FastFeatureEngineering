# fastfe
Fast feature engineering with simple operations using pandas for baseline purposes

## Getting Started
#### Dependencies
You need Python 3.5 or later to use fastfe. You can find it at [python.org](https://www.python.org/).

You aso need the pandas package, which is available from [PyPI](https://pypi.org). If you have pip, just run:
```
pip install pandas
```
#### Installation
Clone this repo to your local machine using:
```
git clone https://github.com/caiocarneloz/fastfe.git
```

## Features
- Get list of columns by specific data type
- Do arithmetic operations with columns
- Get abs difference between columns
- Onehot encode columns
- Normalize columns

## Usage
The fastfe function takes as argument a dataframe containing the data and a dictionary containing the desired output. The desired outputs are the dictionary keys while column names are the values. The possible outputs are represented by the following keys:

- **sum** - to get the sum of a set of columns
- **diff** - to get the difference between columns
- **quo** - to get de quotient between columns
- **prod** - to get the product between columns
- **abs_diff** - to get the abs difference between columns
- **onehot** - to onehot encode a set of columns
- **norm** - to normalize a set of columns

Arithmetic operations expects a list of lists, while onehot encoding and normalization expects a list.

## Example
With the following dummy dataset:
```
   column_1  column_2  column_3 column_4   column_5  column_6  column_7
0      8.76      2.98      3.30    type1  category2      5.90      7.67
1      3.56      3.89      8.75    type2  category2      6.48      2.08
2      2.76      6.75      2.73    type1  category1      3.07      1.72
3      6.89      7.03      4.72    type1  category2      3.97      9.28
4      5.46      6.45      4.37    type1  category1      9.07      7.74
5      1.18      4.72      2.18    type2  category1      8.13      2.85
6      3.30      0.30      6.65    type2  category2      3.11      3.67
7      8.10      0.58      9.36    type1  category1      3.19      0.22
8      3.73      6.83      4.27    type2  category2      9.88      4.01
9      5.65      8.01      0.31    type1  category1      7.83      2.89
```
we gonna create a dictionary to get:
- a column with the difference between column_1 and column_2
- columns with the sum of column_1 and column_2, and column_1, column_2 and column_3
- columns representing the onehot encoding of column_4 and column_5
- columns with column_6 and column_7 normalized

```python
op_dict = {}
op_dict['diff'] = [['column_1', 'column2']]
op_dict['sum'] = [['column_1', 'column_2'], ['column_1', 'column2', 'column_3']]
op_dict['onehot'] = ['column_4', 'column_5']
op_dict['norm'] = ['column_6', 'column_7']
```
as output, the function returns the dataframe and a dictionary with the index for the new columns:
```
df, features_dict = fastfe(df, op_dict)
```
df:
```
   column_1  column_2      ...       norm_column_6 norm_column_7
0      8.76      2.98      ...            3.580997      6.263216
1      3.56      3.89      ...            4.160997      0.673216
2      2.76      6.75      ...            0.750997      0.313216
3      6.89      7.03      ...            1.650997      7.873216
4      5.46      6.45      ...            6.750997      6.333216
5      1.18      4.72      ...            5.810997      1.443216
6      3.30      0.30      ...            0.790997      2.263216
7      8.10      0.58      ...            0.870997     -1.186784
8      3.73      6.83      ...            7.560997      2.603216
9      5.65      8.01      ...            5.510997      1.483216
```
features_dict:
```
{'arithmetic': 
['sum_column_1_column_2',
'sum_column_1_column_2_column_3',
'diff_column_1_column_2'],

 'onehot': 
 ['column_4_type1',
 'column_4_type2',
 'column_5_category1',
 'column_5_category2'],
 
 'normalized': 
 ['norm_column_6', 
 'norm_column_7']}
```



