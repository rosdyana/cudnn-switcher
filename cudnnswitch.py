import argparse
import glob
import subprocess
import webbrowser
import os


def switchCudnn(version, cudadir):
    packages = glob.glob("packages/*{}.tgz".format(version))
    lenfiles = len(packages)
    if lenfiles:
        print("Switching cudnn version {}".format(version))
        subprocess.call(['mkdir', 'packages/cudnn'])
        subprocess.call(['tar', 'xf', packages[0],
                         '-C', 'packages/cudnn', '--strip-components', '1'])
        subprocess.call(['rm -rf', '{}/include/cudnn.h'.format(cudadir)])
        subprocess.call(['rm -rf', '{}/lib64/*libcudnn*'.format(cudadir)])
        subprocess.call(
            ['cp -P', 'packages/cudnn/include/cudnn.h {}/include'.format(cudadir)])
        subprocess.call(
            ['cp -P', 'packages/cudnn/lib64/libcudnn* {}/lib64'.format(cudadir)])
        subprocess.call(
            ['chmod a+r', '{}/lib64/libcudnn*'.format(cudadir))
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
    parser.add_argument('-c', '--cudadir',
                        help='set cuda dir path', required=True)

    args = parser.parse_args()
    switchCudnn(args.version, args.cudadir)


if __name__ == '__main__':
    main()
