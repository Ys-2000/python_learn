from admin import admin_blue


# admin模块
@admin_blue.route('/alluser')
def alluser():
    return 'alluser'


@admin_blue.route('/deluser')
def deluser():
    return 'deluser'