"""
Module energy.end_use.transport.railway_tracks
Translated using PySD version 3.10.0
"""


@component.add(
    name="initial_railway_catenary_length",
    units="km",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_railway_tracks_length": 1,
        "share_electrified_rails_vs_train_activity": 1,
    },
)
def initial_railway_catenary_length():
    """
    initial length of railway catenary
    """
    return initial_railway_tracks_length() * share_electrified_rails_vs_train_activity()


@component.add(
    name="new_railway_catenary",
    units="km/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "required_catenary_length": 1,
        "railway_catenary_length": 1,
        "one_year": 1,
    },
)
def new_railway_catenary():
    """
    new km of railway catenary
    """
    return (required_catenary_length() - railway_catenary_length()) / one_year()


@component.add(
    name="new_railway_tracks",
    units="km/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "required_railway_tracks_length": 2,
        "railway_tracks_length": 2,
        "one_year": 1,
    },
)
def new_railway_tracks():
    """
    new km of railway tracks
    """
    return (
        if_then_else(
            required_railway_tracks_length() - railway_tracks_length() < 0,
            lambda: xr.DataArray(
                0, {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]}, ["REGIONS_35_I"]
            ),
            lambda: required_railway_tracks_length() - railway_tracks_length(),
        )
        / one_year()
    )


@component.add(
    name="railway_catenary_length",
    units="km",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_railway_catenary_length": 1},
    other_deps={
        "_integ_railway_catenary_length": {
            "initial": {"initial_railway_catenary_length": 1},
            "step": {"new_railway_catenary": 1, "wear_railways_catenary": 1},
        }
    },
)
def railway_catenary_length():
    """
    railway catenary km length
    """
    return _integ_railway_catenary_length()


_integ_railway_catenary_length = Integ(
    lambda: new_railway_catenary() - wear_railways_catenary(),
    lambda: initial_railway_catenary_length(),
    "_integ_railway_catenary_length",
)


@component.add(
    name="railway_tracks_length",
    units="km",
    subscripts=["REGIONS_35_I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_railway_tracks_length": 1},
    other_deps={
        "_integ_railway_tracks_length": {
            "initial": {"initial_railway_tracks_length": 1},
            "step": {
                "new_railway_tracks": 1,
                "replacement_railway_lines_length": 1,
                "wear_railway_tracks": 1,
            },
        }
    },
)
def railway_tracks_length():
    """
    railway tracks km length
    """
    return _integ_railway_tracks_length()


_integ_railway_tracks_length = Integ(
    lambda: new_railway_tracks()
    + replacement_railway_lines_length()
    - wear_railway_tracks(),
    lambda: xr.DataArray(
        initial_railway_tracks_length(),
        {"REGIONS_35_I": _subscript_dict["REGIONS_35_I"]},
        ["REGIONS_35_I"],
    ),
    "_integ_railway_tracks_length",
)


@component.add(
    name="reestimate_share_train_elec_vs_total_train",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"public_passenger_vehicle_fleet": 2},
)
def reestimate_share_train_elec_vs_total_train():
    """
    percents train over 1.
    """
    return zidz(
        sum(
            public_passenger_vehicle_fleet()
            .loc[:, "EV", "RAIL", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        ),
        sum(
            public_passenger_vehicle_fleet()
            .loc[:, :, "RAIL", :]
            .reset_coords(drop=True)
            .rename(
                {
                    "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                    "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
                }
            ),
            dim=["TRANSPORT_POWER_TRAIN_I!", "HOUSEHOLDS_I!"],
        ),
    )


@component.add(
    name="replacement_railway_lines_length",
    units="km/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"wear_railway_tracks": 1},
)
def replacement_railway_lines_length():
    """
    km replaced of railway tracks
    """
    return wear_railway_tracks() * 0


@component.add(
    name="required_catenary_length",
    units="km",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "railway_tracks_length": 1,
        "share_electrified_rails_vs_train_activity": 1,
    },
)
def required_catenary_length():
    """
    km of railway catenary required
    """
    return railway_tracks_length() * share_electrified_rails_vs_train_activity()


@component.add(
    name="required_railway_tracks_length",
    units="km",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_number_trains": 1,
        "total_length_rail_tracks_vs_lines_historic": 1,
        "length_railway_lines_per_locomotive_historic": 1,
    },
)
def required_railway_tracks_length():
    """
    km of railway tracks required
    """
    return (
        total_number_trains()
        * total_length_rail_tracks_vs_lines_historic()
        * length_railway_lines_per_locomotive_historic()
    )


@component.add(
    name="share_electrified_rails_vs_train_activity",
    units="DMNL",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "reestimate_share_train_elec_vs_total_train": 1,
        "passenger_transport_demand_public_fleet": 2,
    },
)
def share_electrified_rails_vs_train_activity():
    """
    COEFFICIENT_EQUATION_ELECTRIFIED_CONSTANT_A*(reestimate_share_train_elec_vs_total_tra in[REGIONS 35 I])^2+COEFFICIENT_EQUATION_ELECTRIFIED_CONSTANT_B *reestimate_share_train_elec_vs_total_train[REGIONS 35 I] Ratio between combustion and electric train activity. On a graph with x-axis representing the world train activity (/1) and y-axis representing the world percentage of electrified rails (/1). Equation of the parabola joining the points (0.0) and (1.1) through the point (0.5.0.27). 50% of the railway activity is carried out on the 27% of rails that are electrified.
    """
    return zidz(
        reestimate_share_train_elec_vs_total_train()
        * sum(
            passenger_transport_demand_public_fleet()
            .loc[:, "RAIL", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["HOUSEHOLDS_I!"],
        ),
        sum(
            passenger_transport_demand_public_fleet()
            .loc[:, "RAIL", :]
            .reset_coords(drop=True)
            .rename({"REGIONS_35_I": "REGIONS_35_I!", "HOUSEHOLDS_I": "HOUSEHOLDS_I!"}),
            dim=["REGIONS_35_I!", "HOUSEHOLDS_I!"],
        ),
    )


@component.add(
    name="total_number_trains",
    units="locomotives",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"public_passenger_vehicle_fleet": 1},
)
def total_number_trains():
    """
    Total number of locomotives
    """
    return sum(
        public_passenger_vehicle_fleet()
        .loc[:, :, "RAIL", :]
        .reset_coords(drop=True)
        .rename(
            {
                "TRANSPORT_POWER_TRAIN_I": "TRANSPORT_POWER_TRAIN_I!",
                "HOUSEHOLDS_I": "HOUSEHOLDS_I!",
            }
        ),
        dim=["TRANSPORT_POWER_TRAIN_I!", "HOUSEHOLDS_I!"],
    )


@component.add(
    name="wear_railway_tracks",
    units="km/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"railway_tracks_length": 1, "lifetime_railway_tracks": 1},
)
def wear_railway_tracks():
    """
    wear km of railway tracks
    """
    return railway_tracks_length() / lifetime_railway_tracks()


@component.add(
    name="wear_railways_catenary",
    units="km/Year",
    subscripts=["REGIONS_35_I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"railway_catenary_length": 1, "lifetime_railway_catenary": 1},
)
def wear_railways_catenary():
    """
    wear km of railway catenary
    """
    return railway_catenary_length() / lifetime_railway_catenary()
