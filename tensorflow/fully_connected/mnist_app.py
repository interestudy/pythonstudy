# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-15 19:30
# @File      :mnist_app.py
# @Software  :PyCharm

import tensorflow as tf
import numpy as np
from PIL import Image
from fully_connected import mnist_backward, mnist_forward


# 恢复模型
def restore_model(test_pic_arr):
    with tf.Graph().as_default() as tg:
        x = tf.placeholder(tf.float32, [None, mnist_forward.INPUT_NODE])
        y = mnist_forward.forward(x, None)
        pre_value = tf.argmax(y, 1)

        # 采用滑动平均的方式从训练好的模型中恢复参数值
        variable_averages = tf.train.ExponentialMovingAverage(mnist_backward.MOVING_AVERAGE_DECAY)
        variables_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variables_to_restore)
        # 创建会话 开始测试
        with tf.Session() as sess:
            ckpt = tf.train.get_checkpoint_state(mnist_backward.MODEL_SAVE_PATH)
            if ckpt and ckpt.model_checkpoint_path:
                saver.restore(sess, ckpt.model_checkpoint_path)

                pre_value = sess.run(pre_value, feed_dict={x: test_pic_arr})
                return pre_value
            else:
                print("No checkpoint file found")
                return -1


# 图片预处理
def pre_pic(pic_name):
    img = Image.open(pic_name)  # 打开图片生成Image对象
    re_im = img.resize((28, 28), Image.ANTIALIAS)  # 剪裁为28*28像素 抗锯齿
    re_im.convert('L').show()   # 显示灰度后的图片
    im_arr = np.array(re_im.convert('L'))  # 彩色转换为黑白 转换为矩阵
    threshold = 50
    # 遍历每一个像素 转换为1，0的矩阵
    for i in range(28):
        for j in range(28):
            im_arr[i, j] = 255 - im_arr[i, j]
            if im_arr[i][j] < threshold:
                im_arr[i][j] = 0
            else:
                im_arr[i][j] = 255

    nm_arr = im_arr.reshape(1, 784)
    nm_arr = nm_arr.astype(np.float32)
    img_ready = np.multiply(nm_arr, 1.0/255.0)
    return img_ready


# 读取控制台信息
def application():
    test_num = input('input the number of test pictures:')
    # print(eval(test_num))
    for i in range(eval(test_num)):
        test_pic = input('the path of test picture:')
        test_pic_arr = pre_pic(test_pic)
        pre_value = restore_model(test_pic_arr)
        print("The prediction number is:", pre_value)


def main():
    application()


if __name__ == '__main__':
    main()

