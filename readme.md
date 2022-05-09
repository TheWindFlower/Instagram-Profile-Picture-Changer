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

the script will change your instagram profile picture every x time, by using your cookie

## Usage guide :

- Install all dependencies
- clone or download the repo
- create a pfp_list directory
- put your profiles pictures in the pfp_list directory
- add your [X-CSRFToken, X-Instagram-AJAX and instagram cookie](https://github.com/TheWindFlower/instagram_profile_picture_changer#get-x-csrftoken-x-instagram-ajax-and-instagram-cookie) in the script
- [set your delay and the path](https://github.com/TheWindFlower/instagram_profile_picture_changer#Customisation)
- run the code and have fun

### Customisation

- set your delay between change in second line 10, or an hour to change the pfp line 11
  ![alt text](https://cdn.discordapp.com/attachments/849279007626625024/973085626738040892/Screenshot_from_2022-05-09_06-53-56.png)
- set the path of your python file line 9(the directory should containe the python file, a directory named pfp_list and a log.log file)

### get X-CSRFToken, X-Instagram-AJAX and instagram cookie

- to get your X-X-CSRFToken, X-Instagram-AJAX and instagram cookie you'll need to go to your [accout edit page](https://www.instagram.com/accounts/edit/)
- open the Web DEveloper Tools and go the the Network tab
  ![alt text](https://cdn.discordapp.com/attachments/849279007626625024/969274423481868329/unknown.png)
- click on one of the request
  ![alt text](https://media.discordapp.net/attachments/849279007626625024/969275638802423888/unknown.png)
- then scroll all the way down on the request tab and you have all the stuff you need
  ![alt text](https://media.discordapp.net/attachments/849279007626625024/969277032829714482/unknown.png)
- _if one of them is missing try another request_
- now you just need to put them in the script :
  ![alt text](https://media.discordapp.net/attachments/849279007626625024/969279156275798066/unknown.png)
