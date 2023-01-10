# Robot Perception Tutorial

This repo contains examples for manipulating point cloud data and basic ICP odometry.

## Data
A public CARLA dataset is available: https://drive.google.com/drive/folders/1ZvZNciFTd71-3tSiCzUWCZnVxEyuGBAQ?usp=share_link

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

```bash
mkdir point_cloud_data
mkdir ply
```

unzip the above CARLA lidar data and put the `.npy` files to `point_cloud_data`

```bash
python run_icp.py
```

The transformed points are saved to `ply`

## ICP
Currently there are two ICP methods available
1. point-to-point ICP (from https://github.com/ClayFlannigan/icp)
2. point-to-plane ICP (from https://github.com/pglira/simpleICP)

## Colab example
https://colab.research.google.com/drive/1MiJIdCOQppVoseCKH0vMo0go2p2EbK3G?usp=sharing#scrollTo=mLPi_52VKEU6