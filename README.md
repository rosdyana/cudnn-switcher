# cuDNN Switcher
a simple cli tools based on python to switch cudnn version on your linux machine

## Usage
1. Download cudnn package first, and put it on packages folder ( no need to extract )

2. run this script to switch the cudnn version
```console
python cudnnswitch.py -v <cudnn version> -c <cuda version> -d <cuda directory path>
```
example :
```console
python cudnnswitch.py -v 6.0 -c 8.0 -d /usr/local/cuda-8.0
```

