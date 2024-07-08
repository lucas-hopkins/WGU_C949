from operator import attrgetter


class Activity:
  def __init__(self, name, initial_start_time, initial_finish_time):
    self.start_time = initial_start_time
    self.finish_time = initial_finish_time
    self.name = name


  def conflicts_with(self, other_activity):
    if self.finish_time <= other_activity.start_time:
      return False

    elif other_activity.finish_time <= self.start_time:
      return False

    else:
      return True

def activity_selection(activities):
  chosen_activities = []

  activities.sort(key=attrgetter('finish_time'))
  current = activities[0]
  chosen_activities.append(current)

  for i in range(1, len(activities)):
    if not activities[i].conflicts_with(current):
      chosen_activities.append(activities[i])
      current = activities[i]

  return chosen_activities
  
if __name__ == '__main__':
  activity_1 = Activity('Fireworks show', 20, 21)
activity_2 = Activity('Morning mountain hike', 9, 12)
activity_3 = Activity('History museum tour', 9, 10)
activity_4 = Activity('Day mountain hike', 13, 16)
activity_5 = Activity('Night movie', 19, 21)
activity_6 = Activity('Snorkeling', 15, 17)
activity_7 = Activity('Hang gliding', 14, 16)
activity_8 = Activity('Boat tour', 11, 14)

activities = [ activity_1, activity_2, activity_3, activity_4,
               activity_5, activity_6, activity_7, activity_8 ]

# Use the activity_selection() method to get a list of optimal
# activities with no conflicts.               
itinerary = activity_selection(activities)
for activity in itinerary:
    # Output the activity's information.
    print('%s - start time: %d, finish time: %d' % 
         (activity.name, activity.start_time, activity.finish_time))