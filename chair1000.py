
#coding:utf-8
import rhinoscriptsyntax as rs
import math
import time
import random as rnd
import scriptcontext
def return_rectangle_pt(num, cnt, r, h):
    #半径r，高さh，椅子の脚がnum個ある時，cnt個目の椅子の座標を返す関数
    fst_taple_list = [(r - 7.5, 0.6, h), (r - 7.5, -0.6, h), (r - 3, 0.6, h), (r - 3, -0.6, h)]

    cnt_taple_list = []     #Answer 
    base_deg = 2 * math.pi/num    #deviding 360 by number of legs
    for i in range(4):
        deg = base_deg * cnt
        cnt_taple_list.append((fst_taple_list[i][0] * math.cos(deg) - fst_taple_list[i][1] * math.sin(deg), fst_taple_list[i][0] * math.sin(deg) + fst_taple_list[i][1] * math.cos(deg), h))

    return cnt_taple_list
circle = rs.AddCircle((0, 0, 40), 10)
surface = rs.AddPlanarSrf(circle)
curve = rs.AddLine((0, 0, 40), (0, 0, 41.2))
rs.ExtrudeSurface(surface, curve)

circle1 = rs.AddCircle((0, 0, 40), 12)
circle2 = rs.AddCircle((0, 0, 40), 20)
surface = rs.AddPlanarSrf([circle1, circle2])
curve = rs.AddLine((0, 0, 40), (0, 0, 41.2))
rs.ExtrudeSurface(surface, curve)

for i in range(10):
    num_legs = rnd.randint(4, 50)
    r = rnd.random() * 45 + 5
    h = rnd.random() * 50 + 20
    pitch = 360 / num_legs
    for j in range(num_legs):
        surface = rs.AddSrfPt(return_rectangle_pt(num_legs, j, r, h))
        curve = rs.AddLine((0, 0, 40), (0, 0, 0))
        rs.ExtrudeSurface(surface, curve)

        circle = rs.AddCircle((0, 0, 35), 18)
        surface = rs.AddPlanarSrf(circle)
        curve = rs.AddLine((0, 0, 40), (0, 0, 41.2))
        rs.ExtrudeSurface(surface, curve)

    # カメラ
    angle = i * pitch
    view = rs.CurrentView()
    camera = [0, -230, -230 * 2]
    camera = rs.VectorRotate(camera, 45, [0, 1, 0])
    camera = rs.VectorRotate(camera, angle, [0, 0, 1])
    target = [0, 0, 0]
    rs.ViewCameraTarget( view, camera, target )

    rs.EnableRedraw(False)
    # 描画
   
 
    # キャプチャー
    bitmap =scriptcontext.doc.ActiveDoc.Views.ActiveView.CaptureToBitmap(True,True,True)
    bitmap.Save("image/image{}.png".format(j))
    # 消去

    rs.EnableRedraw(True)
#coding:utf-8
import rhinoscriptsyntax as rs
import math
import time
import random as rnd
import scriptcontext
def return_rectangle_pt(num, cnt, r, h):
    #半径r，高さh，椅子の脚がnum個ある時，cnt個目の椅子の座標を返す関数
    fst_taple_list = [(r - 7.5, 0.6, h), (r - 7.5, -0.6, h), (r - 3, 0.6, h), (r - 3, -0.6, h)]

    cnt_taple_list = []     #Answer 
    base_deg = 2 * math.pi/num    #deviding 360 by number of legs
    for i in range(4):
        deg = base_deg * cnt
        cnt_taple_list.append((fst_taple_list[i][0] * math.cos(deg) - fst_taple_list[i][1] * math.sin(deg), fst_taple_list[i][0] * math.sin(deg) + fst_taple_list[i][1] * math.cos(deg), h))

    return cnt_taple_list
circle = rs.AddCircle((0, 0, 40), 10)
surface = rs.AddPlanarSrf(circle)
curve = rs.AddLine((0, 0, 40), (0, 0, 41.2))
rs.ExtrudeSurface(surface, curve)

circle1 = rs.AddCircle((0, 0, 40), 12)
circle2 = rs.AddCircle((0, 0, 40), 20)
surface = rs.AddPlanarSrf([circle1, circle2])
curve = rs.AddLine((0, 0, 40), (0, 0, 41.2))
rs.ExtrudeSurface(surface, curve)

for i in range(10):
    num_legs = rnd.randint(4, 50)
    r = rnd.random() * 45 + 5
    h = rnd.random() * 50 + 20
    pitch = 360 / num_legs
    for j in range(num_legs):
        surface = rs.AddSrfPt(return_rectangle_pt(num_legs, j, r, h))
        curve = rs.AddLine((0, 0, 40), (0, 0, 0))
        rs.ExtrudeSurface(surface, curve)

        circle = rs.AddCircle((0, 0, 35), 18)
        surface = rs.AddPlanarSrf(circle)
        curve = rs.AddLine((0, 0, 40), (0, 0, 41.2))
        rs.ExtrudeSurface(surface, curve)

    # カメラ
    angle = i * pitch
    view = rs.CurrentView()
    camera = [0, -230, -230 * 2]
    camera = rs.VectorRotate(camera, 45, [0, 1, 0])
    camera = rs.VectorRotate(camera, angle, [0, 0, 1])
    target = [0, 0, 0]
    rs.ViewCameraTarget( view, camera, target )

    rs.EnableRedraw(False)
    # 描画
    
    # キャプチャー
    bitmap =scriptcontext.doc.ActiveDoc.Views.ActiveView.CaptureToBitmap(True,True,True)
    bitmap.Save("image/image{}.png".format(j))
    # 消去

    rs.EnableRedraw(True)