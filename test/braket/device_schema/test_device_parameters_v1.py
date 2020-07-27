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

from braket.device_schema.device_parameters_v1 import DeviceParameters


@pytest.fixture(scope="module")
def valid_gate_model_input():
    input = {
        "braketSchemaHeader": {"name": "braket.device_schema.device_parameters", "version": "1",},
        "deviceParameters": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.gate_model_parameters",
                "version": "1",
            }
        },
    }
    return input


@pytest.fixture(scope="module")
def valid_annealing_model_input():
    input = {
        "braketSchemaHeader": {"name": "braket.device_schema.device_parameters", "version": "1",},
        "deviceParameters": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.annealing_model_parameters",
                "version": "1",
            },
            "dWaveParameters": {
                "braketSchemaHeader": {
                    "name": "braket.device_schema.d_wave_parameters",
                    "version": "1",
                }
            },
        },
    }
    return input


def test_valid_gate_model(valid_gate_model_input):
    result = DeviceParameters.parse_raw_schema(json.dumps(valid_gate_model_input))
    assert result.braketSchemaHeader.name == "braket.device_schema.device_parameters"


def test_valid_annealing_model(valid_annealing_model_input):
    result = DeviceParameters.parse_raw_schema(json.dumps(valid_annealing_model_input))
    assert result.braketSchemaHeader.name == "braket.device_schema.device_parameters"


@pytest.mark.xfail(raises=ValidationError)
def test__missing_schemaHeader(valid_gate_model_input):
    valid_gate_model_input.pop("braketSchemaHeader")
    DeviceParameters.parse_raw_schema(json.dumps(valid_gate_model_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_both_model(valid_gate_model_input):
    valid_gate_model_input["deviceParameters"] = []
    DeviceParameters.parse_raw_schema(json.dumps(valid_gate_model_input))
