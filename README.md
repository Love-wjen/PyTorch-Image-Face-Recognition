# 🚀 PyTorch Image Classification & Face Recognition

A simple image classification and real-time face recognition system based on PyTorch and OpenCV

---

# 📌 基于PyTorch的图像分类与人脸识别系统

## 📖 项目简介
本项目基于 Python + PyTorch + OpenCV 开发，集成轻量级卷积神经网络图像分类与实时人脸识别功能。

主要包含两大模块：

1. 基于 CNN 的图像分类模型，支持花卉、动物、日常物品等图像识别  
2. 基于 OpenCV 的实时人脸检测，调用摄像头实现动态识别  

项目结构简洁、代码轻量化，适合深度学习入门、课程设计、实践作业及 GitHub 作品展示，便于后期拓展升级。

---

## 🧩 核心功能

- 图像分类：自动识别图片类别，完成图像智能判别  
- 人脸识别：调用电脑摄像头，实时检测并框选人脸  
- 模型训练：支持自定义数据集训练模型  
- 数据可视化：展示训练损失、精度变化曲线  
- 低门槛拓展：可升级为表情识别、目标检测等功能  

---

## ⚙️ 技术栈

- Python 3.8+  
- PyTorch 2.0+  
- OpenCV-Python  
- NumPy / Matplotlib  

---

## 🚀 快速运行

### 1️⃣ 安装依赖
```bash
pip install torch torchvision opencv-python numpy matplotlib
```
####2. 运行程序
- 图像分类训练
```bash
python train_image_classifier.py
```

- 实时人脸识别
```bash
python face_detection.py
```

---

### 📂 项目结构
```
PyTorch-Image-Face-Recognition/
├── data/                # 数据集存放文件夹
├── models/              # 深度学习模型文件
├── utils/               # 工具函数模块
├── train_image_classifier.py
├── face_detection.py
└── README.md
```

---

### ✅ 项目亮点
- 零基础友好，代码简洁易懂
- 模块化结构，便于修改与二次开发
- 适配课程实践、实训报告、简历项目
- 深度学习+计算机视觉入门优质案例

---

### 📌 后续拓展方向
- 升级ResNet等深层网络，提升识别准确率
- 增加人脸表情识别、身份识别功能
- 结合Web框架，搭建网页端识别平台
- 拓展工业图像缺陷检测等实用场景

---

# Image Classification & Face Recognition Based on PyTorch
### 📌 Project Introduction
This project is developed based on Python, PyTorch and OpenCV.
It combines lightweight CNN model and computer vision technology to realize image classification and real-time face detection.

### 🧩 Features
- Image classification and recognition
- Real-time face detection via webcam
- Custom dataset training
- Training data visualization
- Flexible expansion and optimization

### ⚙️ Tech Stack
- Python 3.8+
- PyTorch
- Torchvision
- OpenCV-Python
- Numpy, Matplotlib

### 🚀 Quick Start
```bash
pip install torch torchvision opencv-python numpy matplotlib
```

### ✅ Project Advantages
- Simple and standardized code
- Beginner-friendly design
- Suitable for academic and practical projects
- Easy to expand and upgrade
```
