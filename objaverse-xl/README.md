Forked from allenai/objaverse-xl
https://github.com/allenai/objaverse-xl.git
对部分代码进行了修改

以下为适合在Jupyter Book中安装的代码：

```jupyter
import os
repo_path="/content/objaverse-xl"

if os.path.exists(repo_path):
    print(f"仓库已存在于 {repo_path}，跳过克隆步骤。")
else:
    # 克隆仓库
    !git clone https://github.com/allenai/objaverse-xl.git

    # 进入目标目录
    %cd objaverse-xl/scripts/rendering

    # 下载并解压 Blender 到当前目录
    !wget https://download.blender.org/release/Blender3.2/blender-3.2.2-linux-x64.tar.xz -P ./ && \
      tar -xf blender-3.2.2-linux-x64.tar.xz -C ./ && \
      rm blender-3.2.2-linux-x64.tar.xz

    # 检查 Blender 是否已正确安装在当前目录中
    !./blender-3.2.2-linux-x64/blender -b --version

    # 返回项目根目录并安装 Python 依赖
    %cd ../..
    !pip install -r requirements.txt && \
      pip install -e .
```

运行：

```
%cd scripts/rendering
!python3 main.py
```

