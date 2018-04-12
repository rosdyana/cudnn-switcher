# cuDNN Switcher
a simple cli tools based on python to switch cudnn version on your linux machine

## Current cuDNN available version
| Version | CUDA  | Package                             |
| :-----: | :---: | :---------------------------------: |
| 7.1     | 9.1   | cudnn-9.1-linux-x64-v7.1.tgz        |
| 7.1     | 9.0   | cudnn-9.0-linux-x64-v7.1.tgz        |
| 7.1     | 8.0   | cudnn-8.0-linux-x64-v7.1.tgz        |
| 7.0     | 9.1   | cudnn-9.1-linux-x64-v7.tgz          |
| 7.0     | 9.0   | cudnn-9.0-linux-x64-v7.tgz          |
| 7.0     | 8.0   | cudnn-8.0-linux-x64-v7.tgz          |
| 6.0     | 8.0   | cudnn-8.0-linux-x64-v6.0.tgz        |
| 6.0     | 7.5   | cudnn-7.5-linux-x64-v6.0.tgz        |
| 5.1     | 8.0   | cudnn-8.0-linux-x64-v5.1.tgz        |
| 5.1     | 7.5   | cudnn-7.5-linux-x64-v5.1.tgz        |
| 5.0     | 8.0   | cudnn-8.0-linux-x64-v5.0-ga.tgz     |
| 5.0     | 7.5   | cudnn-7.5-linux-x64-v5.0-ga.tgz     |
| 4.0     | 7.0   | cudnn-7.0-linux-x64-v4.0-prod.tgz   |
| 3.0     | 7.0   | cudnn-7.0-linux-x64-v3.0.8-prod.tgz |
| 2.0     | 6.5   | cudnn-6.5-linux-x64-v2.tgz          |
| 1.0     | 6.5   | cudnn-6.5-linux-R1.tgz              |

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

