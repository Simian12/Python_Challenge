import csv
def_vote_data=("C:\\Users\\Banni\\Desktop\\Python_Challenge\\PyPoll\\Resources\\election_data.csv")
candidate_votes={}
with open("C:\\Users\\Banni\\Desktop\\Python_Challenge\\PyPoll\Resources\\election_data.csv") as File:
    reader=csv.reader(File)

    for row in reader:
        candidate=row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate]+=1
        else:
            candidate_votes[candidate]=1

total_votes=sum(candidate_votes.values())

candidate_percentage={name:(votes/total_votes)*100 for name,votes in candidate_votes.items()}

winner=max(candidate_votes,key=candidate_votes.get)

print("Election Results")
print("--------------------")
print(f"Total votes:{total_votes}")
print("----------------------")

for candidate, votes in candidate_votes.items():
    percentage=round(candidate_percentage[candidate],3)
    print("{}:{}%({})".format(candidate,percentage,votes))

print("-------------------------")
print(f"Winner{winner}")
print("---------------------------")

