# simple iterator to input data category-wise for each institution
# output average for each category for each institution

"""""""""
A : Jalukbari State Home
B : Ambari State Home
C : Destination
D : Assam Sishu Kalyan Sadan

"A" : 29,
"B" : 22,
"C" : 21,
"D" : 28

"""

institutions = {
    "A": 29,
    "B": 22,
    "C": 21,
    "D": 28
}

categories = ["food_and_nutrition", "education", "shelter", "economic", "protection",
              "mental_health", "family", "health", "spirituality", "community"]

for category in categories:

    for k, v in institutions.items():
        print("Calculating for Institution : " + k + "; Category : " + category + "\n")
        score_list = []
        for count in range(1, v+1):
            score = float(input("Calculating for Institution : " + k + "; Category : " + category +
                                "; Count : " + str(count) + "; Score ? "))
            score_list.append(score)

        print("\nCount of score_list : " + str(len(score_list)))
        print(score_list)

        print("\nAverage score for " + category + " for Institution " + k + " : " +
              str(sum(score_list)/len(score_list)) + "\n")
