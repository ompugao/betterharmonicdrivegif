# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os

# os.mkdir('output')


def bgr2rgb(color):
    return (color[2], color[1], color[0])

def draw_centeraxis(img, theta):
    center = (np.array([img.shape[0], img.shape[1]]) / 2).astype(np.int64)
    r_green = 180
    pos1 = 150 * np.array([np.cos(theta), np.sin(theta)]) + center
    pos1 = tuple(pos1.astype(np.int64))
    pos2 = 200 * np.array([np.cos(theta), np.sin(theta)]) + center
    pos2 = tuple(pos2.astype(np.int64))
    # tiplength = 50.0/np.linalg.norm(pos2 - pos1)
    return cv2.arrowedLine(imgpad, pos1, pos2, bgr2rgb((158, 255, 177)), thickness=9, line_type=cv2.FILLED, tipLength=0.5)

def draw_outeraxis(img, theta):
    center = (np.array([img.shape[0], img.shape[1]]) / 2).astype(np.int64)
    r_green = 180
    pos1 = 350 * np.array([np.cos(theta), np.sin(theta)]) + center
    pos1 = tuple(pos1.astype(np.int64))
    pos2 = 300 * np.array([np.cos(theta), np.sin(theta)]) + center
    pos2 = tuple(pos2.astype(np.int64))
    # tiplength = 50.0/np.linalg.norm(pos2 - pos1)
    return cv2.arrowedLine(imgpad, pos1, pos2, bgr2rgb((255, 28, 28)), thickness=9, line_type=cv2.FILLED, tipLength=0.5)


plt.subplot(211)
nframeperrotation = 100
ratio = 40
for i in range(ratio*nframeperrotation):
    filename = 'frame-%02d.png'%(i%100)
    imgorig = cv2.imread(filename)
    margin = 100
    imgpad = cv2.copyMakeBorder(imgorig, margin, margin, margin, margin, cv2.BORDER_CONSTANT, value=(255,255,255))
    # imgpad = cv2.copyMakeBorder(imgorig, top, bottom, left, right, borderType)
    #plt.imshow(imgpad)
    #plt.show()
    # plt.subplot(211),plt.imshow(cv2.cvtColor(imgorig, cv2.COLOR_BGR2RGB)),plt.title('ORIGINAL')
    # plt.subplot(212),plt.imshow(cv2.cvtColor(imgpad, cv2.COLOR_BGR2RGB)),plt.title('CONSTANT')

    # plt.show()
    theta = i*np.pi*2 / nframeperrotation / 2
    imgpad2 = draw_centeraxis(imgpad, theta)

    dtheta = np.pi*2 / nframeperrotation / ratio
    theta = - (i*np.pi*2 / nframeperrotation / ratio + (dtheta*0.4*np.sin(i*np.pi*2 / nframeperrotation)))
    imgpad3 = draw_outeraxis(imgpad2, theta)
    # plt.show()

    # plt.clf()
    # plt.imshow(cv2.cvtColor(imgpad3, cv2.COLOR_BGR2RGB)),plt.title('CONSTANT')
    # plt.draw()
    # plt.pause(0.00001)
    cv2.imwrite('output/frame-%05d.png'%i, imgpad3)
    print(i)
