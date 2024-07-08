

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.fraction = 1.0

class Knapsack:
    def __init__(self, items, weight):
        self.items = items
        self.max_weight = weight

def fractional_knapsack(knapsack,item_list):
    item_list.sort(key = value_to_weight_ratio, reverse = True)

    remaining = knapsack.max_weight
    for item in item_list:
        if item.weight <= remaining:
              knapsack.items.append(item)
              remaining = remaining - item.weight
        else:
              item.fraction = remaining / item.weight
              knapsack.items.append(item)
              break

def value_to_weight_ratio(item):
    return item.value / item.weight

if __name__ == '__main__':
    item_list = []
    initial_knapsack_list = []


    item_list.append(Item(6, 25))
    item_list.append(Item(8, 42))
    item_list.append(Item(12, 60))
    item_list.append(Item(18, 95))

    knapsack = Knapsack(items=initial_knapsack_list, weight=38)
    fractional_knapsack(knapsack, item_list)

    print ('Objects in knapsack')
    i = 1
    sum_weight = 0
    sum_value = 0
    for item in knapsack.items:
        sum_weight += item.weight * item.fraction
        sum_value += item.value * item.fraction
        print ('%d: %0.1f of weight %0.1f, value %0.1f' % 
              (i, item.fraction, item.weight, item.value * item.fraction))
        i += 1
    print()

    # Display the total weight of the items as well as the total value.
    print('Total weight of items in knapsack: %d' % sum_weight)
    print('Total value of items in knapsack: %d' % sum_value)