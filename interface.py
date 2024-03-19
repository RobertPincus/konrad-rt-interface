import numpy as np
import xarray as xr


class RadiationLW:
    def __init__(self, lookup_table=None, **kwargs):
        """Initialize the radiatiove transfer model."""
        # The signature of this method will likely differ for various models.
        return

    def compute_fluxes(self, atmosphere, surface):
        fluxes = xr.Dataset(
            coords={
                "level": atmosphere.level,
            },
            data_vars={
                "flux_up": (("level",), np.ones(atmosphere.sizes["level"])),
                "flux_down": (("level",), -1 * np.ones(atmosphere.sizes["level"])),
            },
        )

        return fluxes


class RadiationSW:
    def __init__(self, lookup_table=None, **kwargs):
        return

    def compute_fluxes(self, atmosphere, surface, geometry=None):
        # I think that the sun geometry needs to be passed here.
        fluxes = xr.Dataset(
            coords={
                "level": atmosphere.level,
            },
            data_vars={
                "flux_up": (("level",), np.ones(atmosphere.sizes["level"])),
                "flux_down": (("level",), -1 * np.ones(atmosphere.sizes["level"])),
            },
        )

        return fluxes


# Define the atmospheric state
nlev = 101
atmosphere = xr.Dataset(
    coords={
        "level": np.arange(nlev),
        "layer": np.arange(nlev - 1),
    },
    data_vars={
        "T": (("level"), 300 * np.ones(nlev)),
        "p": (("level"), np.linspace(1000e3, 1, nlev)),
        "N2": 0.78084,
        "O2": 0.20946,
        "H2O": (("level"), np.linspace(0.02, 0, nlev)),
        "CO2": 348e-6,
    },
)

# Define the surface state
surface = xr.Dataset(
    coords={
        "wavenumber": np.arange(1),
    },
    data_vars={
        "T": 300,
        "albedo": 0.07,
        "emissivity": 1.0,
    },
)


# This could also be a class that allows to transform between coordinates (maybe too much at this point)
geometry = xr.Dataset(
    data_vars={
        "zenith_angle": 45.0,
        "total_solar_irradiance": 345.0,
    },
)


radiation_lw = RadiationLW()
radiation_lw.compute_fluxes(atmosphere, surface)

radiation_sw = RadiationSW()
radiation_sw.compute_fluxes(atmosphere, surface)
