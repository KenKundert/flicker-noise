# Generates schematic as an .svg file.
# Requires svg_schematic:
#     git clone https://github.com/KenKundert/svg_schematic.git
#     cd svg-schematic
#     python3 setup.py --user --upgrade install

from svg_schematic import (
    Schematic, shift, shift_x, shift_y, midpoint, Box, Ground, Label, Source, Wire
)

with Schematic(filename = "msnm.svg"):
    v = Source(kind='noise', value='S(f)', orient='v')
    Ground(C=v.n, orient='v')

    m = Source(C=shift_x(v.p, 200), kind='mult')
    Wire([v.p, m.W])
    wm = Wire([m.S, shift_y(m.S, 25)])
    Label(C=wm.e, loc='S', name='m(t)')
    Label(C=midpoint(v.p, m.W), loc='N', name='stationary noise')

    wo = Wire([m.E, shift_x(m.E, 210)])
    Label(C=wo.e, kind='arrow', loc='NW', name='cyclostationary noise')

    Box(C=shift(v.C, 100, -3), w=5.5, h=3.2, line_width=0.5, background='none', stroke_dasharray="4 2")
