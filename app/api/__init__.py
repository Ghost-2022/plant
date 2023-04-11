#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Date: 2023/4/10 17:28
    @Auth: Jacob
    @Desc:
"""
from flask import Blueprint

api = Blueprint('/api/', __name__, url_prefix='/api/')

from . import views