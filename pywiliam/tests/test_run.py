import pytest
import runpy


def test_pysd_version(mocker, proj_folder):
    """It should raise RuntimeError if pysd<3.10"""

    mocker.patch('pysd.__version__', return_value="3.9")

    with pytest.raises(RuntimeError):
        runpy.run_path(str(proj_folder.joinpath("run.py")))
