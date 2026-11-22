#Student Member Directory
from pyscript import display, document

grade7 = {"Alex Band", "Chito Miranda"}
grade8 = {"Chris Daughtry", "James Blunt", "Allison Burgers", "Employs Muswashans", "Max Imumoccupancy120" }
grade9 = {"Zayn Malik", "Harry Styles", "Liam Payne", "Louis Tomlinson", "Niall Horan"}
grade10 = {"Carlos Agassi", "Jhong Hilario", "Malupiton", "Pareng G"}
new_members = set()

def add_member(e):
    first = document.getElementById('first_name').value
    last = document.getElementById('last_name').value
    full_name = f"{first} {last}"

    new_members.add(full_name)

    all_members = grade7 | grade8 | grade9 | grade10 | new_members

    display(f"All Members: {all_members}", target='members_list')
    display(f"The total number of members are: {len(all_members)}", target='total_count')