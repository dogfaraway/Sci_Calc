## 凯撒密码的破解演示

## 假设已获得一段密文如下
## GUVF VF ZL FRPERG ZRFFNTR
## 先讲密文赋值给变量
message = "COCBKPIOAGCTRJQPG"
## 采用A~Z大写字母进行破解
## 将26个大写字母进行一次排列并赋值给‘生成密码本’：LETTERS
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

## 解决思路：把每个可能出现的密钥都循环生成一遍
## 采用循环结构,迭代变量key代表每一种可能的密钥

for key in range(len(LETTERS)):
    # translated设为空字符串，每次循环后必须清空以接受下一个新的循环密钥
    translated = ""

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) #.find()是方法，用来搜索密文字符的位置
            num = num - key

            # 检查是否小于0，
            if num <0:
                num = num + len(LETTERS)

            # 解密后的字符串追加到translated变量的末尾,组成句子
            translated = translated + LETTERS[num]

        else:
            translated  = translated + symbol # 密文里的symbol如果不在26个字母里，默认为标点符号追加到translated末尾

    ## 将密钥key和明文都打印出来
    print('Key #%s:%s' %(key, translated)) # %s,%(变量)是print函数中打印多个变量值的方法


