#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Date: 2023/4/10 18:42
    @Auth: Jacob
    @Desc:
"""
import os


class BaseConfig:
    basedir = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_IMG = 'static/imgs'


class DevlopConfig(BaseConfig):
    CLASSIFICATION_MODEL_PATH = 'app/model/classification/logs/best_epoch_weights.pth'
    CLASSIFICATION_CLASSES_PATH = 'app/model/classification/model_data/cls_classes.txt'
    YOLO_MODEL_PATH = 'app/model/detection/logs/best_epoch_weights.pth'
    YOLO_CLASSES_PATH = 'app/model/detection/model_data/new_classes.txt'
    YOLO_ANCHORS_PATH = 'app/model/detection/model_data/yolo_anchors.txt'
    DEEPLAB_MODEL_PATH = 'app/model/segmentation/logs/best_epoch_weights.pth'


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