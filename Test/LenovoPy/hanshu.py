


def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()        # 首字母大写


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# def greet_users(names):
#     """向列表中的每位用户都发出简单的问候"""
#     for name in names:
#         msq = "Hello," + name.title() + "!"
#         print(msq)
#
#
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)


# # 首先创建一个列表，其中包含一些要打印的设计
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# # 模拟打印每个设计，直到没有未打印的设计为止
# # 打印每个设计后，都将其移到列表completed_models中
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     # 模拟根据设计制作3D打印模型的过程
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)
#
# # 显示打印好的所有模型
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


# def print_models(unprinted_designs, completed_models):
#     """
#     模拟打印每个设计，直到没有未打印的设计为止
#     打印每个设计后，都将其移到列表completed_models中
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         # 模拟根据设计制作3D打印模型的过程
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     """显示打印好的所有模型"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)
