card_list=[]

#展示菜单
def show_main():
    print('*'*50)
    print('欢迎使用【名片管理系统】')
    print('')
    print('1.新建名片')
    print('2.显示全部')
    print('3.查询名片')
    print('')
    print('0.退出系统')
    print('*'*50)

#新建名片
def new_card():
    #1.提示用户依次输入名片信息
    print('请输入信息')
    name=input('请输入姓名')
    phone=input('请输入号码')
    qq=input('请输入qq')
    email=input('请输入邮箱')
    #2.将名片信息保存到一个字典
    card_dict={'name':name,
               'phone':phone,
               'qq':qq,
               'email':email}
    #3.将字典添加到名片列表
    card_list.append(card_dict)
    # print(card_list)
    #4.成功信息
    print('成功添加%s名片' %card_dict['name'])

#显示全部
def show_all():
    print('-'*50)
    for card_dict in card_list:
        print('\t\t姓名\t\t号码\t\tqq\t\t邮箱')
        print('\t\t%s\t\t%s\t\t%s\t\t%s'%(card_dict['name'],
                                          card_dict['phone'],
                                          card_dict['qq'],
                                          card_dict['email']))
    print('-'*50)

    if len(card_list) == 0:
        print('没有任何名片')
        return

#搜索名片
def search_card():
    print('输入要搜索的名片')
    #1.提示要输入的名字
    find_name=input('请输入姓名')
    #2.遍历列表 这个很重要！
    print('-'*50)
    for card_dict in card_list:
        if find_name == card_dict['name']:
            print('\t\t姓名\t\t号码\t\tqq\t\t邮箱')
            print('\t\t%s\t\t%s\t\t%s\t\t%s' % (card_dict['name'],
                                              card_dict['phone'],
                                              card_dict['qq'],
                                              card_dict['email']))


            deal_card(card_dict)
            break
        else:
            print('没有该用户名片')
    print('-'*50)

#搜索名片附加功能。处理搜索的名片 进行删除/修改操作
def deal_card(find_list):
    print('【1】   删除'   '【2】  修改'   '【0】返回上级菜单')
    action=input('请选择执行的操作')
    if action == '1':
        print('删除操作')
        card_list.remove(find_list)

    elif action == '2':
        print('修改操作')
        
        # result_name=input('姓名:')
        # find_list['name']=inp(find_list['name'],result_name)

        find_list['name']=inp(find_list['name'],'姓名')
        find_list['phone']=inp(find_list['phone'],'号码')
        find_list['qq']=inp(find_list['qq'],'qq')
        find_list['email']=inp(find_list['email'],'邮箱')
        print('修改成功')

#修改操作 如果输入的值不变 则返回原来的值
#输入的值变化了 则返回输入的值
def inp(bu,gai):
    """
    如果名片进行修改了，则返回gai  如果未修改 则返回原来的值
    :param bu: 原来名片的值
    :param gai: 修改后名片的值
    :return:
    """

    #gai即为 '姓名' 即input('姓名')
    result = input(gai)
    if len(result)>0:
        return result
    # if len(gai)>0:
    #     return gai
    else:
        return bu

