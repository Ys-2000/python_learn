height = int(input('输入身高:'))
weight = int(input('输入体重:'))

# 转换身高为米
height = height / 100

bmi = weight / (height ** 2)
print("您的身高是",height,",体重是",weight, "bim=%.2f" %bmi)
if bmi < 18.5:
    print("过轻")
elif bmi <= 25:
    print("正常")
elif bmi <= 32:
    print("肥胖")
else:
    print("严重肥胖")



# chatGPT生成
def calculate_bmi(height, weight):
    # 转换身高为米
    height_m = height / 100

    # 计算BMI指数
    bmi = weight / (height_m ** 2)

    return bmi

def get_weight_status(bmi):
    if bmi < 18.5:
        return "过轻"
    elif 18.5 <= bmi < 25:
        return "正常"
    elif 25 <= bmi < 28:
        return "过重"
    elif 28 <= bmi < 32:
        return "肥胖"
    else:
        return "严重肥胖"

# 小明的身高和体重
height_cm = 180
weight_kg = 180

# 计算BMI指数
bmi_index = calculate_bmi(height_cm, weight_kg)

# 获取体重状况
weight_status = get_weight_status(bmi_index)

print(f"小明的BMI指数为: {bmi_index:.2f}")
print(f"体重状况: {weight_status}")
