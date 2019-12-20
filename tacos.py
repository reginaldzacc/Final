'''
Reginald Zaccardi-Richey
Random Taco Cook Book Generator
'''


'''
'''
import requests
import docx


'''
'''
document = docx.Document()
url = 'https://taco-1150.herokuapp.com/random/?full_taco=true'


'''
'''
def main(url):
    try:
        data = requests.get(url).json()
        seasoning = (data["seasoning"]["recipe"])
        condiment = (data["condiment"]["recipe"])
        mixin = (data["mixin"]["recipe"])
        base_layer = (data["base_layer"]["recipe"])
        document.add_paragraph(f'{seasoning}\n{condiment}\n{mixin}\n{base_layer}')
    except ConnectionError:  # output if Connection Error
        print('Connection Error')
    except TimeoutError:  # output if Timeout error
        print('Timeout Error')
    except:  # broad error output
        print('Error')


'''
'''
while True:
    try:
        recipes = int(
            input('How many recipes would you like in your Random cookbook?\nPlease enter a whole number: '))
        break
    except ValueError:
        print('Try again')
print('Generating TacoBook')
for number in range(recipes):
    main(url)
document.save('TacoBook.docx')
print('Your Random Taco Cookbook has been created with the file name \'TacoBook.docx\'')
