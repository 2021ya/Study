"""
需求：
    一个玩家可以自定义移动位置，上下左右
"""


def map_x_y():
    """
    通过传入列表和步数来控制方向
    x_or_Y 是一个列表，可以选择x轴或y轴来进行位移，需要位移的轴写1，否则写0
    step 是位移数
    """
    # 初始坐标
    coordinate_init = [0, 0]

    def player(x_or_y, step):
        # 坐标运算
        new_x = coordinate_init[0] + x_or_y[0] * step
        new_y = coordinate_init[1] + x_or_y[1] * step
        # 记录坐标数据-没有重新定义变量，只是修改其中的值不需要nonlocal函数
        coordinate_init[0] = new_x
        coordinate_init[1] = new_y
        return tuple(coordinate_init)  # 结果返回元组
    return player


if __name__ == '__main__':
    player1 = map_x_y()
    print(player1([1, 0], 10))
    print(player1([0, 1], 20))
    print(player1([-1, 0], 10))




