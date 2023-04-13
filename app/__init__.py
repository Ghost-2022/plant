#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Date: 2023/4/10 16:58
    @Auth: Jacob
    @Desc:
"""
import os

from flask import Flask
from flask_cors import CORS
import torch

from app.model.classification import classification
from app.model.detection import yolo
from app.model.segmentation import deeplab
from . import api
from app.setting import config


def create_app():
    app = Flask(__name__)
    env = os.getenv('APP_ENV', 'develop')
    app.config.from_object(config.config_map.get(env))
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.register_blueprint(api.api)

    cuda = torch.cuda.is_available()
    app.classification = classification.Classification(
        model_path=app.config['CLASSIFICATION_MODEL_PATH'],
        classes_path=app.config['CLASSIFICATION_CLASSES_PATH'],
        cuda=cuda
    )
    app.detection = yolo.YOLO(
        model_path=app.config['YOLO_MODEL_PATH'],
        classes_path=app.config['YOLO_CLASSES_PATH'],
        anchors_path=app.config['YOLO_ANCHORS_PATH'],
        font_path=app.config['YOLO_FONT_PATH'],
        cuda=cuda
    )
    app.segmentation = deeplab.DeeplabV3(
        model_path=app.config['DEEPLAB_MODEL_PATH'],
        cuda=cuda
    )

    return app
