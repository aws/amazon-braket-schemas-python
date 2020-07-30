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

from typing import Dict

from pydantic import Field

from braket.device_schema.device_action_properties import DeviceActionType
from braket.device_schema.device_capabilities import DeviceCapabilities
from braket.device_schema.gate_model_qpu_paradigm_properties_v1 import (
    GateModelQpuParadigmProperties,
)
from braket.device_schema.ionq.ionq_device_parameters_v1 import IonqDeviceParameters
from braket.device_schema.jaqcd_device_action_properties import JaqcdDeviceActionProperties
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class IonqDeviceCapabilities(BraketSchemaBase, DeviceCapabilities):

    """
    This defines the capabilities of a Ion-Q device.

    Attributes:
        action: Actions that a Ion-Q device can support
        paradigm: Paradigm properties of a Ion-Q

    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {
        ...        "name": "braket.device_schema.ionq.ionq_device_capabilities",
        ...        "version": "1",
        ...    },
        ...    "service": {
        ...        "braketSchemaHeader": {
        ...            "name": "braket.device_schema.device_service_properties",
        ...            "version": "1",
        ...        },
        ...        "executionWindows": [
        ...            {
        ...                "executionDay": "Everyday",
        ...                "windowStartHour": "1966280412345.6789",
        ...                "windowEndHour": "1966280414345.6789",
        ...            }
        ...        ],
        ...        "shotsRange": [1, 10],
        ...    },
        ...    "action": {
        ...        "braket.ir.jaqcd.program": {
        ...            "actionType": "braket.ir.jaqcd.program",
        ...            "version": ["1.0", "1.1"],
        ...            "supportedOperations": ["x", "y"],
        ...            "supportedResultTypes": [{
        ...                 "name": "resultType1",
        ...                 "observables": ["observable1"],
        ...                 "minShots": 2,
        ...                 "maxShots": 4,
        ...             }],
        ...        }
        ...    },
        ...    "paradigm": {
        ...        "braketSchemaHeader": {
        ...            "name": "braket.device_schema.gate_model_qpu_paradigm_properties",
        ...            "version": "1",
        ...        },
        ...        "qubitCount": 11,
        ...        "nativeGateSet": ["ccnot", "cy"],
        ...        "connectivity": {
        ...            "fullyConnected": False,
        ...            "connectivityGraph": {"1": ["2", "3"]},
        ...        },
        ...    },
        ...    "deviceParameters": {IonqDeviceParameters.schema_json()},
        ...    "device" : {
        ...         "supportedRegions": ["IAD"],
        ...         "deviceCost": [10, "task"],
        ...         "deviceMetadata": "metadata of the device",
        ...         "deviceLocation": "IAD",
        ...         "summary": "details of the device",
        ...         "externalDocumentation": "details to external doc",
        ...     }
        ... }
        >>> IonqDeviceCapabilities.parse_raw_schema(json.dumps(input_json))
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.ionq.ionq_device_capabilities", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    action: Dict[DeviceActionType, JaqcdDeviceActionProperties]
    paradigm: GateModelQpuParadigmProperties
