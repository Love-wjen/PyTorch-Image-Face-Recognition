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

2️⃣ 运行程序
图像分类训练
python train_image_classifier.py
实时人脸识别
python face_detection.py
📁 项目结构
PyTorch-Image-Face-Recognition/
├── data/                # 数据集文件夹
├── models/              # 网络模型文件
├── utils/               # 工具类代码
├── train_image_classifier.py
├── face_detection.py
└── README.md
✅ 项目亮点
零基础友好，代码简洁易懂
模块化设计，方便修改与复用
适配课程作业、实训、简历项目
深度学习计算机视觉入门实战
📌 后续拓展
升级 ResNet 等深度网络，提升识别精度
新增人脸表情、身份识别功能
结合 Web 框架，搭建网页端识别系统
拓展图像缺陷检测、智能识别场景
🌍 English Version
📖 Project Introduction

This project is developed based on Python, PyTorch and OpenCV. It integrates lightweight CNN image classification and real-time face detection.

It supports image recognition and real-time face detection, making it suitable for computer vision learning and practical applications.

🧩 Features
Image classification and recognition
Real-time face detection via camera
Custom model training
Visual analysis of training results
Easy to expand and optimize
⚙️ Tech Stack
Python 3.8+
PyTorch
Torchvision
OpenCV-Python
NumPy, Matplotlib
🚀 Quick Start
pip install torch torchvision opencv-python numpy matplotlib
✅ Advantages
Simple and clear code
Beginner-friendly
Suitable for projects and portfolio
Easy for future improvement and expansion
📜 License

MIT License

🙌 Acknowledgements
PyTorch
OpenCV
Open Source Community
