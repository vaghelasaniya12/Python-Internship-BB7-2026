library = {
    101:{"title":"Python Basics", "author":"John", "copies":5},
    102:{"title":"Java Programming", "author": "David", "copies":3},
    103:{"title":"Web Develeopment", "author":"Sarah", "copies":4}
}

book_id = 101

library[book_id]["copies"] -= 1

print("Updated Library:")
print(library)
