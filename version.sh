#!/bin/bash

set -ue

python -V

## 导出pip依赖
pip freeze > lib.txt