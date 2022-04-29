import os
import requests
from time import sleep, time
from random import shuffle

main_path = '/pfp_list'
delay = 3600  # <----


def write_to_log(data):
    """function to write the data into the log file"""
    with open(main_path+"/log.log", "a") as f:
        f.write(str(time())+':'+data+"\n")


def get_all_image(dir_path) -> list:
    """function to get all image in a directory"""
    image_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                image_list.append(os.path.join(root, file))
    return image_list


def upload_image(path_pic):
    """request to upload an image to instagram profile picture"""
    p_pic_s = os.path.getsize(path_pic)
    headers = {
        "Host": "www.instagram.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "YOUR_INTAGRAM_ACCOUT_PAGE", # <---- your instagram account page (exe:https://www.instagram.com/garfield/)
        "X-CSRFToken": "YOUR_X-CSRFToken",  # <---- your X-CSRFToken
        "X-Instagram-AJAX": "YOUR_X-Instagram-AJAX",  # <---- your X-Instagram-AJAX
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": str(p_pic_s),  # should also work without this
        "DNT": "1",
        "Connection": "keep-alive",
        "Cookie": 'YOUR_Cookie'  # <---- your cookie
    }

    url = "https://www.instagram.com/accounts/web_change_profile_picture/"

    files = {'profile_pic': open(path_pic, 'rb')}
    values = {"Content-Disposition": "form-data", "name": "profile_pic", "filename": "profilepic.jpg",
              "Content-Type": "image/jpeg"}

    r = requests.post(url, files=files, data=values, headers=headers)
    write_to_log(r.text)


def change_every_x_time(time):
    """change your instagram profile picture every x time"""
    while True:
        all_images = get_all_image(main_path+"/pfp_list")
        shuffle(all_images)
        for i in all_images:
            upload_image(i)
            sleep(time)


if __name__ == "__main__":
    change_every_x_time(delay)
