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

import pytest
from pydantic import ValidationError

from braket.device_schema.simulator_device_parameters_v1 import SimulatorDeviceParameters


def test_valid():
    input = (
        '{"braketSchemaHeader": {"name": "braket.device_schema.simulator_device_parameters", '
        '"version": "1"}, "qubitCount": 30} '
    )
    result = SimulatorDeviceParameters.parse_raw_schema(input)
    assert result.qubitCount == 30


@pytest.mark.xfail(raises=ValidationError)
def test_missing_schemaHeader():
    input = {"qubitCount": 1}
    assert SimulatorDeviceParameters.parse_raw_schema(input)


@pytest.mark.xfail(raises=ValidationError)
def test_missing_qubitCount():
    input = (
        '{"braketSchemaHeader": {"name": "braket.device_schema.simulator_device_parameters", '
        '"version": "1"}} '
    )
    assert SimulatorDeviceParameters.parse_raw_schema(input)


@pytest.mark.xfail(raises=ValidationError)
def test_invalid_qubitCount():
    input = (
        '{"braketSchemaHeader": {"name": "braket.device_schema.simulator_device_parameters", '
        '"version": "1"}, "qubitCount": 32} '
    )
    SimulatorDeviceParameters.parse_raw_schema(input)
