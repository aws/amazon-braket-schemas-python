# Copyright 2019-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from typing import List

from pydantic import Field

from braket.device_schema.device_connectivity import DeviceConnectivity
from braket.device_schema.device_paradigm_properties_v1 import DeviceParadigmProperties
from braket.schema_common import BraketSchemaHeader


class IonqDeviceParadigmProperties(DeviceParadigmProperties):

    """
    This class defines the properties that are specific to ionq device

    Attributes:
        connectivity: defines the connectivity if a ionq device. tells the graph and connection type.
        qubitCount: number of qubits ionq device contains
        nativeGateSet: list of native gates

    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {
        ...        "name": "braket.device_schema.ionq_device_paradigm_properties",
        ...        "version": "1",
        ...    },
        ...    "qubitCount": 32,
        ...    "nativeGateSet": ["ccnot", "cy"],
        ...    "connectivity": {
        ...        "fullyConnected": True,
        ...        "connectivityGraph": {"1": ["2", "3"]},
        ...    },
        ... }
        >>> IonqDeviceParadigmProperties.parse_raw_schema(json.dumps(input_json))
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.ionq_device_paradigm_properties", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    connectivity: DeviceConnectivity
    qubitCount: int
    nativeGateSet: List[str]
