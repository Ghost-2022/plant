#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Date: 2023/4/10 17:13
    @Auth: Jacob
    @Desc:
"""
import os
import uuid

from flask import request, jsonify, current_app, url_for
from PIL import Image

from . import api


@api.route('/identify', methods=['GET', 'POST'])
def identify():
    """
    识别接口
    """
    if request.method == 'POST':
        identify_type = request.form.get('type')
        file = request.files.get('file')
        if not file:
            return jsonify({'code': 400, 'message': '需要上传图片'})
        file_path = os.path.join(current_app.config['UPLOAD_IMG'], file.filename)

        save_file_name = f'{uuid.uuid4().hex}.png'
        save_path = os.path.join(current_app.config['UPLOAD_IMG'], save_file_name)
        file.save(file_path)
        image = Image.open(file_path)
        data = {'imgUrl': file_path.replace('app', ''), 'resultUrl': save_path.replace('app', '')}
        if identify_type == 'classification':
            class_name, probability = current_app.classification.detect_image(image, save_path)
            data['tableData'] = [{'className': class_name, 'probability': f'{probability:.3f}',
                                  'size': f"{image.size[0]}*{image.size[1]}"}]
        elif identify_type == 'detection':
            new_image, class_name = current_app.detection.detect_image(image, crop=True, count=True)
            new_image.save(save_path)
            data['tableData'] = [{'className': class_name,
                                  'size': f"{image.size[0]}*{image.size[1]}"}]
        elif identify_type == 'segmentation':
            new_image = current_app.segmentation.detect_image(image, count=False, name_classes=["_background_", "1", '2', '3'])
            new_image.save(save_path)
        return jsonify({'code': 200, 'message': 'success', 'data': data})
    else:
        return jsonify({'code': 405, 'message': 'Method Not Allowed', 'method': request.method})


