same = input("error the same? Y or N")
if same == 'Y':
    xmin = float(input("xmin "))
    ymin = float(input("ymin "))
    xmax = float(input("xmax "))
    ymax = float(input("ymax "))
    dx = float(input("dx "))
    dy = float(input("dy "))

    print("max steepness slope")
    print(f"({xmin+dx}, {ymin-dy}), ({xmax-dx}, {ymax+dy})")
    print(f"slope = {(ymax+dy-ymin+dy)/(xmax-dx-xmin-dx)}")
    print(f"intercept = {ymin-dy-(ymax+dy-ymin+dy)/(xmax-dx-xmin-dx)*(xmin+dx)}")

    print("min steepness slope")
    print(f"({xmin-dx}, {ymin+dy}), ({xmax+dx}, {ymax-dy})")
    print(f"slope = {(ymax-dy-ymin-dy)/(xmax+dx-xmin+dx)}")
    print(f"intercept = {ymin+dy-(ymax-dy-ymin-dy)/(xmax+dx-xmin+dx)*(xmin-dx)}")

else:
    xmin = float(input("xmin "))
    ymin = float(input("ymin "))
    xmax = float(input("xmax "))
    ymax = float(input("ymax "))
    dxmin = float(input("dxmin "))
    dymin = float(input("dymin "))
    dxmax = float(input("dxmax "))
    dymax = float(input("dymax "))

    print("max steepness slope")
    print(f"({xmin + dxmin}, {ymin - dymin}), ({xmax - dxmax}, {ymax + dymax})")
    print(f"slope = {(ymax + dymax - ymin + dymin) / (xmax - dxmax - xmin - dxmin)}")
    print(f"intercept = {ymin - dymin - (ymax + dymax - ymin + dymin) / (xmax - dxmax - xmin - dxmin) * (xmin + dxmin)}")

    print("min steepness slope")
    print(f"({xmin - dxmin}, {ymin + dymin}), ({xmax + dxmax}, {ymax - dymax})")
    print(f"slope = {(ymax - dymax - ymin - dymin) / (xmax + dxmax - xmin + dxmin)}")
    print(f"intercept = {ymin + dymin - (ymax - dymax - ymin - dymin) / (xmax + dxmax - xmin + dxmin) * (xmin - dxmin)}")
