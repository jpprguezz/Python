import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('data/route1.dat', (320, 151, 382)),
    ('data/route2.dat', (31, 4, 0)),
    ('data/route3.dat', (60, -1, 698)),
    ('data/route4.dat', (176, 601, 1590)),
]


@pytest.mark.parametrize('route_path, expected', testdata)
def test_run(route_path, expected):
    assert main.run(route_path) == expected
