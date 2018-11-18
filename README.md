# Image categorizer. An image classification application

An app that categorizes images in a drop box folder. To help understand the app consider this scenario: You have 1000 photos in a drop box folder. The photos are of 5 types of items. You would like to generate 5 folders, each having all the photos of a particular item type.

## System overview

The system utilizes two services, the [image-classifier](https://github.com/mungujn/image-classifier) and the [downloader-uploader](https://github.com/mungujn/downloader-uploader) service .

The frontend described in this repo is a script that interacts with the two micro-services, serving to demonstrate usage of the system. It invokes the downloader-uploader first to dowload images from a dropbox folder called 'all'. It then invokes the image-classifier service to classify these images and move them to individual folders. Finally the frontend invokes the downloader-uploader service again to upload the classified images back up to seperate folders in dropbox.

The [image-classifier](https://github.com/mungujn/image-classifier) and [downloader-uploader](https://github.com/mungujn/downloader-uploader) repos each have a READMEs that explain their design and functionality in more detail.

## Running the system

1. Generate a dropbox access token and set it as an environment variable called ACCESS_TOKEN
2. Define a SERVICE_KEY environment varible which serves as an extra layer of security
3. Create a folder in dropbox called 'All'
4. Place the images that you want to classify in that folder
5. Install the requirements defined in each services' requirements.txt file
6. Start the [downloader-uploader](https://github.com/mungujn/downloader-uploader) service
7. Start the [image-classifier](https://github.com/mungujn/image-classifier) service
8. Run main.py and pass in the classes you want to sort your uploaded images by
   e.g 'python main.py --classes cat dog truck' will sort for cats, dogs and trucks
9. The system will start the classification and update you on its progress along the way

![System output](https://raw.githubusercontent.com/mungujn/image-classification-system/master/output.jpg 'System output')

## Testing

Refer to the individual service repos. I have included each services' build status below;

### Classifier service

[![Build Status](https://travis-ci.com/mungujn/image-classifier.svg?branch=master)](https://travis-ci.com/mungujn/image-classifier)
[![codecov](https://codecov.io/gh/mungujn/image-classifier/branch/master/graph/badge.svg)](https://codecov.io/gh/mungujn/image-classifier)

### Downloader, uploader service

[![Build Status](https://travis-ci.com/mungujn/downloader-uploader.svg?branch=master)](https://travis-ci.com/mungujn/downloader-uploader)
[![codecov](https://codecov.io/gh/mungujn/downloader-uploader/branch/master/graph/badge.svg)](https://codecov.io/gh/mungujn/downloader-uploader)
