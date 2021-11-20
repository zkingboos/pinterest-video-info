# PVI
PVI (Pinterest Video Info) is an inspired project to get the CDN (Content Delivery Network) of videos using [youtube-dl](https://youtube-dl.org/) to resolve page info.

## Contents

* [Usage](#usage)
* [Contributing](#contributing)


### Usage

First clone this repository locally using git-cli.

```cmd
$ git clone https://github.com/zkingboos/pinterest-video-info
$ cd pinterest-video-info
$ DISCORD_TOKEN=xxx.xxx.xxx python3 __init__.py
```

Or run using docker
```cmd
$ docker run -e DISCORD_TOKEN=xxxx.xxxx.xxxx --name pvi zkingboos/pinterestvideoinfo
```

Example from docker-compose
```yml
version: '3.8'

services:
  pinterestvideoinfo:
    container_name: pvi
    restart: always # Restart if container crash or something else
    image: zkingboos/pinterestvideoinfo
    environment:
      - DISCORD_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxx.xxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.