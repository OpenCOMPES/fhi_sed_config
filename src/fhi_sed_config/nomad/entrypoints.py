#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Entry points for fhi sed config and templates."""

try:
    from nomad.config.models.plugins import ExampleUploadEntryPoint, UploadResource
except ImportError as exc:
    raise ImportError(
        "Could not import nomad package. Please install the package 'nomad-lab'.",
    ) from exc

resources = [
    "Metis/Bin_scan_to_NeXus.ipynb",
    "Metis/Cleanup_Scratch.ipynb",
    "Metis/Generate_calibration_parameters.ipynb",
    "Metis/Scan_diagnostics.ipynb",
    "Phoibos/Save_scan_to_NeXus.ipynb",
    "Phoibos/Setup_Parameters.ipynb",
    "Phoibos/config_doublepump.yaml",
]

fhi_sed_config = ExampleUploadEntryPoint(
    title="Conversion template for FHI Metis and Phoibos data",
    category="Templates",
    description="""
        This template contains configurations and template notebooks for
        converting data from the FHI trARPES lab to Nexus.
    """,
    plugin_package="fhi_sed_config",
    # Include a file/folder into a specific location within the upload
    resources=[
        UploadResource(
            path="https://raw.githubusercontent.com/OpenCOMPES/fhi_sed_config/refs/heads/main/templates/"
            + resource,
            target=resource,
        )
        for resource in resources
    ],
)
