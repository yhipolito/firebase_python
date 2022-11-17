import firebase_admin
from firebase_admin import credentials, db


cred = credentials.Certificate("helipads89-serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://helipads89-default-rtdb.firebaseio.com'
})

#create data
ref = db.reference('py/')
helipads_ref = ref.child('helipads')


def create_helipad():
    name = input("Enter helipad name: ")
    location = input("Enter helipad coordinates [example: 0475300N 115500E]: ")
    elevation = input("Enter helipad elevation in feet: ")
    name_str = f'{name}_helipad'
    helipads_ref_list = helipads_ref.child(name_str)
    helipads_ref_list.set({
        'name': name,
        'location': location,
        'elevation': elevation
    })
    

# Read data
def read_helipad():
    helipads_data = helipads_ref
    print(helipads_data.get())


def update_helipad():
    name = input("Enter helipad name: ")
    new_name = input("Enter new helipad name: ")
    location = input("Enter helipad coordinates [example: 0475300N 115500E]: ")
    elevation = input("Enter helipad elevation in feet: ")
    update_ref = helipads_ref.child(name)
    update_ref.update({
        'name': new_name,
        'location': location,
        'elevation': elevation
    })


# Delete data
def delete_helipad():
    name = input("Enter helipad name to delete: ")
    helipads_ref.child(name).delete()


def start_application():
    """Gets the inputs for helipads data"""

    print("\nWelcome to Helipads information")
    selection = ""

    while not selection == 'q':
        print("\nSelect an option: \n")
        print("Create a Helipad [c]: ")
        print("Read a Helipad [r]: ")
        print("update a Helipad [u]: ")
        print("Delete a Helipad [d]: ")
        selection = input("Enter your selection [q to quit]: ")
        
        if selection == 'c':
            create_helipad()
        
        elif selection == 'r':
            read_helipad()

        elif selection == 'u':
            update_helipad()

        elif selection == 'd':
            delete_helipad()

        else:
            return
        

start_application()


