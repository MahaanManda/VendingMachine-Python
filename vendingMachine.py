# You are at a vending machine. If you are hungry and want something salty or you are thirsty, get a drink. If you are hungry and want something sweet, get a chocolate bar
import sys

# Welcome message
print("Welcome to the Vending Machine")

# Prompts
user_hungry = str(input('Are you HUNGRY?: ')).lower()
user_thirsty = str(input('Are you THIRSTY?: ')).lower()


#for both
if user_thirsty == 'yes' and user_hungry == 'yes':
   print('Get a drink')
   #for hungry
   user_salty= str(input('Do you want something SALTY?: ')).lower()
   user_sweet = str(input('Do you want something SWEET: ')).lower()

   #if sweet/salty
   if user_salty == 'yes' and user_sweet == 'yes':
       print('Get some chips')
       print('Get a chocolate bar')
   elif user_salty == 'yes':
       print('Get some chips')
   elif user_sweet == 'yes':
       print("Get a chocolate bar")
   elif user_sweet == 'no' and user_salty == 'no':
       print('Come back when your hungry... :)')








#if hungry
elif user_hungry == 'yes':
   user_salty= str(input('Do you want something SALTY?: ')).lower()
   user_sweet = str(input('Do you want something SWEET: ')).lower()
   #if sweet/salty
   if user_salty == 'yes' and user_sweet == 'yes':
       print('Get some chips')
       print('Get a chocolate bar')
   elif user_salty == 'yes':
       print('Get some chips')
   elif user_sweet == 'yes':
       print("Get a chocolate bar")
   elif user_sweet == 'no' and user_salty == 'no':
       print('Come back when your hungry... :)')






#if thirsty
elif user_thirsty == 'yes':
   print('Get a drink')


#if none
elif user_hungry == 'no' and user_thirsty == 'no':
    print('Come back when your hungry or thirsty... :)')