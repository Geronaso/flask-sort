# flask-sort
Flask-sort is a simple API that counts the vowels of a string and sort array strings alphabetically.

## Features
* Counts the number of the vowels of a string
* Order a list of arrays alphabetically (it can be reversed)

## Requirements
Flask >= 2.2.2<br/>
Python >= 3.7<br/>
pytest >= 7.1.3

## Quickstart

Placeholder


## Endpoints

All requests needs to be of application/json type

# /vowel_count
objects:<br/>
    'words':*Array*  An array of strings

```python
json_data= { 
      'words' = ['array of strings'],
      }
```


# /sort
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
