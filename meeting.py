attendees = ["Ken", "Alena", "Treasure"]
# this add an item at the end of the list
attendees.append("Ashley")
# this modifies the specified list by extending n# of items
attendees.extend(["James", "Guil"])
optional_invitees = ["Ben", "Dave"]
# this way we create a new list where we concatenate 2 lists into 1
# without distortioning the original lists
potential_attendees = attendees + optional_invitees

print("There are", len(potential_attendees), "potential attendees currently")