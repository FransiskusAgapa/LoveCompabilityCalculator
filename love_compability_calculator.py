def calculate_love_score(n1,n2):
    sum_n1 = sum(ord(c) for c in n1)
    sum_n2 = sum(ord(c) for c in n2)
    return 0

    # score is based on the different between 'sum_n1' and 'sum_n2/


# start the project here
def start_the_love():
    print("\n== Love Compatibility Calculator ==\n")
    print("... where numbers tell you if it's true love,.. or just bad Wi-Fi ...")

    # get a person's name
    seeker_name = input("\n> What is your first name: ")

    # get the person's crush name
    seeker_crush_name = input("\n> What is your crush first name : ")

    # calculate score based on the names
    score = calculate_love_score(seeker_name,seeker_crush_name)

    # prince love 'score'
    print(f"\nYour love score is {score}%")
    print("\n=================================\n")

# check if there's python program running
if __name__ == "__main__":
    start_the_love()