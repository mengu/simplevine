#### simplevine

A simple python package to extract vine posts' data.

#### usage


```python
from simplevine import vine

data = vine.dump("https://vine.co/v/hpHx7mhT9qX")
print data
```

```javascript
{
    'sender': {
        'name': u 'Trey Kennedy',
        'avatar': u '...',
    'title': u 'Miley Cyrus as a baby part II. #wreckingball',
    'tags': [u '#wreckingball'],
    'thumbnail': u '...',
    'id': 'hpHx7mhT9qX',
    'mp4_stream': u '...'
}
```
