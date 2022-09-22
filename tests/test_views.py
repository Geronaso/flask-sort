"""Test file for the endpoints and methods"""

import pytest


# Parametrize some variables for tests
# key_words is the key value words, words is the list and
# response_message is the expected response from the server
@pytest.mark.parametrize('key_words,words,response_message', [
    ('words',["batman", "coringa", "robin"], b'{"batman":2,"coringa":3,"robin":2}\n'),
    ('words','', b'Bad Request'),
    ('wods',["batman", "coringa", "robin"], b'Bad Request'),
    ('words',["batman", "penguim", "coringa"], b'{"batman":2,"coringa":3,"penguim":3}\n'),
    ('words',[1, "penguim", "coringa"], b'Bad Request'),
])

# The test function that asserts the values are correct
def test_vowel_count(client, key_words, words, response_message):
    """test the vowel count endpoint and its inner logic"""
    response = client.post('/vowel_count', json = {key_words: words})
    assert response_message in response.data



# Parametrize some variables for tests
# key_words is the key value words, words is the list
# key_order is the key value order, order is the string
# and response_message is the rexpected response from the server
@pytest.mark.parametrize('words,order,response_message', [
    ({'words': ["batman", "robin", "coringa"]}, \
    {'order': 'asc'}, b'["batman","coringa","robin"]\n'),
    ({'words': ["batman", "robin", "coringa"]}, \
    {'order': 'desc'}, b'["robin","coringa","batman"]\n'),
    ({'words': ["batman", "robin", "coringa"]}, {'ordr': 'desc'}, b'Bad Request'),
    ({'words': ["batman", "robin", "coringa"]}, {'order': 'dc'}, b'Bad Request'),
    ({'wo': ["batman", "robin", "coringa"]}, \
    {'order': ''}, b'Bad Request'),
    ({'words': ["batman", "robin", "penguim"]}, \
    {'order': 'desc'}, b'["robin","penguim","batman"]\n'),
    ({'words': [1, "robin", "coringa"]}, {'order': 1}, b'Bad Request'),
    ({'words': ['bat', "robin", "coringa"]}, {'order': ''}, b'Bad Request'),
])

# The test function that asserts the values are correct
def test_sort(client, words, order, response_message):
    """test the sort endpoint and its inner logic"""
    response = client.post('/sort', json = (words | order))
    assert response_message in response.data
