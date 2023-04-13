#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Date: 2023/4/10 18:42
    @Auth: Jacob
    @Desc:
"""
import os

BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig:
    UPLOAD_IMG = 'app/static/imgs'


class DevlopConfig(BaseConfig):
    CLASSIFICATION_MODEL_PATH = os.path.join(BASEDIR, 'model/classification/logs/best_epoch_weights.pth')
    CLASSIFICATION_CLASSES_PATH = os.path.join(BASEDIR, 'model/classification/model_data/cls_classes.txt')
    YOLO_MODEL_PATH = os.path.join(BASEDIR, 'model/detection/logs/best_epoch_weights.pth')
    YOLO_CLASSES_PATH = os.path.join(BASEDIR, 'model/detection/model_data/new_classes.txt')
    YOLO_ANCHORS_PATH = os.path.join(BASEDIR, 'model/detection/model_data/yolo_anchors.txt')
    YOLO_FONT_PATH = os.path.join(BASEDIR, 'model/detection/model_data/simhei.ttf')
    DEEPLAB_MODEL_PATH = os.path.join(BASEDIR, 'model/segmentation/logs/best_epoch_weights.pth')


class ProductConfig(BaseConfig):
    CLASSIFICATION_MODEL_PATH = ''
    CLASSIFICATION_CLASSES_PATH = ''
    YOLO_MODEL_PATH = ''
    YOLO_CLASSES_PATH = ''
    YOLO_ANCHORS_PATH = ''
    DEEPLAB_MODEL_PATH = ''


config_map = {
    'develop': DevlopConfig,
    'product': ProductConfig,
}
