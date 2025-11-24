class PasswordFormatError(Exception):  # 使用类来创造自定义错误类型，括号中需要继承Exception类
    """密码格式错误自定义异常类型"""
    pass  # 无需自定义其他信息，直接pass，如果要自定义信息自行修改


def user_password():

    user_input_password = input("Please input your password: ")

    if len(user_input_password) >= 8:
        return user_input_password
    password_format_error = PasswordFormatError("Password is too short!")  # 创建异常对象，使用变量来接收异常信息，然后PasswordFormatError()来创建异常信息
    raise password_format_error  # 抛出异常，使用raise来抛出异常


try:  # 尝试执行
    user_password()
except PasswordFormatError as result:  # 捕捉异常
    print(result)
except Exception as result:  # 未知错误捕捉
    print(result)
else:  # 若执行成功，执行下方代码
    print("执行成功")
finally:  # 最后执行的代码
    print("执行完毕")

