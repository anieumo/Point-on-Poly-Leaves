import pymel.core as pm
#pm.curve( d=3, p=[(0, 2, 0), (0, 1, -1 ), (0, 0, 0), (0, 1, 1), (0, 2, 0)])
#pm.planarSrf( d=1, ch=1, ko=0, tol=0.01, rn=0, po=1 )

sel = pm.ls(sl=True)
vtx = 'cell'
selected = cmds.ls(sl=True,long=True)
print(selected)
vtx = pm.ls(selected[0] + '.vtx[*]', fl=True)
print(vtx)

for each in vtx:
        
    cc = pm.curve( d=3, p=[(0, 2, 0), (0, 1, -1 ), (0, 0, 0), (0, 1, 1), (0, 2, 0)])
    cl = pm.cluster(each)
    pm.matchTransform(cl, each)