# playing with 'in-line conditionals'
threshold = 8
for i in range(0, 13, 3):
    position = "below" if i < threshold else "above"
    print("the iterator " + str(i) + " is " + position + " " + str(threshold))
