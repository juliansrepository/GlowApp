import main_functions
import requests
import os.path


def query(myQuery):
    #Deserializes api key that is in .json format
    myKey = main_functions.read_from_file("api_key.json")
    api_key = myKey['apikey']

    #The first header requests data in .json and the second passes the deserialized api key
    headers = {
    'Content-Type': 'application/json',
    'apikey': api_key
    }


    #Within the response lib you can pass headers and params as a dic. Can also be a tuple.
    params = {
    'q': '',
    'location': 'United States',
    'search_engine': 'google.com',
    'gl': 'US',
    'hl': 'en',
    'num': '10'
    }

    #Asks user for beauty product
    #productQ = input("What beauty product will you like to look for? : ")
    #print('Your product is', productQ)
    params['q'] = myQuery



    #This will use request lib to make a custom url request.
    #params will add "?" before first parameter "q".
    #Output will be handled by .json function so that we may save it using main_functions/
    response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params).json()




    #if statement will check to see if the file name has not been created.
    #If the file exists it will be named after the past index location of 'i'.
    i = 0
    if os.path.exists("results_json%s.json" % i):
        i += 1
        fileName = "results_json%s.json" % i
        main_functions.save_to_file(response, fileName)
    else:
        fileName = "results_json%s.json" % i
        main_functions.save_to_file(response, fileName)
        return fileName