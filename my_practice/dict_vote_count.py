def vote_count(votes):
    count = {}
    for vote in votes:
        count[vote] = count.get(vote, 0) + 1
    return count

votes = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob","Alice"]
print(vote_count(votes))