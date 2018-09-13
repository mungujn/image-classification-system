import requests
import argparse

parser = argparse.ArgumentParser(description='System frontend')
parser.add_argument(
    "--classes",
    nargs="*",  # expects ≥ 0 arguments
    type=str,
    # default list if no arg value
    default=['cat', 'dog', 'horse', 'car', 'truck'],
)

job = None


def startDownloadJob():
    r = requests.post('http://localhost:8081/download-job')
    job = r.json()
    print(f'Job {job} started')


def checkStatusOfDownloadJob():
    pass


def startClassificationJob():
    pass


def checkStatusOfClassificationJob():
    pass


def startUploadJob():
    pass


def checkStatusOfUploadJob():
    pass


if __name__ == '__main__':
    """Parses command line arguments and starts the classification process
    """
    args = parser.parse_args()
    classes = args.classes
    print('Classifying images of the following classes: ', classes)
    startDownloadJob()


