items=[]
while True:
	name=input('Item (enter "finished" when done): ')
	if name.lower()=='finished':
		break
	quantity=int(input('Quantity: '))
	price=float(input('Price: '))
	items.append({'name':name,'price':price,'quantity':quantity})

print('-'*len('receipt')*2+'\n   Receipt\n'+'-'*len('receipt')*2)

total_price=0
for item in items:
	total_price+=item['price']*item['quantity']
	print('%d %s %.3fKD'%(item['quantity'],item['name'],item['price']))

print('-'*len('receipt')*2)
print('Total: %.3fKD'%(total_price))