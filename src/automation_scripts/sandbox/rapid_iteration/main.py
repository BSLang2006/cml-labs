crate = [
    {"artist": "Miles Davis", "title": "Kind of Blue", "year": 1959, "plays": 12},
    {"artist": "Portishead", "title": "Dummy", "year": 1994, "plays": 3},
    {"artist": "Bill Evans", "title": "Sunday at the Village Vanguard", "year": 1961, "plays": 7},
    {"artist": "Radiohead", "title": "In Rainbows", "year": 2007, "plays": 21},
]

new = 0

for r in crate:
    if r["year"] > 1990:
        print("title:", r["title"])

for r in crate:
    if r["plays"] < 10:
        print("artist:", r["artist"])

for r in crate:
    if r["artist"] == "Portishead":
        print("title:", r["title"])

for r in crate:
    if r["plays"] > 5:
        print("plays:", r["plays"])

for r in crate:
    if r["year"] < 1965 and r["year"] > 1955:
        print("title:", r["title"])

heavy = []
for r in crate:
    if r["plays"] > 10:
        heavy.append(r["title"])

print("more than 10 plays:", heavy)        

winning_title = ""
winning_amt = 0

for r in crate:
    if r["plays"] > winning_amt:
        winning_amt = r["plays"]
        winning_title = r["title"]
print("And the winner goes to:", winning_title)
