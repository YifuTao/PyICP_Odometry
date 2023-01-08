# Robot Perception Tutorial

This repo contains examples for manipulating point cloud data and basic ICP odometry.

## Data
A public CARLA dataset is available: https://drive.google.com/drive/folders/1Ni6TpQPz8jFWxQMt-aSrvPsr5mrCPaIb?usp=sharing

It contains synced lidar point cloud, camera images, and poses.

## Dependency

```bash
pip install -r requirements.txt
```

If you are in China, you can run this instead:

```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Quick Start

`mkdir point_cloud_data`

unzip the above CARLA lidar data

`python point_cloud_loading.py`

## Colab example
https://colab.research.google.com/drive/1MiJIdCOQppVoseCKH0vMo0go2p2EbK3G?usp=sharing#scrollTo=mLPi_52VKEU6