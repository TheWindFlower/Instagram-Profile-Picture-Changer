import os
import requests
from time import sleep, time
from random import shuffle
from datetime import datetime


class main:
    main_path = '' # <---- your path to the directory of the python file
    delay = None # <---- your delay (not used if you set a hour_to_change)
    hour_to_change = None #<---- your hour to change (not used if you set a delay)

    def long_sleep(sleep_time):
        i=0
        while i<=sleep_time:
            local_sleep_time = sleep_time/10
            sleep(local_sleep_time)
            i+=local_sleep_time
            print("sleeping left:"+str(round((sleep_time-i+1), 2))+'s', end='\r')


    def write_to_log(self, data):
        print("wrinting to log")
        """function to write the data into the log file"""
        with open(self.main_path+"/log.log", "a") as f:
            data = str(data)
            f.write(str(time())+':'+data+"\n"+"\n")


    def get_all_image(dir_path) -> list:
        """function to get all image in a directory"""
        image_list = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(".jpg") or file.endswith(".png"):
                    image_list.append(os.path.join(root, file))
        return image_list


    def upload_image(self, path_pic) -> bool:
        p_pic_s = os.path.getsize(path_pic)
        headers = {
            "Host": "www.instagram.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "YOUR_INTAGRAM_ACCOUT_PAGE", #<---- your instagram account page (exe:https://www.instagram.com/garfield/)
            "X-CSRFToken": "YOUR_X-CSRFToken",  # <---- your X-CSRFToken
            "X-Instagram-AJAX": "YOUR_X-Instagram-AJAX",  # <---- your X-Instagram-AJAX
            "X-Requested-With": "XMLHttpRequest",
            "Content-Length": str(p_pic_s),  # should also work without this
            "DNT": "1",
            "Connection": "keep-alive",
            "Cookie":'YOUR_Cookie'  # <---- your cookie
        }

        url = "https://www.instagram.com/accounts/web_change_profile_picture/"

        files = {'profile_pic': open(path_pic, 'rb')}
        values = {"Content-Disposition": "form-data", "name": "profile_pic", "filename": "profilepic.jpg",
                "Content-Type": "image/jpeg"}
        try:
            r = requests.post(url, files=files, data=values, headers=headers)
            self.write_to_log(r.text)
            return True
        except Exception as error:
            print('\033[1;31;48m'+'error !'+'\033[1;37;0m')
            self.write_to_log(error)
            return False


    def change_pfp(self):
        """change your instagram profile picture every x time"""
        print("starting program")
        while True:
            all_images = self.get_all_image(self.main_path+"/pfp_list")
            shuffle(all_images)

            if self.hour_to_change != None:
                for image in all_images:
                    self_run = True
                    trying = 0
                    while self_run:
                        now = datetime.now()
                        
                        if now.hour == self.hour_to_change: #if it's the hour to change
                            print('trying to change')
                            r = self.upload_image(image) #make the request and put the result in r
                            if r==False: #if the request failed :
                                trying += 1
                                
                                if trying >= 5: #if 5 try have failed:
                                    print('5 failed try stopping program')
                                    self.write_to_log("5 failed attemps to make a request, stopping program")
                                else:
                                    print('request failed, retry in 5min')
                                    sleep(300)
                            else:
                                print('image applied: '+str(image))
                                self_run = False #if the request is successful then stop the loop and restart with a new image
                                self.long_sleep(3600) #wait an 1 hour before looping (to avoid multiple pfp changement in the same hour)
                        else:
                            sleep(300) #if it's not 10am then sleep 5min

            elif self.delay != None:
                for i in all_images:
                    if self.upload_image(i)==False:
                        sleep(10)
                    else:
                        sleep(self.delay)


if __name__ == "__main__":
    main.change_pfp(main)
