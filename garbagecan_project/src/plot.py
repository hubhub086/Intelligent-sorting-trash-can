import matplotlib.pyplot as plt
import PIL.Image as Image
import numpy as np


class_num = 7
class_name = ['fruit', 'bricks', 'bottle', 'cigarette', 'vegetable', 'can', 'battery']


def drawplot(garbage):
    np.random.seed(5520)
    theta = np.linspace(0.0, 2 * np.pi, class_num, endpoint=False)
    width = np.pi / 4 * np.random.rand(class_num)
    radii = np.array([])
    for item in class_name:
        count = 0
        for i in garbage:
            for j in i:
                if j == item:
                    count += 1
        radii = np.append(radii, count)

    if len(garbage):
        radii = radii / len(garbage) * 10
    figure = plt.figure()
    ax = plt.subplot(111, projection='polar')
    bars = ax.bar(theta, radii, width=width, bottom=0.0)
    # 自定义颜色和不透明度
    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.viridis(r / 10.))
        bar.set_alpha(0.5)
    return figure


def fig2data(fig):
    # draw the renderer
    fig.canvas.draw()
 
    # Get the RGBA buffer from the figure
    w, h = fig.canvas.get_width_height()
    buf = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint8)
    buf.shape = (w, h, 4)
 
    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = np.roll(buf, 3, axis=2)
    image = Image.frombytes("RGBA", (w, h), buf.tostring())
    image = np.asarray(image)
    return image
