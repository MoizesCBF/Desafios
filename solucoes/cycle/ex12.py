# Proposto por @L48J0R#4564

participants = int(input("Number of"
                 " participants: "))

positiveVotes = 0
negativeVotes = 0


for x in range(participants):
    vote = int(input("Vote 1 for yes or"
                     " 0 for no: "))
    if vote == 1:
        positiveVotes += 1
    elif vote == 0:
        negativeVotes += 1
    else:
        print("Invalid vote")
        x -= 1

if positiveVotes >= (2/3 * participants):
    print(1)
else:
    print(0)