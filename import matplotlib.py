import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# 점 (별) 위치 생성
np.random.seed(42)
stars = np.random.rand(50, 2) * [7, 5]

# 연결할 선 (선택된 점들만 일부 연결)
edges = [
    (0, 1), (2, 3), (4, 5), (6, 7), (10, 11), (12, 13),
    (14, 15), (16, 17), (18, 19)
]

fig, ax = plt.subplots(figsize=(8, 5))
ax.set_facecolor('black')
ax.set_xlim(0, 7)
ax.set_ylim(0, 5)
ax.axis('off')

star_dots = ax.scatter([], [], c='white', s=10)
line_objs = []

def init():
    star_dots.set_offsets(np.empty((0, 2)))
    return star_dots,

def update(frame):
    if frame < len(stars):
        star_dots.set_offsets(stars[:frame+1])
    else:
        edge_i = frame - len(stars)
        if edge_i < len(edges):
            s, e = edges[edge_i]
            x = [stars[s][0], stars[e][0]]
            y = [stars[s][1], stars[e][1]]
            line, = ax.plot(x, y, color='white', linewidth=0.5)
            line_objs.append(line)
    return [star_dots] + line_objs

ani = animation.FuncAnimation(
    fig, update, init_func=init,
    frames=len(stars) + len(edges) + 10,
    interval=120,
    blit=False  # ✅ 반드시 False로 설정!
)

ani.save("/mnt/data/ai_opening_fixed.mp4", dpi=150)

