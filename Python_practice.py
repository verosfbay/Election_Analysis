print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

counties_tuples = ("Arapahoe","Denver","Jefferson")
for i in range(len(counties_tuples)):
    print(counties_tuples[i])

counties_tuples = ("Arapahoe","Denver","Jefferson")
for county in counties_tuples:
      print(county)
    
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438} 
for county in counties_dict:
    print(county)

counties_dict.keys = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438} 
for county in counties_dict.keys():
    print(county)

#Getting values of keys
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

#Getting the key-value pairs
for county, voters in counties_dict.items():
    print(county, voters)

#Skill Drill 
for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters")

#Get Each Dictionary in a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):

      print(voting_data[i]['county'])

#Get the Values from a List of Dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#Retrieve the number of registered voters from each dictionary 
for county_dict in voting_data:

     print(county_dict['registered_voters'])

#If we only want to print the county name from each dictionary
for county_dict in voting_data:
    print(county_dict['county'])

 #F-strings: Formatted String Literals
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#Skill Drill Edit
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#If we use f-stings
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {3345} number of votes. "
    f"The total number of votes in the election was {23123}. "
    f"You received {3345 / 23123 * 100}% of the total votes.")
print(message_to_candidate)

#Format Floating-Point Decimals
message_to_candidate = (
    f"You received {3345:,} number of votes. "
    f"The total number of votes in the election was {23123:,}. "
    f"You received {3345 / 23123 * 100:.2f}% of the total votes.")
print(message_to_candidate)

#Skill Drill
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

#Skill Drill
voting_data = [``{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
