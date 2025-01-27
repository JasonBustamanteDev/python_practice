head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}

print(head["next"]["value"]) 
print(head.next.value) # doesn't work now, but it will work once we implement a linked list properly using classes