import cast_tools

while True:
    cast_tools.show_main()
    action = input('请选择操作功能')
    print('您的选择是%s' %action)

    if action in ['1','2','3']:
        if action == '1':
            cast_tools.new_card()
        elif action == '2':
            cast_tools.show_all()
        elif action == '3':
            cast_tools.search_card()
    elif action == '0':
        print('欢迎下次使用')
        break
    else:
        print('您的操作有误,请重新选择')