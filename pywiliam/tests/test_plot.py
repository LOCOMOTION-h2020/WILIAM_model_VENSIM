import pytest

from plot_tool import main


@pytest.mark.skip(reason="not implemented")
def test_open_plot_tool(default_config):
    """Run of the 3 models in cascade"""
    main(default_config)
