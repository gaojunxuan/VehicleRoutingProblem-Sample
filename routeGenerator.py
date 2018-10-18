import route, mapping

points = [(35.647156, 139.709739), (35.714071, 139.774079),(35.713968, 139.79645), (35.712056, 139.762775), (35.702259, 139.774473), (35.690543, 139.754693), (35.672801, 139.692596), (35.672114, 139.770825), (35.635585, 139.884578), (35.629686, 139.77499)]
names = ["ウェスティンホテル東京", "上野公園", "浅草寺", "東京大学", "秋葉原", "東京国立近代美術館", "代々木公園", "銀座", "ディズニーランド", "お台場海浜公園"]
demands = [0, 30, 30, 30, 4*60, 60, 30, 6*60, 7*60, 30]
if len(points) == len(names):
    mapped = mapping.pointMapping(points)._points
    routes = route.getRoute(mapped, demands, 3, 8*60)
    for key, val in routes.items():
        print(key, [names[i] for i in val])

