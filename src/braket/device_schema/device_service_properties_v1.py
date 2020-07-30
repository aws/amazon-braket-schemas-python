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

from typing import List, Optional, Tuple

from pydantic import BaseModel, Field

from braket.device_schema.device_execution_window import DeviceExecutionWindow
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class DeviceCost(BaseModel):

    """
    This class provides the details on the cost of a device.

    Attributes:
        price: Price of the device in terms of US $
        unit: unit for charging the price, eg: minute, hour, task [price per task]

    Examples:
        >>> import json
        >>> input_json = {
        ...     "price": 0.25,
        ...     "unit": "minute"
        ... }
        >>> DeviceCost.parse_raw(json.dumps(input_json))
    """

    price: float
    unit: str


class DeviceDocumentation(BaseModel):
    """
    This class provides the device metadata like image, summary of it and external documentation.

    Attributes:
        imageUrl: url for the image of the device
        summary: brief description on the device
        externalDocumentationLink: link to provide any useful information to the users.

    Examples:
        >>> import json
        >>> input_json = {
        ...     "imageUrl": "image_url",
        ...     "summary": "Summary on the device",
        ...     "externalDocumentationUrl": "exter doc link",
        ... }
        >>> DeviceDocumentation.parse_raw(json.dumps(input_json))
    """

    imageUrl: Optional[str]
    summary: Optional[str]
    externalDocumentationUrl: Optional[str]


class DeviceServiceProperties(BraketSchemaBase):
    """
    This class defines the common service properties for each device.

    Attributes:
        executionWindows: List of the executionWindows, it tells us which days the device can
            execute a task.
        shotsRange: range of the shots for a given device.

    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {
        ...        "name": "braket.device_schema.device_service_properties",
        ...        "version": "1",
        ...    },
        ...    "executionWindows": [
        ...        {
        ...            "executionDay": "Everyday",
        ...            "windowStartHour": "1966280412345.6789",
        ...            "windowEndHour": "1966280414345.6789",
        ...        }
        ...    ],
        ...    "shotsRange": [1,10],
        ...    "deviceCost": {
        ...        "price": 0.25,
        ...        "unit": "minute"
        ...    },
        ...    "deviceDocumentation": {
        ...        "imageUrl": "image_url",
        ...        "summary": "Summary on the device",
        ...        "externalDocumentationUrl": "exter doc link",
        ...    },
        ...    "deviceLocation": "us-east-1"
        ... }
        >>> DeviceServiceProperties.parse_raw_schema(json.dumps(input_json))

    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.device_service_properties", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    executionWindows: List[DeviceExecutionWindow]
    shotsRange: Tuple[int, int]
    deviceCost: Optional[DeviceCost]
    deviceDocumentation: Optional[DeviceDocumentation]
    deviceLocation: Optional[str]
