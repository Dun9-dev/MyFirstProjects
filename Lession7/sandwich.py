sandwich_orders = ['pastrami', 'cheese', 'pastrami', 'tuna', 'pastrami', 'meet']
finished_sandwiches = []

while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    if 'pastrami' in sandwich_orders:
        print('Как же так, ужос')

    for i in sandwich_orders:
        old_san = sandwich_orders.pop()
        print(f"I made you {old_san} sandwich")

        finished_sandwiches.append(old_san)
        #print(finished_sandwiches)

print("Приготовленные сендвичи: ")
for i in finished_sandwiches:
    print(i)
