# 反转字符转
def reverse(text):
    return text[::-1]


# 把字符串转换成元祖
# def reverse_to_tuple(text):
#     while(len(text) > 0):


# 判断是否反转
def is_palindrome(text):
    print(text.rjust())
    return text == reverse(text)


# input方法接收一个字符串作为参数 并返回一个字符串
something = input('Enter text: ')

# 判断并执行输出
if is_palindrome(something):

    print('its a palindrome')
else:
    print('its not a palindrome')
