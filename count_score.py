def score_counter( score_list ):
    nagative = 0
    neutral = 0
    positive = 0
    for score in score_list:
        if score in [1,2,3,4,5]:
            nagative = nagative + 1
        elif score in [6,7,8]:
            neutral = neutral + 1
        else:
            positive = positive + 1
    print("Nagative", nagative)
    print("Neutral", neutral)
    print("Positive", positive)
score_counter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
