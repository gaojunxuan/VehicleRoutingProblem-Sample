import math

KM_PER_LAT = 111
KM_PER_LON = 85
class pointMapping:
    def __init__(self, points:list):
        self._lats = [p[0] for p in points]
        self._lons = [p[1] for p in points]
        self._count = len(points)
        self._points = []
        self.mapPoints()
    
    @property
    def height(self):
        return math.ceil((max(self._lats) - min(self._lats)) * KM_PER_LAT)

    @property
    def width(self):
        return math.ceil((max(self._lons) - min(self._lons)) * KM_PER_LON)

    def mapPoints(self):
        maxLat = max(self._lats)
        minLon = min(self._lons)
        for i in range(self._count):
            x = (self._lons[i] - minLon) * KM_PER_LON
            y = (maxLat - self._lats[i]) * KM_PER_LAT
            self._points.append((x,y))
