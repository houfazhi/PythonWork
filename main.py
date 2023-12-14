
my_dict = {
    '标识符': 'IDENFR',
    '整型常量': 'INTCON',
    '字符常量': 'CHARCON',
    '字符串': 'STRCON',
    'const': 'CONSTTK',
    'int': 'INTTK',
    'char': 'CHARTK',
    'void': 'VOIDTK',
    'main': 'MAINTK',
    'if': 'IFTK',
    'else': 'ELSETK',
    'do': 'DOTK',
    'while': 'WHILETK',
    'for': 'FORTK',
    'scanf': 'SCANFTK',
    'printf': 'PRINTFTK',
    'return': 'RETURNTK',
    '+': 'PLUS',
    '-': 'MINU',
    '*': 'MULT',
    '/': 'DIV',
    '<': 'LSS',
    '<=': 'LEQ',
    '>': 'GRE',
    '>=': 'GEq',
    '==': 'EQL',
    '!=': 'NEQ',
    '=': 'ASSIGN',
    ';': 'SEMICN',
    ',': 'COMMA',
    '(': 'LPARENT',
    ')': 'RPARENT',
    '[': 'LBRACK',
    ']': 'RBRACK',
    '{': 'LBRACE',
    '}': 'RBRACE'
}


# In[43]:


def is_numeric(i: str) -> bool:
    if i >= '0' and i <= '9':
        return True
    else:
        return False

def is_char(i: str) -> bool:
    return i.isalpha() and len(i) == 1


# In[45]:


one_token = ['+', '-', '/', '*', ',', '(', ')', '[', ']', '{', '}', ';']

# In[47]:


testfile_list = []
with open('testfile.txt', 'r') as testfile:
    for i in testfile:
        testfile_list.append(i.strip())

testfile_str = ' '.join(testfile_list)

# In[48]:


token_type = []
token_list = []

i = 0
end_count = len(testfile_str)

mycount = 0

mid = ''
while True:

    if i >= end_count:
        break

    if testfile_str[i] == ' ':
        i = i + 1
        if i >= end_count:
            break

    # 识别字母
    if is_char(testfile_str[i]) or testfile_str[i] == '_':
        while is_char(testfile_str[i]) or is_numeric(testfile_str[i]) or testfile_str[i] == '_':
            mid = mid + testfile_str[i]
            i = i + 1

        if mid in my_dict:
            token_type.append(my_dict[mid])
            token_list.append(mid)
            mid = ''

        else:
            token_type.append(my_dict['标识符'])
            token_list.append(mid)
            mid = ''

    # 识别数字
    if is_numeric(testfile_str[i]):

        while is_numeric(testfile_str[i]):
            mid = mid + testfile_str[i]
            i = i + 1
        token_type.append(my_dict['整型常量'])
        token_list.append(mid)
        mid = ''

    # 识别字符常量
    if testfile_str[i] == '\'':
        mid = testfile_str[i + 1]
        i = i + 3

        token_type.append(my_dict['字符常量'])
        token_list.append(mid)

        mid = ''

    # 识别字符串
    if testfile_str[i] == '\"':
        i = i + 1
        while testfile_str[i] != '\"':
            mid = mid + testfile_str[i]
            i = i + 1

        token_type.append(my_dict['字符串'])
        token_list.append(mid)

        mid = ''
        i = i + 1

    # 识别<= <  > >= = ==  两级判断
    if testfile_str[i] == '<' or testfile_str[i] == '>' or testfile_str[i] == '=':
        mid = mid + testfile_str[i]
        i = i + 1

        if testfile_str[i] == '=':
            mid = mid + testfile_str[i]
            i = i + 1

        token_type.append(my_dict[mid])
        token_list.append(mid)

        mid = ''

    if testfile_str[i] == '!':
        mid = mid + testfile_str[i:i + 2]
        i = i + 2

        token_type.append(my_dict[mid])
        token_list.append(mid)

        mid = ''

    # 识别+ - * / ； () 等一级单位
    if testfile_str[i] in one_token:
        mid = mid + testfile_str[i]
        i = i + 1

        token_type.append(my_dict[mid])
        token_list.append(mid)

        mid = ''

# In[37]:


with open('output.txt', 'w') as output:
    for item1, item2 in zip(token_type, token_list):\
        # output.write("{} {}\n".format(item1,item2))
        output.write(f'{item1} {item2}\n')

# In[ ]:


# jupyter nbconvert --to script demo5.ipynb

