import fingerprint_enhancer
import argparse
import cv2
import os
from PIL import Image


def enhance_fingerprint(img_path, show=False):
    file_path = os.path.splitext(img_path)[0]
    file_name = file_path.split('/')[-1] + ".jpg"
    img = cv2.imread(img_path, 0)
    enhanced = fingerprint_enhancer.enhance_Fingerprint(img)

    if not os.path.isdir('./enhanced_prints'):
        os.mkdir('./enhanced_prints')

    path = './enhanced_prints'
    print(os.path.join(path, file_name))

    result = cv2.imwrite(os.path.join(path, file_name), enhanced)

    if result != True:
        print("Error when saving file '{}'.".format())

    print("Enhanced image written to: {}".format(os.path.join(path, file_name)))

    if show:
        show_enhanced_print(enhanced)


def enhance_fingerprints(dir_path):
    if not os.path.isdir(dir_path):
        print("Directory does not exist.")
        return
    
    for file in os.listdir(dir_path):
        enhance_fingerprint(file)


def show_enhanced_print(img_path):
    cv2.imshow('enhanced_image', img_path)
    cv2.waitKey(0)


def main():
    parser = argparse.ArgumentParser(description='Allow for command line generation of enhanced finger print images from photos.')

    parser.add_argument('-i','--img', action='store', type=str, help='Enhance a single image. Supply the image path.', required=False)
    parser.add_argument('-d','--dir', action='store', type=str, help='Enhance a whole directory of images. Supply the directory path.', required=False)
    args = parser.parse_args()

    if not args.img and not args.dir:
        print("Please provide a valid image or directory path.")
        return
    
    if args.img:
        enhance_fingerprint(args.img, show=True)
    
    if args.dir:
        enhance_fingerprints(args.dir)
    
    print("Fingerprints have been enhanced.")
    print("Enhanced images have been saved to ./enhanced_prints")
    

if __name__ == "__main__":
    main()
