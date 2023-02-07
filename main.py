import os
import requests
from time import sleep
from random import shuffle
from datetime import datetime
from sys import argv, platform


class main:
    # methode
    def main_path() -> str:
        """set the path pfp_list directory"""
        if len(argv) > 1:
            if argv[1] == '--path1':  # optional path1
                return ''
            elif argv[1] == '--path2':  # optional path1
                return ''
            elif argv[1] == '--path3':  # optional path1
                return ''
        else:
            return ''  # main path <--- required

    def map_range(x, in_min, in_max, out_min, out_max) -> float:
        """relative scaling function"""
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

    def long_sleep(sleep_time) -> None:
        """advanced sleep function with progress bar"""

        print('░'*50, end='\r')
        for i in range(sleep_time):
            compl = int(main.map_range(i+1, 0, sleep_time, 1, 50))
            percent = main.map_range(i+1, 0, sleep_time, 0, 100)
            print(('█'*compl)+('░'*(50-compl))+(str(percent)+'%') +
                  (' time left:'+str(sleep_time-i)+'s')+(' '*10), end="\r")
            sleep(1)
        print('')
        if platform == 'Windows':
            os.system('cls')
        elif platform == 'linux':
            os.system('clear')

    def write_to_log(data) -> None:
        """function to write the data into the log file"""
        print("wrinting to log")
        with open(main.main_path()+"/log.log", "a") as f:
            data = str(data)
            now = datetime.now().strftime("%D at %H:%M:%S")
            f.write(str(now)+'-->'+data+"\n"+"\n")

    def get_all_image(dir_path) -> list:
        """function to get all image of the given directory"""
        image_list = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(".jpg") or file.endswith(".png"):
                    image_list.append(os.path.join(root, file))
        if len(image_list) == 0:
            print('\033[1;31;48m'+'no image found !'+'\033[1;37;0m')
            raise Exception('no image found in this directory, check the path')
        else:
            return image_list

    class upload_image():
        def data(path_pic) -> str:
            """resquest data"""
            p_pic_s = os.path.getsize(path_pic)
            headers = {
                "Host": "www.instagram.com",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
                "Accept": "*/*",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                # your instagram account page (exe:https://www.instagram.com/garfield/)
                "Referer": "YOUR_INTAGRAM_ACCOUT_PAGE",
                # your X-CSRFToken
                "X-CSRFToken": "YOUR_X-CSRFToken",
                # your X-Instagram-AJAX
                "X-Instagram-AJAX": "YOUR_X-Instagram-AJAX",
                "X-Requested-With": "XMLHttpRequest",
                "Content-Length": str(p_pic_s),
                "DNT": "1",
                "Connection": "keep-alive",
                "Cookie": 'YOUR_Cookie🍪'
            }

            url = "https://www.instagram.com/accounts/web_change_profile_picture/"

            files = {'profile_pic': open(path_pic, 'rb')}
            values = {"Content-Disposition": "form-data", "name": "profile_pic", "filename": "profilepic.jpg",
                      "Content-Type": "image/jpeg"}
            return path_pic, headers, url, files, values

        def upload(image) -> bool:
            """send the request"""
            path_pic, headers, url, files, values = main.upload_image.data(
                image)
            try:
                r = requests.post(url, files=files,
                                  data=values, headers=headers)
                main.write_to_log(r.text)
                main.write_to_log(str('image applied :' + str(path_pic)))
                return True
            except Exception as error:
                print('\033[1;31;48m'+'error !'+'\033[1;37;0m')
                main.write_to_log(error)
                return False

    def cond(debug, condition, image) -> bool:
        # condition to send the request with debug feature
        if condition:
            if debug:
                print("time condition passed")

            print('trying to change')
            # make the request and put the result in r
            r = main.upload_image.upload(image)

            if r == False:  # if the request failed :
                return False
            else:
                print('image applied: '+str(image))
                # if the request is successful then stop the loop and restart with a new image
                self_run = False
                # wait an 1 hour before looping (to avoid multiple pfp changement in the same hour)
                main.long_sleep(3600)
        else:
            # if it's not 10am then sleep 5min
            main.long_sleep(300)

    def run(debug, self_run, image) -> bool:
        # main loop function
        while self_run:
            now = datetime.now()

            if debug:
                # if debug mode the request is send instantly
                condition = True
            else:
                # if not, change the condition to (now.hour == 10)[if it's 10am] (24h format)
                condition = now.hour == 10
            if main.cond(debug, condition, image):
                return True

    def image_select(debug) -> None:
        # select all the images of the set directory and shuffle them, then call the main loop

        all_images = main.get_all_image(main.main_path()+"/pfp_list")
        shuffle(all_images)
        for image in all_images:
            self_run = True
            r = main.run(debug, self_run, image)

    def change_pfp(debug=False) -> None:
        """change your instagram profile picture every x time(main function)"""
        if debug:
            print("starting in debug mode")
        else:
            print("starting program")
        while True:
            main.image_select(debug)


if __name__ == "__main__":
    debug_keyword = ['--debug', '--path1',
                     '--path2', '--path3']
    if len(argv) > 1:
        if argv[1] in debug_keyword:
            main.change_pfp(debug=True)
    else:
        main.change_pfp(debug=False)
