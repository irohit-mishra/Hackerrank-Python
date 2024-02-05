if __name__ == "__main__":
    # Input the number of students subscribed to the English newspaper and their roll numbers
    n = int(input())
    english_subscribers = set(map(int, input().split()))

    # Input the number of students subscribed to the French newspaper and their roll numbers
    b = int(input())
    french_subscribers = set(map(int, input().split()))

    # Calculate the number of students subscribed to both newspapers
    common_subscribers = len(english_subscribers.intersection(french_subscribers))

    print(common_subscribers)
