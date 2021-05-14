



def dynamic_programming(weight_of_knapsack, numbers_of_object, weight_of_object, val):

    dp = [[0]*(weight_of_knapsack+1) for col in range(numbers_of_object+1)]

    for i in range(1, numbers_of_object+1):
        for w in range(1, weight_of_knapsack+1):

            left_weight = w - weight_of_object[i-1]
            left_weight

            if(left_weight < 0): dp[i][w] = dp[i-1][w]

            else:
                dp[i][w] = max(dp[i-1][left_weight]+val[i-1], dp[i-1][w])
                temp = dp[i][w]
                temp
            
    return dp[numbers_of_object][weight_of_knapsack]

weight_of_object=[1,3,3,5,5,7,7,9]
val=[4,5,1,2,1,5,4,19]

weight_of_knapsack = 10
numbers_of_object = 8

ans = dynamic_programming(weight_of_knapsack, numbers_of_object, weight_of_object, val)
ans