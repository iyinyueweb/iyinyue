__author__ = 'jjzhu'
from pylab import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def show_sin_cos():
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c, s = np.cos(x), np.sin(x)

    xlim(-4.0, 4.0)  # 横轴上下限
    # xticks(np.linspace(-4, 4, 9, endpoint=True))
    ylim(-1.0, 1.0)  # 纵轴
    # yticks(np.linspace(-1, 1, 5, endpoint=True))
    xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    yticks([-1, 0, +1],
           [r'$-1$', r'$0$', r'$+1$'])
    ax =gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    plot(x, c, color='blue', linewidth=1.0, linestyle='-', label='cosine')
    plot(x, s, color='red', linewidth=1.0, linestyle='-', label='sine')
    legend(loc='upper left')

    t = 2*np.pi/3
    plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
    scatter([t, ], [np.cos(t), ], 50, color='blue')

    annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
    scatter([t, ], [np.sin(t), ], 50, color='red')

    annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    show()


def show_normal_graph():
    n = 256
    x = np.linspace(-np.pi, np.pi, n, endpoint=True)
    y = np.sin(2*x)
    plot(x, y + 1, color='blue', alpha=1.00)
    plot(x, y - 1, color='blue', alpha=1.00)
    show()


def show_point():
    n = 1024
    x = np.random.normal(0, 1, n)
    y = np.random.normal(0, 1, n)
    scatter(x[0: 512], y[0:512], c='red')
    scatter(x[513: 1023], y[513: 1023], c='blue')
    show()


def show_bar_shape():
    x1 = [0, 2, 4]
    x2 = [0.5, 2.5, 4.5]
    y1 = [0.61, 0.32, 0.58]
    y2 = [0.68, 0.54, 0.71]
    lab = [u'准确率', u'覆盖率', u'多样性']
    title(u'相似度计算改进前后的各指标对比直方图')
    bar(x1, y1, facecolor='#9999ff', edgecolor='white', width=0.5, label='改进前')
    bar(x2, y2, facecolor='#ff8888', edgecolor='white', width=0.5, label='改进后')

    for x, y in zip(x1, y1):
        text(x+0.25, y+0.05, '%.2f' % y, ha='center', va='bottom')
    for x, y in zip(x2, y2):
        text(x+0.25, y+0.05, '%.2f' % y, ha='center', va='bottom')
    i = 0
    for x, y in zip(x1, y1):
        text(x+0.5, -0.05, '%s' % lab[i], ha='center', va='bottom')
        i += 1
    ylim(0, 1)
    legend(loc='upper left')
    show()


def show_bar_shape2():
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.arange(0, 1000, 0.5)
    y = np.random.rand(2000)*10
    n, bins, patches = plt.hist(y, 50, normed=1, alpha=0.8)
    plt.title('Hist of Y')
    plt.xlabel('Smarts')
    plt.ylabel('NormProbability')
    plt.text(2, 0.12, '$\mu=10,\\sigma=20$')
    plt.grid(True)
    plt.show()


def show_contour():
    def f(x, y):
        return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

    n = 256
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X, Y = np.meshgrid(x, y)

    contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='jet')
    C = contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
    show()


def show_polar():
    axes([0, 0, 1, 1])
    N = 20
    theta = np.arange(0.0, 2*np.pi, 2*np.pi/N)
    radii = 10*np.random.rand(N)
    width = np.pi/4*np.random.rand(N)
    bars = bar(theta, radii, width=width, bottom=0.0)

    for r, b in zip(radii, bars):
        b.set_facecolor(cm.jet(r/10.))
        b.set_alpha(0.5)
    show()


def show_3d():
    fig = figure()
    ax = Axes3D(fig)
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')

    show()

if __name__ == '__main__':
    # show_sin_cos()
    # show_normal_graph()
    # show_point()
    show_bar_shape()
    # show_contour()
    # show_polar()
    # show_3d()