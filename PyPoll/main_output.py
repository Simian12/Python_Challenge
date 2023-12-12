import csv
def_vote_data=("C:\\Users\\Banni\\Desktop\\Python_Challenge\\PyPoll\\Resources\\election_data.csv")
output_file=("C:\\Users\\Banni\\Desktop\\Python_Challenge\\PyPoll\\Analysis\\election_results.txt")

candidate_votes={}

with open(def_vote_data) as File:
    reader=csv.reader(File)

    for row in reader:
        candidate=row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate]=+1
        else:
            candidate_votes[candidate]=1

total_votes=sum(candidate_votes.values())
candidate_percentage={name:(votes/total_votes)*100 for name, votes in candidate_votes.items()}
winner=max(candidate_votes, key=candidate_votes.get)

with open(output_file, 'w') as Final_output:
    Final_output.write("Election_results\n")
    Final_output.write("-------------------\n")
    Final_output.write(f"Total votes:{total_votes}\n")
    Final_output.write("--------------------\n")

    for candidate,total_votes in candidate_votes.items():
        percentage= round(candidate_percentage[candidate],3)
        Final_output.write(f"{candidate}:{percentage}%({bytes})\n")

    Final_output.write("----------------------\n")
    Final_output.write(f"Winner:{winner}\n")
    Final_output.write("------------------------\n")

    print(output_file)

