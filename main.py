import os
import requests
from time import sleep
from random import shuffle
from datetime import datetime
from sys import argv


class main:
    # the path of the directory containing this python file
    main_path = ''
    # your delay (not used if you set a hour_to_change)
    delay = None
    # your hour to change (not used if you set a delay)
    hour_to_change = None

    # methode
    def long_sleep(sleep_time) -> None:
        """advanced sleep function with progress bar"""
        local_sleep_time = sleep_time/50
        print('░'*50, end='\r')
        for i in range(50):
            print('█'*(i+1)+'░'*(50-i)+(str(i*2))+'% '+'sleeping left:' +
                  str(round((sleep_time-(local_sleep_time*i)), 2))+'s', end='\r')
            sleep(local_sleep_time)

    def write_to_log(data) -> None:
        """function to write the data into the log file"""
        print("wrinting to log")
        with open(main.main_path+"/log.log", "a") as f:
            data = str(data)
            now = datetime.now().strftime("%D at %H:%M:%S")
            f.write(str(now)+'-->'+data+"\n"+"\n")

    def get_all_image(dir_path) -> list:
        """function to get all image in a directory"""
        image_list = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(".jpg") or file.endswith(".png"):
                    image_list.append(os.path.join(root, file))
        return image_list

    def upload_image(path_pic) -> bool:
        p_pic_s = os.path.getsize(path_pic)
        headers = {
            "Host": "www.instagram.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            # your instagram account page (exe:https://www.instagram.com/garfield/)
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "YOUR_INTAGRAM_ACCOUT_PAGE",
            # your X-CSRFToken
            "X-CSRFToken": "YOUR_X-CSRFToken",
            # your X-Instagram-AJAX
            "X-Instagram-AJAX": "YOUR_X-Instagram-AJAX",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Length": str(p_pic_s),  # should also work without this
            "DNT": "1",
            "Connection": "keep-alive",
            # your cookie
            "Cookie": 'YOUR_Cookie'
        }

        url = "https://www.instagram.com/accounts/web_change_profile_picture/"

        files = {'profile_pic': open(path_pic, 'rb')}
        values = {"Content-Disposition": "form-data", "name": "profile_pic", "filename": "profilepic.jpg",
                  "Content-Type": "image/jpeg"}
        try:
            r = requests.post(url, files=files, data=values, headers=headers)
            main.write_to_log(r.text)
            return True

        except Exception as error:
            print('\033[1;31;48m'+'error !, '+'\033[1;37;0m')
            main.write_to_log(error)
            return False

    def change_pfp() -> None:
        """change your instagram profile picture every x time or at an specified hour"""
        print("starting program")

        while True:
            all_images = main.get_all_image(main.main_path+"/pfp_list")
            shuffle(all_images)

            for image in all_images:
                self_run = True
                trying = 0
                while self_run:
                    now = datetime.now()

                    condition = now.hour == main.hour_to_change

                    if condition:
                        print('trying to change')
                        # make the request and put the result in r
                        r = main.upload_image(image)
                        if r == False:  # if the request failed :
                            trying += 1

                            if trying >= 5:  # if 5 try have failed:
                                print('5 failed try stopping program')
                                main.write_to_log(
                                    "5 failed attemps to make a request, stopping program")
                            else:
                                print('request failed, retry in 5min')
                                sleep(300)
                        else:
                            print('image applied: '+str(image))
                            # if the request is successful then stop the loop and restart with a new image
                            self_run = False
                            # wait an 1 hour before looping (to avoid multiple pfp changement in the same hour)
                            main.long_sleep(3600)
                    else:
                        sleep(300)  # if it's not 10am then sleep 5min and loop


if __name__ == "__main__":
    main.change_pfp()
