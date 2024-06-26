import gmsh
import pandas as pd
import numpy as np
import sys

DF = pd.read_csv("./ttt.csv")

X = np.array(DF.iloc[:, 0])
Y = np.array(DF.iloc[:, 1])

SIZE = DF.shape[0]

gmsh.initialize()

for i, point in enumerate(zip(X, Y)):
    x, y = point
    gmsh.model.geo.addPoint(x, y, 0, 200.0, i + 1)

gmsh.model.geo.addLine(1, SIZE, 1)

for i in range(2, SIZE + 1):
    gmsh.model.geo.add_line(SIZE + 2 - i, SIZE + 1 - i, i)

gmsh.model.geo.addCurveLoop([SIZE] + [i for i in range(1, SIZE)], 1)

gmsh.model.geo.addPlaneSurface([1], 1)

gmsh.model.geo.add_point(-31, 550, 0, 0.01, SIZE + 1)
gmsh.model.geo.synchronize()
gmsh.model.mesh.embed(0, [SIZE + 1], 2, 1)

gmsh.model.mesh.generate(1)
gmsh.model.mesh.refine()
gmsh.model.mesh.generate(2)

gmsh.write("GFG.msh")

gmsh.fltk.run()
gmsh.finalize()