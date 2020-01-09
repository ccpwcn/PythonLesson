# 简单的
info = {
    'name': 'wang',
    'age': 18,
    'in': '2019-10-12'
}

# 支持嵌套
student = {
    'name': 'wang',
    'class': {
        'level': 1,
        'score': 120,
        'teacher': 'Mr. li',
    }
}

# 复杂类型
students = [
    {
        'name': 's_1',
        'lesson': 'Language',
        'score': 100,
    },
    {
        'name': 's_2',
        'lesson': 'Language',
        'score': 110,
    }
]
menuTree = [
    {
        'name': '首页',
        'link': '/',
        'icon': './img/dashboard.png'
    },
    {
        'name': '客户管理',
        'link': '/customer.html',
        'icon': './img/customer_list.png'
    },
    {
        'name': '系统设置',
        'link': None,
        'icon': './img/settings.png',
        'children': [

            {
                'name': '角色信息',
                'link': '/role.html',
                'icon': './img/role_list.png'
            },
            {
                'name': '系统资源',
                'link': '/resource.html',
                'icon': './img/resource_list.png'
            }
        ]
    }
]

# 遍历Key和Value
for k, v in info.items():
    print('KEY {} => VALUE {}'.format(k, v))

# 另外一种遍历Key和Value的方式
for k in info:
    print(k, '\t', info[k])

# 仅遍历Key
for k in info.keys():
    print(k)

# 仅遍历Value
for _, v in info.items():
    print(v)

# 仅遍历Value的另一种方式
for v in info.values():
    print(v)
