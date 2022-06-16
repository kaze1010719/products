# while 適合用在不知有幾次的情況
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')

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


for p in products:
	print(p[0], '的價格是', p[1])


with open('products.csv', 'w') as f:  # open只有打開而已，還沒寫入
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')  # 才有真正寫入