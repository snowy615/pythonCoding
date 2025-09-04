x_dir = {0, 0, 1, -1}
y_dir = {1, -1, 0, 0}
st = [[0 for i in range(col)] for j in range(row)]
def runShop(shop, p_x, p_y, item, row, col):
    x = p_x
    y = p_y
    while True:
        for i in range(4):


x = int(input())
for i in range(x):
    row, col, n_lis = map(int, input().split())
    shop = []
    items = []
    e_x = 0
    e_y = 0
    for j in range(row):
        r = input()
        shop.append(r)
        if "e" in r:
            e_x = r.find("e")
            e_y = j
    for j in range(n_lis):
       runShop(shop, e_x, e_y, input(), row, col)
