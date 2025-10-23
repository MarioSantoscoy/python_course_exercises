import json


def age_average():
    with open('ages.json','r') as file:
        data = json.load(file)
        ages = []

        for user in data['user_info']:
            age = user['age']
            ages.append(age)

        average = sum(ages)/len(ages)

    return average





if __name__ == '__main__':
    print(age_average())