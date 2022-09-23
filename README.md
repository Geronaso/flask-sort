# flask-sort
Flask-sort is a simple API that counts the vowels of a string and sort array strings alphabetically.

This API is meant only to be an ability assessment of my skills as a developer, it has no meaningful use or contribution.

## Features
* Counts the number of the vowels of a string
* Order an arrays alphabetically (it can be reversed)

## Requirements
Flask >= 2.2.2<br/>
Python >= 3.9<br/>
pytest >= 7.1.3

# Quickstart

The application can be accessed here: <br/>

https://flask-sort.azurewebsites.net/

It may require some time to start the application, please open the link and a wait a little before sending requests to the endpoints.

There is no index page, it only receives post messages at the specified endpoints.

OR

You can build it locally!

```
git clone https://github.com/Geronaso/flask-sort.git
cd flask sort
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
export API_KEY='DEV'
flask --app flask_sort --debug run
```

## Testing with POSTMAN

https://www.postman.com/foxmc/workspace/7089b35b-75bd-446f-ad12-95ac20daff93/overview

# Endpoints

All requests needs to be of application/json type

## /vowel_count
objects:<br/>
    'words':*Array*  An array of strings

```python
json_data= { 
      'words' = ['array of strings'],
      }
```


## /sort
objects:<br/>
    'words':*Array*  An array of strings.<br/>
    'order':*string* A string value of asc or desc fo reverse ordering the words.
    
```python
json_data= { 
      'words' = ['array of objects'],
      'order' = 'asc'
      }
```
      
## Author
Cézar Murilo (cezarmgt@gmail.com)

## License

GNU General Public License v3.0 or later.

See [LICENSE](LICENSE) for the full text.
