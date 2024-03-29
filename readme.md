# Instagram profile picture changer

## _a little script written in python to automatically change your Instagram profile picture_

## Requirements :

- Python 3.9 (not tested on older version but a least python 3.7)
- [request library](https://docs.python-requests.org/en/latest/) to make the request
- your [X-CSRFToken, X-Instagram-AJAX and instagram cookie](https://github.com/TheWindFlower/instagram_profile_picture_changer#get-x-csrftoken-x-instagram-ajax-and-instagram-cookie)

### Install all requirements :

```
pip3 install request
```

## What does this script do ?

the script will change your instagram profile picture every x time, by using your instagram cookie

## Usage guide :

- Install all dependencies
- clone or download the repo
- create a pfp_list directory
- put your profiles pictures in the pfp_list directory
- add your [Referer, X-CSRFToken, X-Instagram-AJAX and instagram cookie] in the script (line 75, 77, 79, 84)
- [set your delay and the path](in the run function)
- [set your path](main_path function)
- run the code and have fun

### Customisation

- set your delay between change in the run function

### get X-CSRFToken, X-Instagram-AJAX and instagram cookie

- to get your X-X-CSRFToken, X-Instagram-AJAX and instagram cookie you'll need to go to your [accout edit page](https://www.instagram.com/accounts/edit/)
- open the Web DEveloper Tools and go the the Network tab
- click on one of the request
- then scroll all the way down on the request tab and you have all the stuff you need
- _if one of them is missing try refreshing the page and another request_
- now you just need to put them in the script:
