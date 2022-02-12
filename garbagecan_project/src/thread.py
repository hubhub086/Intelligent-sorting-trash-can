from PyQt5.QtCore import *
import numpy as np
import time
import cv2

garbage = []
VIDEO_SET = 1

class cameraThread(QObject):
    # 通过类成员对象定义信号
    items = pyqtSignal(list)
    img = pyqtSignal(np.ndarray)

    # 处理业务逻辑
    def run(self):
        label_path = '../net/garbage_sorting.names'
        config_path = '../net/yolo-garbage_sorting.cfg'
        weights_path = '../net/yolo-garbage_sorting_best.weights'
        confidence_thre = 0.3
        nms_thre = 0.3
        jpg_quality = 80
            
        labels = open(label_path).read().strip().split("\n")
        nclass = len(labels)

        # random color for bounding box
        np.random.seed(int(time.time()))
        COLOR = np.random.randint(0, 255, size=(nclass, 3), dtype='uint8')
        net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

        # get YOLO ouput_layer's name
        ln = net.getLayerNames()
        out = net.getUnconnectedOutLayers()  # Get the unconnected layer number
        x = []
        for i in out:
            x.append(ln[i - 1])
        ln = x
        ln = net.getUnconnectedOutLayersNames()

        # Capture video frames
        vs = cv2.VideoCapture(VIDEO_SET)
        # time.sleep(0.9)
        writer = None
        (W, H) = (None, None)
        while True:
            (grabbed, frame) = vs.read()
            if not grabbed:
                print(" not grabbed! exit thread2")
                break
            if W is None or H is None:
                (H, W) = frame.shape[:2]
            
            # classes, confidences, boxes =net.detect(img, confThreshold=0.1, nmsThresh=0.4)
            blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
            net.setInput(blob)
            start = time.time()
            layerOutputs = net.forward(ln)  # predit
            end = time.time()
            # print("use time for one detection: {:.2f}".format(end - start))

            boxes = []
            confidences = []
            classIDs = []

            # 循环提取每个输出层
            for output in layerOutputs:
                # 循环提取每个框
                for detection in output:
                    # 提取当前目标的类 ID 和置信度
                    scores = detection[5:]
                    classID = np.argmax(scores)
                    confidence = scores[classID]
                    # 通过确保检测概率大于最小概率来过滤弱预测
                    if confidence > confidence_thre:
                        # 将边界框坐标相对于图像的大小进行缩放，YOLO 返回的是边界框的中心(x, y)坐标，
                        # 后面是边界框的宽度和高度
                        box = detection[0:4] * np.array([W, H, W, H])
                        (centerX, centerY, width, height) = box.astype("int")
                        # 转换出边框左上角坐标
                        x = int(centerX - (width / 2))
                        y = int(centerY - (height / 2))
                        # 更新边界框坐标、置信度和类 id 的列表
                        boxes.append([x, y, int(width), int(height)])
                        confidences.append(float(confidence))
                        classIDs.append(classID)
            
            # 非最大值抑制，确定唯一边框
            idxs = cv2.dnn.NMSBoxes(boxes, confidences, confidence_thre, nms_thre)
            
            value = []
            # 确定每个对象至少有一个框存在
            if len(idxs) > 0:
                # 循环画出保存的边框
                for i in idxs.flatten():
                    # 提取坐标和宽度
                    (x, y) = (boxes[i][0], boxes[i][1])
                    (w, h) = (boxes[i][2], boxes[i][3])
                    # 画出边框和标签
                    temp = []
                    for c in COLOR[classIDs[i]]:
                        temp.append(int(c))
                    color = tuple(temp)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2, lineType=cv2.LINE_AA)
                    text = "{}: {:.4f}".format(labels[classIDs[i]], confidences[i])
                    cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, lineType=cv2.LINE_AA)
                    print(labels[classIDs[i]])
                    value.append(labels[classIDs[i]])
            if len(value) != 0:
                set_temp = list(set(value))
                for item in set_temp:
                    one_detection = [str(1 + len(garbage)), item, value.count(item), "OK"]
                    garbage.append(one_detection)
                self.items.emit(garbage)
                self.img.emit(frame)
                time.sleep(2)  # delay 2s
            self.img.emit(frame)
