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

It may require some time to start the application, please open the link and wait a little before sending requests to the endpoints.


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

Clone the postman page and execute the requests!

Or test the Endpoints yourself with your favorite tool.

# Endpoints

All requests needs to be of application/json type

## /vowel_count

+ Request (application/json)
+ Method [POST]

    + Body
```    
        {
            "words": [array of strings],
        }
```        

## /sort


+ Request (application/json)
+ Method [POST]

    + Body
```    
        {
            "words": [array of strings],
            "order": "asc",
        }
```        
"order" supports two strings asc for alphabetical ordering or desc for reverse ordering.

# Pipeline
The pipeline is ilustrated in the CI.yml file.

It runs the following steps on push.

```mermaid
graph TD;
    Pylint-->Pytest;
    Pytest-->Azure_AppServices;

```

Pylint checks the written code for bad practices, errors and suspicious constructs.

Pytest runs the written tests for the endpoints and the core system.

Azure_AppServices upload the application to production at Azure.

## Author
Cézar Murilo (cezarmgt@gmail.com)

## License

GNU General Public License v3.0 or later.

See [LICENSE](LICENSE) for the full text.
