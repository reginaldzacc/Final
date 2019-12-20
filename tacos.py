'''
Reginald Zaccardi-Richey
Random Taco Cook Book Generator
'''

'''
This block of code is for importing the mods 
needed to handle my URL and create/edit word 
documents.
'''
import requests  # Imports requests mod to recieve data from api as JSON
import docx  # Imports docx for creating and editing word documents

'''
This block of code is variables needed to run the program
'''
document = docx.Document()  # this variable creates my empty word document for future use.
url = 'https://taco-1150.herokuapp.com/random/?full_taco=true'  # this variable is the URL for the API used to get our JSON data

'''
This block of code is where the main() function is. 
This is where most of the code will be run.
this block of code will try to request JSON data 
using our URL, Pull the data from that request, and 
add a paragraph to word with the recipe. If there are 
errors the program will tell the user instead of crashing.
'''


def main(url):  # creates main() function
    try:  # this line 'trys' to run the following code
        data = requests.get(url).json()  # this line returns our API request as the variable 'data'
        seasoning = (data["seasoning"]["recipe"])  # creates seasoning variable with information from our returned data
        condiment = (data["condiment"]["recipe"])  # creates condiment variable with information from our returned data
        mixin = (data["mixin"]["recipe"])  # creates mixin variable with information from our returned data
        base_layer = (
            data["base_layer"]["recipe"])  # creates base layer variable with information from our returned data
        document.add_paragraph(
            f'{seasoning}\n{condiment}\n{mixin}\n{base_layer}')  # this line prints our 4 variables onto our word document with a new line after each variable
    except ConnectionError:  # output if Connection Error
        print('Connection Error')  # what user sees if Connection Error
    except TimeoutError:  # output if Timeout error
        print('Timeout Error')  # what user sees if timeout Error
    except:  # broad error output
        print('Error')  # what user sees if Broad, missed Error


'''
this block of code will try to get input from 
user for amount of recipes they would like generated.
'''
while True:
    try:  # 'trys' to run following code
        recipes = int(
            input(
                'How many recipes would you like in your Random cookbook?\nPlease enter a whole number in numeric form: '))# this line asks user for a whole number of recipes they would like
        break  # breaks loop
    except ValueError:  # error exception if wrong input data type
        print('Wrong Data Type. Try again')  # error output to user


'''
This block is meant to generate the tacobook using main looped as many times as the user wanted. 
'''
print('Generating TacoBook')#lets user know the tacobook is being generated

for number in range(recipes):#for loop to create recipes
    main(url)#runs our main function
document.save('TacoBook.docx')#saves the document under file name "TacoBook.docx
print('Your Random Taco Cookbook has been created with the file name \'TacoBook.docx\'')#notifys user the tacobook is complete and the file name
