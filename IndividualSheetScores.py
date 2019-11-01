# simple calculator to calculate the scores
# for individual categories and final score for each questionnaire

score_list = []

for count in range(1, 37):
    score = int(input("score for question " + str(count) + " ? "))
    score_list.append(score)

print("\nCount of score_list : " + str(len(score_list)))
print(score_list)

food_and_nutrition = (score_list[0] + score_list[1] + score_list[2])/3
education = (score_list[3] + score_list[4] + score_list[5] + score_list[6] + score_list[7])/5
shelter = (score_list[8] + score_list[9] + score_list[10])/3
economic = (score_list[11] + score_list[12] + score_list[13])/3
protection = (score_list[14] + score_list[15] + score_list[16] + score_list[17])/4
mental_health = (score_list[18] + score_list[19] + score_list[20] + score_list[21])/4
family = (score_list[22] + score_list[23] + score_list[24] + score_list[25])/4
health = (score_list[26] + score_list[27] + score_list[28] + score_list[29])/4
spirituality = (score_list[30] + score_list[31] + score_list[32])/3
community = (score_list[33] + score_list[34] + score_list[35])/3

print("\nThe food and nutrition score is " + str(food_and_nutrition))
print("The education score is " + str(education))
print("The shelter score is " + str(shelter))
print("The economic score is " + str(economic))
print("The protection score is " + str(protection))
print("The mental health score is " + str(mental_health))
print("The family score is " + str(family))
print("The health score is " + str(health))
print("The spirituality score is " + str(spirituality))
print("The community score is " + str(community))

print("\nThe final score is " + str(food_and_nutrition + education + shelter + economic + protection + mental_health
                                    + family + health + spirituality + community))
