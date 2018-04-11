import argparse
import glob
import subprocess
import webbrowser
import os


def switchCudnn(version,):
    packages = glob.glob("packages/*{}.tgz".format(version))
    lenfiles = len(packages)
    if lenfiles:
        print("Switching cudnn version {}".format(version))
        subprocess.call(['mkdir', 'packages/cudnn'])
        subprocess.call(['tar', 'xf', packages[0],
                         '-C', 'packages/cudnn', '--strip-components', '1'])
        subprocess.call(['sudo rm -rf', '/usr/include/cudnn.h'])
        subprocess.call(
            ['rm -rf', '/usr/lib/x86_64-linux-gnu/*libcudnn*'])
        subprocess.call(['rm -rf', '/usr/local/cuda-*/lib64/*libcudnn*'])
        subprocess.call(
            ['cp -P', 'packages/cudnn/include/cudnn.h /usr/include'])
        subprocess.call(
            ['cp -P', 'packages/cudnn/lib64/libcudnn* /usr/lib/x86_64-linux-gnu/'])
        subprocess.call(
            ['chmod a+r', '/usr/lib/x86_64-linux-gnu/libcudnn*'])
        subprocess.call(['rm -rf', 'packages/cudnn'])
        print("Sucessfully switched to version {}".format(version))
    else:
        print("Please download cudnn first")
        webbrowser.open_new_tab(
            "https://developer.nvidia.com/rdp/cudnn-archive")


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--version',
                        help='select cudnn version ( 4.0, 5.1, 6.0', required=True)
    args = parser.parse_args()
    switchCudnn(args.version)


if __name__ == '__main__':
    main()
