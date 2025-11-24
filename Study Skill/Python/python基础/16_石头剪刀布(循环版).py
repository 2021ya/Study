import random  # 导入模块工具包（随机）


print("Welcome to my game!")


while True:
    player = input("请输入你的选择（石头/剪刀/布/退出）：")
    # AI选择规则1(AI必赢)
    if player == "石头":  # 判断胜负时也可用or，例如："if () or () or ():"
        AI = "布"
        print("player:我的选择是：%s" % player)
        print("AI:我的选择是：%s" % AI)
        print("AI:Win / Player:Fail")
    elif player == "剪刀":
        AI = "石头"
        print("player:我的选择是：%s" % player)
        print("AI:我的选择是：%s" % AI)
        print("AI:Win / Player:Fail")
    elif player == "布":
        AI = "剪刀"
        print("player:我的选择是：%s" % player)
        print("AI:我的选择是：%s" % AI)
        print("AI:Win / Player:Fail")
    elif player == "system":  # 系统权限
        print("SYSTEM PERMISSIONS")
        while True:
            system = input("SYSTEM(choose AI / auto AI / exit system):")
            if system == "choose AI":
                AI = input("Please enter AI choose（石头/剪刀/布）:")  # 系统权限，直接定义AI选择
            elif system == "auto AI":
                print("Auto AI")
                AI_choose = random.randint(1, 3)  # 从1-3中随机选一个数
                if AI_choose == 1:
                    AI = "石头"
                elif AI_choose == 2:
                    AI = "剪刀"
                elif AI_choose == 3:
                    AI = "布"
                else:
                    print("System AI Choose Error!")
            elif system == "exit system":
                break
            else:
                AI = 0  # 选择错误时自动定义为0，以防后面执行代码报错
                # if not AI != "石头" or "剪刀" or "布":
                """
                实际执行顺序为：if (not (AI != "石头")) or ("剪刀") or ("布"):，符号优先级:!= > not > or
                if not AI != "石头" or "剪刀" or "布":这句代码中，因为!=的优先级大于not，not的优先级又大于or，
                所以我假设输入“布”然后执行代码时，AI != "石头"是正确的，所以是Ture,但又因为not优先级大于or，所以先执行not，
                但是如果先执行not的话，not Ture就变为False了，然后实际代码变为了if false or "剪刀" or "布":，这时，
                下一个执行优先级就是or了，然后有因为非空字符串都为Ture，所以“剪刀”变为了Ture，然后实际代码又变成了if False or Ture or
                 "布":，这时三个or中有一个是Ture,所以最终执行了print("Unknown System Error!")
                """
            if AI not in ["石头", "剪刀", "布"]:
                print("System Choose Error! / AI Choose Error!")
                continue
            else:
                player = input("请输入你的选择（石头/剪刀/布）：")
                # AI规则2(公平规则)
                if ((player == "石头" and AI == "剪刀")   # 代码太长用换行
                        or (player == "剪刀" and AI == "布")
                        or (player == "布" and AI == "石头")):
                    print("player:我的选择是：%s" % player)
                    print("AI:我的选择是：%s" % AI)
                    print("Player:Win / AI:Fail")
                elif (AI == "石头" and player == "剪刀") or (AI == "剪刀" and player == "布") or (AI == "布" and player == "石头"):
                    # 原版（不用换行）
                    print("player:我的选择是：%s" % player)
                    print("AI:我的选择是：%s" % AI)
                    print("AI:Win / Player:Fail")
                elif player == AI:
                    print("player:我的选择是：%s" % player)
                    print("AI:我的选择是：%s" % AI)
                    print("Draw!")
                else:
                    print("Unknown rule2 Error!")
                    continue
    elif player == "退出":
        break  # 结束程序
    else:
        print("Unknown Rule1 Error!")
        continue  # 错误，重新循环
