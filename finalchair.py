#coding:utf-8
import rhinoscriptsyntax as rs
import math
import time
import random as rnd
import scriptcontext
import csv

def return_rectangle_pt(num, cnt, r, h):
    #半径r，高さh，椅子の脚がnum個ある時，cnt個目の椅子の座標を返す関数
    fst_taple_list = [(r - 7.5, 0.6, h), (r - 7.5, -0.6, h), (r - 3, -0.6, h), (r - 3, 0.6, h)]

    cnt_taple_list = []     #Answer 
    base_deg = (2 * math.pi)/num    #deviding 360 by number of legs
    for i in range(4):
        deg = base_deg * cnt
        cnt_taple_list.append(
            (fst_taple_list[i][0] * math.cos(deg) - fst_taple_list[i][1] * math.sin(deg),
            fst_taple_list[i][0] * math.sin(deg) + fst_taple_list[i][1] * math.cos(deg),
            h)
        )

    return cnt_taple_list

# def drawRHN(r, h, num_leg):
#         text = "r: %s\n" % r
#         text+= "h: %s\nnum_leg: %s\n" % (h, num_leg)
#         point = [0,-150,0]
#         height = 150
#         font = "Arial"
#         font_style = 0
#         justification = None
#         id = rs.AddText( text,
#                     point,
#                     height,
#                     font,
#                     font_style,
#                     justification)
#         return id

rhn = []
max = 1000
for i in range(max):
    rs.DeleteObjects(rs.AllObjects())

    num_legs = rnd.randint(4, 20)
    r = rnd.random() * 35 + 15
    h = rnd.random() * 50 + 20
    rhn.append([r, h, num_legs])
    pitch = 360 / num_legs
    for j in range(num_legs):
        surface = rs.AddSrfPt(return_rectangle_pt(num_legs, j, r, h))
        curve = rs.AddLine((0, 0, h), (0, 0, 0))
        rs.ExtrudeSurface(surface, curve)

    # 座椅子を作る
    # 円を描いて面にする
    circle = rs.AddCircle((0, 0, h), 10)
    surface = rs.AddPlanarSrf(circle)
    # 押し出し　厚さは1.2
    curve = rs.AddLine((0, 0, h), (0, 0, h + 1.2))
    rs.ExtrudeSurface(surface, curve)

    # 内側の小さい円と外側の大きい円
    circle1 = rs.AddCircle((0, 0, h), 12)
    circle2 = rs.AddCircle((0, 0, h), r)
    # それぞれ面にして押し出し　厚さは1.2
    surface = rs.AddPlanarSrf([circle1, circle2])
    curve = rs.AddLine((0, 0, h), (0, 0, h + 1.2))
    rs.ExtrudeSurface(surface, curve)


    circle = rs.AddCircle((0, 0, h - 5), r - 2)
    surface = rs.AddPlanarSrf(circle)
    curve = rs.AddLine((0, 0, h), (0, 0, h + 1.2))
    rs.ExtrudeSurface(surface, curve)
    
    # t = drawRHN(r, h, num_legs)
    # rs.RotateObject(t, 0, 0, math.arctan(133/h))

    # カメラ
    angle = 45
    view = rs.CurrentView()
    camera = [0, -200, h * 2]
    target = [0, 0, h/2]
    rs.ViewCameraTarget( view, camera, target )

    rs.EnableRedraw(False)
    # 描画
    
    # キャプチャー
    bitmap = scriptcontext.doc.ActiveDoc.Views.ActiveView.CaptureToBitmap(True,True,True)
    bitmap.Save("image/image{}.png".format(i))

    # 削除はforの頭でやる
    

    rs.EnableRedraw(True)

with open('./rhn.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(rhn)