n = int(input("初期金額を入力してください："))
x = int(input("消費金額を入力してください："))
m = n - x

coin = [500, 100, 50, 10]
coin_count = {500: 5, 100: 5, 50: 5, 10: 5}

possible = True
refund_details = []

for c in coin:
    refund_coin = min(m // c, coin_count[c])
    m -= refund_coin * c
    coin_count[c] -= refund_coin
    
    if refund_coin > 0:
        refund_details.append(f"{c}円玉が{refund_coin}枚")

if m > 0:
    possible = False

if possible:
    print("お釣りは：")
    for detail in refund_details:
        print(detail)
    print("になります")
else:
    print("お釣りできません。自動販売機に十分なコインがありません。")
