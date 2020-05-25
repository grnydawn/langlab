import os
from langlab import Langlab

here = os.path.dirname(os.path.abspath(__file__))


def test_basic():

    prj = Langlab()

    cmd = "input @1 --forward '@x=2'"
    ret, fwds = prj.run_command(cmd)

    assert ret == 0

def test_print(capsys):

    prj = Langlab()

    cmd = "-- input @1 --forward '@x=2' -- print @x @data[0]"
    ret, fwds = prj.run_command(cmd)

    assert ret == 0

    captured = capsys.readouterr()
    assert captured.out == "21\n"
    assert captured.err == ""

def test_parse_makefile(capsys):

    prj = Langlab()
    makefile = os.path.join(here, "src", "Depends.intel")

    cmd = "-- parsemk %s -s -- print @data" % makefile
    ret, fwds = prj.run_command(cmd)

    assert ret == 0

    captured = capsys.readouterr()
    assert captured.out.startswith("PERFOBJS")
    assert captured.err == ""
