# -*- coding: utf-8 -*-
#将列表list中的’tt’变成大写（用两种方式）
Li_data = [['k', ['qwe', 20, {'k1':['tt', 3, '1']}, 89], 'ab']]
#方法一:
Li_data[0][1][2]['k1'][0] = 'TT' #将tt变成大写TT
print(Li_data)
#方法二：
Li_data[0][1][2]['k1'][0] = Li_data[0][1][2]['k1'][0].upper()
print(Li_data)
#将列表中的数字3变成字符串'100'(用两种方式)
#方法一:
Li_data[0][1][2]['k1'][1] = '100'
print(Li_data)
#方法二:
Li_data[0][1][2]['k1'][1] = str(int(Li_data[0][1][2]['k1'][1]) + 97)
print(Li_data)
#将列表list中的’tt’变成大写（用两种方式）
Li_data = [['k', ['qwe', 20, {'k1':['tt', 3, '1']}, 89], 'ab']]
#方法一:
Li_data[0][1][2]['k1'][0] = 'TT' #将tt变成大写TT
print(Li_data)
#方法二：
Li_data[0][1][2]['k1'][0] = Li_data[0][1][2]['k1'][0].upper()
print(Li_data)
#将列表中的数字3变成字符串'100'(用两种方式)
#方法一:
Li_data[0][1][2]['k1'][1] = '100'
print(Li_data)
#方法二:
Li_data[0][1][2]['k1'][1] = str(int(Li_data[0][1][2]['k1'][1]) + 97)
print(Li_data)