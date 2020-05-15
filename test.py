'''
 @author:hanlu
 @Date:
 @description:python注释、变量
'''




# 1、python简介
    # 1、python是完全面向对象的语言
    # 2、python不通过；来表示语句结束，而是通过空格来表示语句块
'''
    注释知识点：
        1、单行注释  #
        2、多行注释  ''' '''

'''

# 这是单行注释

print("hello World")  # 行尾注释


'''
    多行注释

'''


# 2、变量和数据类型
 # 1、变量的定义和注意事项
    # 1、变量是用存储不同的数据类型的，表示指向对象的地址的值
    # 2、变量必须是以字母、下划线、$开头，不可以数字开头
    # 3、不需要声明变量的类型，是动态的类型分配

 # 2、数据类型
'''
    1、数字：  
        1、整形   
        2、长整数 
        3、浮点型  3.12
        4、复数 --用的不多
    2、字符串
        用''或者""表示字符串  支持切片操作 [2:] [0:4]（0到3的下标元素）
    3、布尔值   
        true或者false
    
    4、列表--有序，可变
        namelist = ['hanlu','dcp',2,3]   namelist[0:2]
        
    5、元祖--有序，不可变
        nametuple = (1,2,4)
    
    6、字典---无序
        dict = {'name':'hanlu','age':24,'class':2}  dict['name'] 
        
        判断key是否存在字典中
        'name' in dict == true
        
        返回所有的key
        dict.keys（）
        
        dict.values()
        
    7、set--无序，只存在key值，不可重复
        1、用于求取交集、并集 & |
        2、增加元素
            .add 如果添加的元素是重复的，set会自动去重
        3、删除元素
            .remove
        
        
    
'''
#
# nametuple = (1,2,4)
# for ele in nametuple:
#     print(ele)
#
# print(nametuple.count(1))
#
#
# #定义一个字典，无序,key值可以重复，但是后面的会覆盖前面的value值
# dictName = {1:'hanlu', 2:"dcp", 3:'lwt', 1:'hanlu2'}
#
# print(dictName[1])
#
# for key in dictName.keys():
#     print(dictName[key])
#
# #定一个set
#
# setName =  set([1,2,3]) #取出共同的值
# setName2 = set([3,4,5]) #将所有的值返回，重复的只显示一次
#
#
# print(setName & setName2)
# print(setName | setName2)
#
# # 3、运算符
#     # 1、算术运算符 + -  * / //(整除) % **
#     # 2、比较运算符 >  <  >= <= == !=         返回true或者false
#     # 3、赋值运算符 =
#     # 4、逻辑运算符 and  or  not 类似于Java的短路与 短路或 && ||
#     # 5、成员运算符 in  not in
#     # 6、身份运算符 is not is
#     # 5、位运算 & |  ^ ~ << >>
#
#
# # 4、 输入和输出
#     # 1、input()函数表示输入
#     # 2、print()函数表示输出
#
# print("请输入你的名字：")
# input2 = input();
# print(input)
#
#
# # 5、控制语句
#   # 1、判断 if  if...else   if elif else
# print("请输入一个数组")
# result = input()
#
# if result == '1':
#     print("你输入的是："+result)
#
#
# if result == '11':
#     print("你输入的是："+result)
#
# else:
#     print("你的输入错误，不是11")
#
# if result == "春":
#     print("输入："+result)
# elif result == "夏":
#     print("输入：" + result)
# else:
#     print("其他季节输"+result)
#
#     #2、循环 for while do...while
#
# for i in range(0,10):  #for循环
#     print(i)
#
#
# while(result == '2'):
#
#     print("输入成功："+result)
#
#
# # 6、列表
#     # 1、列表是用于存储各种类型数据，可以统一管理，和java中不同，java中list只能存储同一个类型数据
#
# name = ['hanlu','dcp','hpp','lwt']
#
# print(name[0])
#
#    # 2、增加列表元素 append insert
# name.append('baobao')
# name.append(1)
# for ele in name:
#     print(ele)
#
# print("===================")
# name.insert(0,'A')
# for ele in name:
#     print(ele)
# print("===================")
#
#    # 3、删除元素 pop方法、remove方法 del关键字
# name.pop(0) #删除指定位置的元素并返回元素
# for ele in name:
#     print(ele)
#
# print("===================")
# name.remove("hanlu") #通过对象名去删除元素
# for ele in name:
#     print(ele)
#
# print("===================")
# del name[1] #关键字删除指定位置元素
# for ele in name:
#     print(ele)
#
#     # 4、判断元素是否存在列表中
# if 'dcp' in name:
#     print("dcp 在列表name中")
#
#
# # 7、函数--提到代码的复用率 def关键字定义
#
# def testAdd(a,b):
#     return a+b
#
# aa = testAdd(3,4)
# print("aaa id "+(str)(aa))


# 8、面向对象

    # 1、通过class关键字来定义，内部有属性+方法
    # 2、属性的私有化，在属性前面加上两个下划线，表示私有__

class TestClass:



    def __init__(self,name,__age):
        self.name = name
        self.__age =__age  # 私有属性


    def get_age(self):

        return self.__age

    def set_oo(self,__age): #名字么没有特殊要求
        self.__age = __age

    def printAge(self):

        print(self.__age)

    def printName(self):
        print(self.name)


#class01 = TestClass('hanlu',12) #初始化对象,调用的是__init__初始化方法
#class01.set_oo(56)
#print(class01.get_age())

    # 3、类的继承
class Class02(TestClass): #表示继承

    def __int__(self,name,__age,__height):
        super(TestClass, self).__init__(name,__age) #调用父类的构造函数
        self.__height = __height

    # def get_height(self):
    #     return self.__height
    #
    # def set_height(self,__height):
    #     self.__height = __height
    def set_height(self,__height):
        self.__height = __height


    def get_height(self):
        return self.__height

    def printAge(self):
        print("这是父类的方法，进行重写")


aa = Class02('hanlu2111',34)

print("======父类方法和属性====")
print(aa.get_age())
aa.printAge()


print("===子类方法和属性")
# aa.set_height(160)
print(aa.get_height())


# 9、模块和包
 '''
    1、同一个包下文件可以直接通过import导入后使用 
        import json  就直接可以用模块的属性和方法 json.dumps()
        from  com.cn.staging import TestClass
        
    2、如果不在一个文件夹下，需要先手动导入包的路径，再导入包
        sys.path.append('/user/qingjiao/test')
        from test import TestClass
        
    3、包--一定是包含__init__.py
 
 '''