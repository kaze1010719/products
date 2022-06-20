#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue # 繼續
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

# 讓使用者輸入
# while 適合用在不知有幾次的情況
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)

	#方法一
	#p = []
	#p.append(name)
	#p.append(price)
	#products.append(p)

	#方法二
	#p = [name, peice]
	#products.append(p)

	#方法三
	products.append([name, price])

print(products)
print(products[1][0])

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:  # open只有打開而已，還沒寫入
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  # 才有真正寫入