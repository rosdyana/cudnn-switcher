import argparse
import glob
import subprocess
import os

# cuDNN package list from https://developer.nvidia.com/rdp/cudnn-download
cudadict = [{"ver": "7.1", "cudver": "9.1", "uri": "cudnn-9.1-linux-x64-v7.1.tgz"},
            {"ver": "7.1", "cudver": "9.0", "uri": "cudnn-9.0-linux-x64-v7.1.tgz"},
            {"ver": "7.1", "cudver": "8.0", "uri": "cudnn-8.0-linux-x64-v7.1.tgz"},
            {"ver": "7.0", "cudver": "9.1", "uri": "cudnn-9.1-linux-x64-v7.tgz"},
            {"ver": "7.0", "cudver": "9.0", "uri": "cudnn-9.0-linux-x64-v7.tgz"},
            {"ver": "7.0", "cudver": "8.0", "uri": "cudnn-8.0-linux-x64-v7.tgz"},
            {"ver": "6.0", "cudver": "8.0", "uri": "cudnn-8.0-linux-x64-v6.0.tgz"},
            {"ver": "6.0", "cudver": "7.5", "uri": "cudnn-7.5-linux-x64-v6.0.tgz"},
            {"ver": "5.1", "cudver": "8.0", "uri": "cudnn-8.0-linux-x64-v5.1.tgz"},
            {"ver": "5.1", "cudver": "7.5", "uri": "cudnn-7.5-linux-x64-v5.1.tgz"},
            {"ver": "5.0", "cudver": "8.0", "uri": "cudnn-8.0-linux-x64-v5.0-ga.tgz"},
            {"ver": "5.0", "cudver": "7.5", "uri": "cudnn-7.5-linux-x64-v5.0-ga.tgz"},
            {"ver": "4.0", "cudver": "7.0",
                "uri": "cudnn-7.0-linux-x64-v4.0-prod.tgz"},
            {"ver": "3.0", "cudver": "7.0",
                "uri": "cudnn-7.0-linux-x64-v3.0.8-prod.tgz"},
            {"ver": "2.0", "cudver": "6.5", "uri": "cudnn-6.5-linux-x64-v2.tgz"},
            {"ver": "1.0", "cudver": "6.5", "uri": "cudnn-6.5-linux-R1.tgz"}]


def runprocess(command):
    try:
        subprocess.call(command, shell=True)
    except Exception as e:
        print(e)


def versionSelector(version, cudaver):
    uri = ""
    for i, k in enumerate(cudadict):
        if cudadict[i]['ver'] == str(version) and cudadict[i]['cudver'] == str(cudaver):
            print(cudadict[i]['uri'])
            uri = cudadict[i]['uri']
    if uri != "":
        return uri


def switchCudnn(version, cudadir, cudaver):
    packagename = versionSelector(version, cudaver)
    if packagename != None:
        packages = glob.glob("packages/{}".format(packagename))
        lenfiles = len(packages)
        print("cudnn version {}".format(version))
        print("cuda dir path : {}".format(cudadir))
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
            runprocess('rm -rf packages/cudnn')
            print("Sucessfully switched to version {}".format(version))
        else:
            print(
                "Please download cudnn first here\nhttps://developer.nvidia.com/rdp/cudnn-download")
    else:
        print("Can not found suitable packages.\nCheck available cudnn package -> https://developer.nvidia.com/rdp/cudnn-download")


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--version',
                        help='select cudnn version ( 4.0, 5.1, 6.0', type=str, required=True)
    parser.add_argument('-d', '--cudadir',
                        help='set cuda dir path', required=True)
    parser.add_argument('-c', '--cudaver',
                        help='set cuda version of cudnn', type=str, required=True)

    args = parser.parse_args()
    switchCudnn(args.version, args.cudadir, args.cudaver)


if __name__ == '__main__':
    main()
