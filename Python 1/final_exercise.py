# Brian Wolfe                       Created: 11/15/2020
candidates = {}  # Creates main dictionary


def display_instructions():
    print("Enter the last name of 3 candidates followed by the total number of votes they received.")


def display_header():
    print("{:-<40}".format(""))
    print("{:^40}".format("Final Exercise"))
    print("{:^40}".format("Vote Tally"))
    print("{:-<40}".format(""))
    print()
    display_instructions()
    print()


def get_candidates():
    value_testing = True
    name_testing = True
    vote_testing = True
    candidate = {}  # Create dictionary to hold data
    count = 0

    # MAIN LOOP TO GATHER NO MORE OR LESS THAN 3 CANDIDATES
    while count < 3:
        while value_testing:  # Loop to test entered values

            # TEST CANDIDATE NAME
            if name_testing:
                candidate['lname'] = input("Enter a candidate's last name: ").title()
                for letter in candidate['lname']:
                    if letter.isspace() or not letter.isalpha():  # Make sure the name contains no spaces or numbers
                        print("INVALID ENTRY:  Candidate's name must be a single name of only letters.")
                        print("\t\t\t\tPlease try again.")
                        name_testing = True
                        break  # No point testing if a failure occurs
                    else:
                        name_testing = False

            # TEST VOTES VALUE
            if vote_testing and not name_testing:
                candidate['votes'] = input(f"Enter {candidate['lname']}'s total votes: ")
                for letter in candidate['votes']:
                    # Keeping votes as a string now helps to logic test easier for valid data input
                    if letter.isspace() or not letter.isdigit():  # Make sure the vote contains no spaces or letters
                        print("INVALID ENTRY:  Votes must be a positive number only.")
                        print("\t\t\t\tPlease try again.")
                        vote_testing = True
                        break  # No point testing if a failure occurs
                    else:
                        vote_testing = False

            # WHEN NAME & VOTE TESTING COMPLETE, ADD TO CANDIDATES & RESET FOR NEXT TEST
            if name_testing == False and vote_testing == False:
                candidate['votes'] = int(candidate['votes'])  # Convert vote to integer
                candidates[count] = candidate  # Add vetted values to main dictionary

                # Reset for the next tests
                candidate = {}  # Cleans for next entry loop
                name_testing = True
                vote_testing = True
                count += 1
                print()

            # IF ALL CANDIDATES ARE ENTERED, EXIT THE MAIN LOOP
            if count == 3:
                value_testing = False


def calculate_votes():
    # CALCULATE TOTAL VOTES RECEIVED
    total_votes = 0
    for i in range(len(candidates)):
        candidate = candidates[i]
        total_votes += candidate['votes']

    # CALCULATE PERCENTAGE OF VOTES PER CANDIDATE
    for i in range(len(candidates)):
        candidate = candidates[i]
        candidate['percentage'] = candidate['votes'] / total_votes

    return total_votes


def get_winner():
    tie_count = 0
    tie_names = []

    # GET THE HIGHEST VOTE VALUE
    winning_votes = max([candidate['votes'] for candidate in candidates.values()])

    # TEST IF THERE IS A TIE: 1 = WINNER, 2 = TIE, 3 = NO WINNERS
    for i in range(len(candidates)):
        candidate = candidates[i]
        if candidate['votes'] == winning_votes:
            tie_count += 1

    # GET THE WINNER'S NAME
    if tie_count == 3:
        print(f"{tie_count}-WAY TIE! There are no winners!")
    elif tie_count == 2:
        for i in range(len(candidates)):
            candidate = candidates[i]
            if candidate['votes'] == winning_votes:
                tie_names.append(candidate['lname'])
        print(f"{tie_count}-WAY TIE! {tie_names[0]} and {tie_names[1]} tied with {winning_votes} votes each!")
    elif tie_count == 1:
        for i in range(len(candidates)):
            candidate = candidates[i]
            if candidate['votes'] == winning_votes:
                print(f"{candidate['lname']} is the winner with {winning_votes:,} votes received!")


def display_final():
    print("{:-<60}".format(""))
    print("{:^15}|{:^15}|{:^30}".format("Name", "Votes", "% of Total Votes"))
    print("{:-<60}".format(""))

    total_votes = calculate_votes()  # Process votes to ready results for display

    for i in range(len(candidates)):
        candidate = candidates[i]
        print("{:^15}|{:^15,}|{:^30.1%}".format(candidate['lname'], candidate['votes'], candidate['percentage']))

    print("{:-<60}".format(""))
    print("Total Votes: {:,} received\n".format(total_votes))

    get_winner()  # Determine winner and display their name


def main():
    display_header()
    get_candidates()
    display_final()


if __name__ == '__main__':
    main()
