from PIL import Image
import numpy as np
import os, glob
from keras.preprocessing.image import load_img,img_to_array
import cv2
import matplotlib.pyplot as plt

#画像フォルダへの絶対パス
ROOT_DIR = "images"
dir_name = "./data"

PETS = [
"Abyssinian",
"american_bulldog",
"american_pit_bull_terrier",
"basset_hound",
"beagle",
"Bengal",
"Birman",
"Bombay",
"boxer",
"British_Shorthair",
"chihuahua",
"Egyptian_Mau",
"english_cocker_spaniel",
"english_setter",
"german_shorthaired",
"great_pyrenees",
"havanese",
"japanese_chin",
"keeshond",
"leonberger",
"Maine_Coon",
"miniature_pinscher",
"newfoundland",
"Persian",
"pomeranian",
"pug",
"Ragdoll",
"Russian_Blue",
"saint_bernard",
"samoyed",
"scottish_terrier",
"shiba_inu",
"Siamese",
"Sphynx",
"staffordshire_bull_terrier",
"wheaten_terrier",
"yorkshire_terrier"]


#File type
file_type  = 'jpg'

img_list = glob.glob(r"./images/*.jpg")

#データ格納用
img_array_list = []
img_label_list = []

#教師用データ格納用
test_array_list = []
test_label_list = []

for img in img_list:
    for i in PETS:
        if(i in img):
            img_label_list.append(PETS.index(i))
            
    imgcv = plt.imread(img)
    # 画像の大きさを取得
    temp_img = load_img(img,grayscale=False,target_size=(imgcv.shape[0],imgcv.shape[1]))
    temp_img_array = img_to_array(temp_img) /255
    img_array_list.append(temp_img_array)
    
teach_array_list = []
teach_label_list = []

#各クラス20枚ずつ取り出して教師用データにする。
# 20*37 = 740
# 学習データ3050枚、教師データ740枚にわけたい
j=0
for j in range(37):
    for i in range(len(img_label_list)):   
        while(teach_label_list.count(j) <=20):
            teach_label_list.append(img_label_list.pop(i))
            teach_array_list.append(img_array_list.pop(i))
        continue

test_label_list = img_label_list
test_array_list = img_array_list

test_array_listnp = np.array(teach_array_list)#教師データ
test_label_listnp = np.array(teach_label_list)#教師ラベル
train_array_listnp = np.array(test_array_list)#学習データ
train_label_listnp = np.array(test_label_list)#学習ラベル

np.save('test_array.npy',test_array_listnp)
np.save('test_label.npy',test_label_listnp)
np.save('train_array.npy',train_array_listnp)
np.save('train_label.npy',train_label_listnp)

