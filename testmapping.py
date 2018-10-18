from mapping import pointMapping
import matplotlib.pyplot as plt

points = [(35.647156, 139.709739), (35.714071, 139.774079),(35.713968, 139.79645), (35.712056, 139.762775), (35.702259, 139.774473), (35.690543, 139.754693), (35.672801, 139.692596), (35.672114, 139.770825), (35.635585, 139.884578), (35.629686, 139.77499)]
points2= [(35.628471, 139.73876), (35.6192719, 139.7767197), (35.716454, 139.771318), (35.718835, 139.776522), (35.665289, 139.726374), (35.665486, 139.770667), (35.681167, 139.767052), (35.710063, 139.8107)]
#Shinagawa, Miraikan, Ueno Zoo, Museum, New Art Museum, Tsukiji, Tokyo Sta., Skytree
m = pointMapping(points2)
print(m.height, m.width)

x_arr = []
y_arr = []

for x,y in m._points:
    x_arr.append(x)
    y_arr.append(y)

plt.gca().invert_yaxis()
plt.scatter(x_arr,y_arr)
plt.show()

