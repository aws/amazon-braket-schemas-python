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

import json
import pdb

import pytest
from pydantic import ValidationError

from braket.device_schema.ion_q_device_capabilities_v1 import IonQDeviceCapabilities


@pytest.fixture(scope="module")
def valid_input():
    input = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.ion_q_device_capabilities",
            "version": "1",
        },
        "service": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.device_service_properties",
                "version": "1",
            },
            "executionWindows": [
                {
                    "braketSchemaHeader": {
                        "name": "braket.device_schema.device_execution_window",
                        "version": "1",
                    },
                    "executionDay": "Everyday",
                    "windowStartHour": "1966280412345.6789",
                    "windowEndHour": "1966280414345.6789",
                }
            ],
            "shots": 2,
        },
        "action": {
            "braket.ir.jaqcd.program": {
                "braketSchemaHeader": {
                    "name": "braket.device_schema.jaqcd_device_action_properties",
                    "version": "1",
                },
                "actionType": "braket.ir.jaqcd.program",
                "version": ["1.0", "1.1"],
                "supportedOperations": [{"control": 0, "target": 1, "type": "cnot"}],
                "supportedResultTypes": [
                    {"observable": ["x"], "targets": [1], "type": "expectation"}
                ],
            }
        },
        "paradigm": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.ion_q_device_paradigm_properties",
                "version": "1",
            },
            "qubitCount": 11,
            "nativeGateSet": ["ccnot", "cy"],
            "connectivity": {
                "braketSchemaHeader": {
                    "name": "braket.device_schema.device_connectivity",
                    "version": "1",
                },
                "fullyConnected": True,
                "connectivityGraph": {"1": ["2", "3"]},
            },
        },
        "deviceParameters": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.ion_q_device_parameters",
                "version": "1",
            },
            "qubitCount": 11,
        },
    }
    return input


def test_valid(valid_input):
    result = IonQDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))
    assert result.braketSchemaHeader.name == "braket.device_schema.ion_q_device_capabilities"


@pytest.mark.xfail(raises=ValidationError)
def test__missing_schemaHeader(valid_input):
    valid_input.pop("braketSchemaHeader")
    IonQDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_paradigm(valid_input):
    valid_input.pop("paradigm")
    IonQDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_deviceParameters(valid_input):
    valid_input.pop("deviceParameters")
    IonQDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_action(valid_input):
    valid_input.pop("action")
    IonQDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_service(valid_input):
    valid_input.pop("service")
    IonQDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))
