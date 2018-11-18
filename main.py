import requests
import os
import argparse
import time
from dotenv import load_dotenv
load_dotenv()
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
AUTHORIZATION = os.environ['SERVICE_KEY']

parser = argparse.ArgumentParser(description='System frontend')
parser.add_argument(
    "--classes",
    nargs="*",  # expects ≥ 0 arguments
    type=str,
    # default list if no classes are given
    default=['cat', 'dog', 'horse', 'car', 'truck'],
)

job = {}
percentage = 0
classes = []


def startJob(job_type):
    """Start a job of job_type

    Arguments:
        job_type {string} -- [type of job]
    """
    global job
    job = {}
    headers = {'Token': ACCESS_TOKEN, 'Authorization': AUTHORIZATION}

    if job_type == 'download':
        url = 'http://localhost:8081/download-job'
        r = requests.post(url, headers=headers)
        job = r.json()
    elif job_type == 'classification':
        url = 'http://localhost:8080/classification-job'
        r = requests.post(url, json={'classes': classes})
        job = r.json()
    elif job_type == 'upload':
        url = 'http://localhost:8081/upload-job'
        r = requests.post(url, json={'classes': classes}, headers=headers)
        jobs = r.json()

        if len(jobs) == 0:
            job = {'id': None, 'percentage': 100, 'complete': True}
        else:
            job = jobs[len(jobs) - 1]

    job_id = job['id']
    print(f'{job_type} job {job_id} has started on server')


def checkStatusOfJob(job_type):
    """Start a job of job_type

    Arguments:
        job_type {string} -- [type of job]
    """
    global job, percentage
    job_id = job['id']
    headers = {'Token': ACCESS_TOKEN, 'Authorization': AUTHORIZATION}

    if job_type == 'download':
        url = f'http://localhost:8081/download-job/{job_id}'
        r = requests.get(url, headers=headers)
        job = r.json()
    elif job_type == 'classification':
        url = f'http://localhost:8080/classification-job/{job_id}'
        r = requests.get(url, headers=headers)
        job = r.json()
    elif job_type == 'upload':
        url = f'http://localhost:8081/upload-job/{job_id}'
        r = requests.get(url, headers=headers)
        job = r.json()

    if job['percentage'] > percentage:
        percentage = job['percentage']
        print(
            f'{job_type} job {job_id} is {percentage} percent complete')


def download():
    """Download images"""
    print('*************************************')
    print(f'Download of images has started')
    startJob('download')
    while not job['complete']:
        checkStatusOfJob('download')
        # a better strategy here would be to calculate the estimated completion time and check then
        time.sleep(2)
    print(f'Download of images has completed')


def classify():
    """Classify downloaded images"""
    print('*************************************')
    print(f'Classification of {classes} has started')
    startJob('classification')
    while not job['complete']:
        checkStatusOfJob('classification')
        time.sleep(2)
    print(f'Classification of images has completed')


def upload():
    """Upload images"""
    print('*************************************')
    print(f'Upload of {classes} has started')
    startJob('upload')
    while not job['complete']:
        checkStatusOfJob('upload')
        time.sleep(2)
    print(f'Upload of images has completed')
    print('*************************************')


if __name__ == '__main__':
    """Parses command line arguments and starts the classification process
    """
    args = parser.parse_args()
    classes = args.classes
    retry = True

    while retry:
        try:
            download()

            classify()

            upload()
            retry = False
        except Exception as error:
            print('\nThe following error has occured \n')
            print('*************************************')
            print(error)
            print('*************************************')
            retry = input('Do you want to retry? yes or no: ')
            if retry == 'yes' or retry == 'y':
                retry = True
            else:
                retry = False
