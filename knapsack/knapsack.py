from operator import attrgetter

class Item:
      def __init__(self, weight, value):
            self.weight = weight
            self.value = value

class Knapsack:
      def __init__(self, items, weight):
            self.items = items
            self.max_weight = weight


def sort_and_add_to_knapsack(knapsack, item_list):
      item_list.sort(key = attrgetter('value'), reverse = True)

      remaining = knapsack.max_weight
      for item in item_list:
            if item.weight <= remaining:
                  knapsack.items.append(item)
                  remaining = remaining - item.weight


if __name__ == '__main__':
      item_list = []
      initial_knapsack_list = []


      item_list.append(Item(6, 25))
      item_list.append(Item(8, 42))
      item_list.append(Item(12, 60))
      item_list.append(Item(18, 95))

      knapsack = Knapsack(items=initial_knapsack_list, weight=32)

      sort_and_add_to_knapsack(knapsack, item_list)

      i = 1
      sum_weight = 0
      sum_value = 0

      for item in knapsack.items:
            sum_weight += item.weight
            sum_value += item.value
            print('%d: weight %d, value %d' % (i, item.weight, item.value))
            i+=1
            print()
      
      print('Total weight of items in knapsack: %d' % sum_weight)
      print('Total value of items in knapsack: %d' % sum_value)
