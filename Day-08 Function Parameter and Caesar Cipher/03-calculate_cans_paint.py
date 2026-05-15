def paint_calc(height, width, cover):
    paint = round((height * width) / cover)
    # or you can use lake this
    # area = height * width
    # num_of_cans = math.ceil(area / cover)
    # print(f"You'll need {num_of_cans} cans of paint.")
    print(f"You'll need {paint} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of Wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)