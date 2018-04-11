import argparse
import glob
import subprocess
import webbrowser
import os


def runprocess(command):
    try:
        subprocess.call(command, shell=True)
    except Exception as e:
        print(e)


def switchCudnn(version, cudadir):
    packages = glob.glob("packages/*{}.tgz".format(version))
    lenfiles = len(packages)
    if lenfiles:
        print("Switching cudnn version {}".format(version))
        runprocess('mkdir packages/cudnn')
        runprocess(
            'tar xf {} -C packages/cudnn --strip-components 1'.format(packages[0]))
        runprocess('sudo rm -rf {}/include/cudnn.h'.format(cudadir))
        runprocess('sudo rm -rf {}/lib64/*libcudnn*'.format(cudadir))
        runprocess(
            'sudo cp -P packages/cudnn/include/cudnn.h {}/include'.format(cudadir))
        runprocess(
            'sudo cp -P packages/cudnn/lib64/libcudnn* {}/lib64'.format(cudadir))
        runprocess(
            'sudo chmod a+r {}/include/cudnn.h {}/lib64/libcudnn*'.format(cudadir, cudadir))
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
