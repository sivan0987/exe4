
import array as arr
from queue import Queue
###########A#############
# I started with the basic case (0,0,0) and added it to the list, then each time we removed the first member and added 2 new members.
# Each time we added a product to each participant
# We did this every time until we reach the last level (where we don't want to add more members) and print to the screen
def BFS( vec):

    queue = []
    # Make the source and enqueue it
    s = (0, 0 ,0)
    num = 0
    i = 1
    while num != len(vec):
        x = s[0]+vec[num]
        y = s[1] + vec[num]
        tuple1 = (x, s[1],num+1)
        tuple2 = (s[0], y ,num+1)
        queue.append(tuple1)
        queue.append(tuple2)
        s = queue.pop(0)
        i = i + 1
        num = s[2]
    while queue:
            s = queue.pop(0)
            print(s, end=" ")
            i = i + 1
    print(i)
###########B#############
#Every member that we wanted to add to the queue we checked if it already existed in the queue,
# if so we did not add it to the original queue and thus stopped the tree from that place
#i put the example (10,20,30,40) and we see that the the number of situations has decreased
def BFS2( vec):
    queue = []
    q1 =[]
    # Make the source and enqueue it
    s = (0, 0, 0)
    num = 0
    i = 1
    while num != len(vec):
        x = s[0] + vec[num]
        y = s[1] + vec[num]
        tuple1 = (x, s[1], num + 1)
        tuple2 = (s[0], y, num + 1)

        b = 0
        c = 0
        for item in q1:
            if item == tuple1 and item[2] == tuple1[2]:
                b = 1
            if item == tuple2 and item[2] == tuple2[2]:
                c = 1
        if b == 0:
            q1.append(tuple1)
            queue.append(tuple1)
        if c == 0:
            q1.append(tuple2)
            queue.append(tuple2)

        s = queue.pop(0)
        i = i + 1
        num = s[2]
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        i = i + 1
    print(i)


if __name__ == '__main__':

    mytuple = (10,20,30,40)
    BFS(mytuple)
    print (888)
    BFS2(mytuple)


