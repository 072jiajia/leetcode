eps = 1e-8
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        overlap = 0
        lx, ly = location
        angles = []
        angle_trans = 180. / math.pi
        for x, y in  points:
            if x == lx and y == ly:
                overlap += 1
                continue
            
            offset_x, offset_y = x - lx, y - ly
            a = math.acos(offset_x / (offset_x * offset_x + offset_y * offset_y) ** 0.5) * angle_trans
            if offset_y < 0:
                a = 360 - a
            angles.append(a)

        max_visible = 0
        angles.sort()
        for a in list(angles):
            angles.append(a + 360)

        visible_right = 0
        for i, angle_left in enumerate(angles[:len(angles)//2]):
            angle_right = angle_left + angle + eps
            
            if angles[-1] <= angle_right:
                max_visible = max(len(angles) -1 -i, max_visible)
                break

            while angles[visible_right] <= angle_right:
                visible_right += 1
            max_visible = max(visible_right - i, max_visible)

        return max_visible + overlap
