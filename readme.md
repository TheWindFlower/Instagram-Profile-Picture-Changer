# Instagram profile picture changer

## _a little script is written in python to automatically change your Instagram profile picture_

## Requirements :

- Python 3.9 (not tested on older version but a least python 3.7)
- [request library](https://docs.python-requests.org/en/latest/) to make the request
- your [X-CSRFToken, X-Instagram-AJAX and instagram cookie]

### Install all requirements :

```
pip3 install request
```

## What does this script do ?

## Usage guide :

- Install all dependencies
- Start qBitrorrent Web UI if it wasn't already
- Download the file `CanalBot.py` into a direcroty
- Create a file named `proceed_list.txt`, it will store the name of which files have already been encoded
- Create another file named `anime_list.txt`, and enter **ONE** keyword (seperated by a return line) for each animes you want the script to take (you can add as many keywords as you want, as long as there is one keyword per anime)
  - _It should look like this :_
    ```
    keyword1
    keyword2
    keyword3
    ```
- Now edit CanalBot.py and modify the first variables to match your settings :

  - `lang` is used to choose the language of subtitles that will be burned in the video (you can choose to not burn the subtitles, see Customisation)
  - `suffix` define the end of the file. Episode name will be in this format : {anime_name}.s1e{episode_number}.{suffix}.mp4, for French subtitles you could put "vostfr" for instance.
  - `target_directory` tells the script where does the animes go
  - `torrents_location` define on which directory torrents are downloaded
  - `linuxuser` specify which linux user shoud own the files
  - `user` is the user of the qBittorrent Web UI
  - `password` is the password of the qBittorrent Web UI
  - `qb` set the link to the qBittorrent Web UI

- If you've done everything, you can start the script and it will ask you if you want to delete torrents afterwards and start his job.
- If the script crashes, just restart it, it won't re-add episodes, or re-encode episode.

## Customisation

- You can custom the encoding command if you want, _see [HandBrakeCLI Documentation](https://handbrake.fr/docs/en/latest/cli/cli-options.html)_
- You can stop the script at any moment py pressing <kbd>CTRL</kbd> + <kbd>C</kbd>, otherwise it will run infinitely
