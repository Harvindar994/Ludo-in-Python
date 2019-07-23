import pymongo

connection = pymongo.MongoClient('localhost',27017)

database = connection['mydb_01']

collection = database['students']

def print_colleciton_names_of_database():
    global database
    print(database.list_collection_names())

def add_record():
    data = {}
    while True:
        key = input("Enter The key : ")
        value = input("Enter the Value : ")
        print("")
        if key != 'next' and (len(key) == 0 or len(value) == 0):
            return data
        if key == 'next' or value == 'next':
            print(collection.insert_one(data))
            print("")
            data = {}
        else:
            data[key] = value

def find_data():
    global collection
    data = []
    while True:
        key = input("Enter The key : ")
        value = input("Enter the Value : ")
        print("")
        if key == 'all':
            data = collection.find()
            for e in data:
                print("-------------------------------------------------\n")
                for key in e:
                    print('%s : %s'%(key,e[key]))
            return
        if len(key) == 0 or len(value) == 0:
            return data
        data = collection.find_one({key:value})
        if data != None:
            for key in data:
                print(key, ' : ', data[key])
        else:
            print("Data Not Find\n")
        print("")

def update_data(key, value, key_value = {}):
    global collection
    global database
    collection.update_many({key:value}, {'$set':key_value})

choice = 0

while True:
    print("0. Exit")
    print("1. Add A New Record In Data Base")
    print("2. Find Data")
    print("3. Switch Data Collection")
    print("4. Switch Data Base")
    print("5. Print Collection Names")
    print("6. Update data")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        add_record()
    elif choice == 0:
        exit(0)
    elif choice == 2:
        find_data()
    elif choice == 3:
        name = input("Enter Your Collection Name : ")
        collection = database[name]
    elif choice == 4:
        data_base = input("Enter Your Data Base Name : ")
        collection_name = input("Enter Your Data collection Name : ")
        database = connection[data_base]
        collection = database[collection_name]
        print("Your Data Base Changed")
    elif choice == 5:
        print_colleciton_names_of_database()
    elif choice == 6:
        s_key = input("Enter Selected Document Key : ")
        s_value = input("Enter Selected Document Value : ")
        update_dict = {}
        while True:
            key = input("Enter The Key : ")
            value = input("Enter The Value : ")
            if len(key) == 0 or len(value) == 0:
                break
            update_dict[key] = value
        if len(s_value) != 0 and len(s_key) != 0 and len(update_dict) != 0:
            update_data(s_key, s_value, update_dict)

