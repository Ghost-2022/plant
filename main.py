#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Date: 2023/4/10 16:57
    @Auth: Jacob
    @Desc:
"""
from app import create_app


def main():
    app = create_app()
    print(app.url_map)
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()