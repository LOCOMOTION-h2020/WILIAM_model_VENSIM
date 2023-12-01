import pytest

import pandas as pd

import tools.data_manager as dm


def test_data_container(proj_folder, doc):
    """Test the data container"""
    data_container = dm.DataContainer()
    data_container.add(
        dm.DataFile(
            proj_folder.joinpath(
                "tests/data/"
                "results_scenario_parameters_2005_2010_0.25.tab")))

    variables = data_container.variable_list
    assert len(variables) == 3
    assert len(data_container) == 1

    data_container.add(
        dm.DataFile(
            proj_folder.joinpath(
                "tests/data/unknown.csv")))

    assert variables == data_container.variable_list
    assert len(variables) == 3
    assert len(data_container) == 2

    data_container.add(
        dm.DataVensim(
            proj_folder.joinpath(
                "tests/data/vensim.tab"), doc))

    assert set(variables).issubset(data_container.variable_list)
    assert len(data_container) == 3

    data_container.set_var("ti_by_commodity")
    assert len(data_container.dimensions) == 2
    values = data_container.get_values(dimensions=('EU27', 'TI_gas_fossil'))
    assert isinstance(values, dict)

    assert isinstance(values["scenario_parameters"], pd.Series)
    assert isinstance(values["Unknown"], pd.Series)
    assert isinstance(values["Vensim output"], pd.Series)

    data_container.set_var("non_financial_corporations_financial_liabilities")
    assert len(data_container.dimensions) == 1

    data_container.clear()
    assert len(data_container) == 0


@pytest.mark.parametrize(
    "filename,scenario",
    [
        (  # BAU_full
            ("tests/data/results_scenario_parameters_2005_2010_0.25.tab",
             "scenario_parameters")
        ),
        (  # Unknown
            ("tests/data/unknown.csv", "Unknown")
        )
    ],
    ids=["scenario_parameters_full", "Unknown"]
)
class TestDataFile:
    """test for data coming from model outputs"""

    @pytest.fixture()
    def data_file(self, proj_folder, filename):
        """return data file object"""
        return dm.DataFile(proj_folder.joinpath(filename))

    def test_metadata(self, proj_folder, filename, data_file, scenario):
        """test the main attributes"""
        assert data_file.filename == proj_folder.joinpath(filename)
        assert data_file.scenario == scenario

    def test_colnames(self, data_file, scenario):
        """test that colnames are correct"""
        assert hasattr(data_file, "variable_list")
        assert len(data_file.variable_list) == 3
        assert len([var for var in data_file.variable_list if "[" in var]) == 0

    def test_set_get_var(self, data_file, scenario):
        """test that setting a var works"""
        assert "ti_by_commodity" not in data_file.cached_values
        assert data_file.current_var is None

        data_file.set_var("ti_by_commodity")
        assert isinstance(
            data_file.get_values(("INDIA", "TI_oceanic")),
            pd.Series)

        assert "ti_by_commodity" in data_file.cached_values
        assert data_file.current_var == "ti_by_commodity"

        assert data_file.get_values(("INDIA", "Peru")) is None

        data_file.set_var("non_financial_corporations_financial_assets")
        assert isinstance(
            data_file.get_values(("AUSTRIA",)),
            pd.Series)

        assert "non_financial_corporations_financial_assets" in \
            data_file.cached_values
        assert data_file.current_var == \
            "non_financial_corporations_financial_assets"

        data_file.set_var("this var does not exist")
        assert data_file.get_values() is None

        assert "this var does not exist" in data_file.cached_values
        assert data_file.current_var == "this var does not exist"


@pytest.mark.parametrize(
    "filename",
    [
        (  # Vensim
            "tests/data/vensim.tab"
        )
    ],
    ids=["Vensim"]
)
class TestDataVensim:
    """test for data coming from Vensim outputs"""

    @pytest.fixture()
    def data_file(self, proj_folder, filename, doc):
        """return data file object"""
        return dm.DataVensim(proj_folder.joinpath(filename), doc)

    def test_metadata(self, proj_folder, filename, data_file):
        """test the main attributes"""
        assert data_file.filename == proj_folder.joinpath(filename)
        assert data_file.scenario == "Vensim output"

    def test_colnames(self, data_file):
        """test that colnames are correct"""
        assert hasattr(data_file, "variable_list")
        assert len(data_file.variable_list) == 3
        assert len([var for var in data_file.variable_list if "[" in var]) == 0

    def test_set_get_var(self, data_file):
        """test that setting a var works"""
        assert "ti_by_commodity" not in data_file.cached_values
        assert data_file.current_var is None

        data_file.set_var("ti_by_commodity")
        assert isinstance(
            data_file.get_values(("INDIA", "TI_oceanic")),
            pd.Series)

        assert "ti_by_commodity" in data_file.cached_values
        assert data_file.current_var == "ti_by_commodity"

        assert data_file.get_values(("INDIA", "Peru")) is None

        data_file.set_var("non_financial_corporations_financial_assets")
        assert isinstance(
            data_file.get_values(("AUSTRIA",)),
            pd.Series)

        assert "non_financial_corporations_financial_assets" in \
            data_file.cached_values
        assert data_file.current_var == \
            "non_financial_corporations_financial_assets"

        data_file.set_var("this var does not exist")
        assert data_file.get_values() is None

        assert "this var does not exist" in data_file.cached_values
        assert data_file.current_var == "this var does not exist"


@pytest.mark.parametrize(
    "filename",
    [
        (  # netCDF
            "tests/data/results_my_scenario_2005_2050_0.25.nc"
        )
    ],
    ids=["netCDF"]
)
class TestDataNCFile:
    """test for data coming from Vensim outputs"""

    @pytest.fixture()
    def data_file(self, proj_folder, filename):
        """return data file object"""
        return dm.DataNCFile(proj_folder.joinpath(filename))

    def test_metadata(self, proj_folder, filename, data_file):
        """test the main attributes"""
        assert data_file.filename == proj_folder.joinpath(filename)
        assert data_file.scenario == "my_scenario"

    def test_colnames(self, data_file):
        """test that colnames are correct"""
        assert hasattr(data_file, "variable_list")
        assert len(data_file.variable_list) == 3
        assert len([var for var in data_file.variable_list if "[" in var]) == 0

    def test_set_get_var(self, data_file):
        """test that setting a var works"""
        assert data_file.current_var is None

        data_file.set_var("ti_by_commodity")
        assert isinstance(
            data_file.get_values(("INDIA", "TI_oceanic")),
            pd.Series)

        assert data_file.current_var == "ti_by_commodity"

        assert data_file.get_values(("INDIA", "Peru")) is None

        data_file.set_var("non_financial_corporations_financial_assets")
        assert isinstance(
            data_file.get_values(("AUSTRIA",)),
            pd.Series)

        assert data_file.current_var == \
            "non_financial_corporations_financial_assets"

        data_file.set_var("this var does not exist")
        assert data_file.get_values() is None

        assert data_file.current_var == "this var does not exist"
