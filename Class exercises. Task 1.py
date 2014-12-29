#Michelle Yick
#29-12-2014
#Lists class exercises. Task 1. Code improvement.

names = ['Jim', 'Bob', 'Alison', 'Jo', 'James']

element_sought = input('Enter the name you are searching for : ')
this_element = 0
found = False
while not found:
       if names[this_element] == element_sought:
          Found = True
       else:
          this_element = this_element + 1

if Found:
   print('{0} was in element {1} in the list'.format(element_sought, this_element))
else:
   print('Not found')
