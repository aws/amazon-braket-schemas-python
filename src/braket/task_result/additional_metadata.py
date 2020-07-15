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
# language governing permissions and limitations under the License

from typing import Optional, Union

from pydantic import BaseModel

from braket.ir.annealing import Problem
from braket.ir.jaqcd import Program
from braket.task_result.dwave_metadata_v1 import DwaveMetadata


class AdditionalMetadata(BaseModel):
    """
    The additional metadata result schema.

    Attributes:
        action (Union[Program, Problem]): The action of the task
        dWaveMetadata (DWaveMetadata): Additional metadata for tasks that ran on D-Wave.
            Default is None.

    Examples:
        >>> AdditionalMetadata(action=Program(instructions=[CNot(control=0, target=1)]))

    """

    action: Union[Program, Problem]
    dwaveMetadata: Optional[DwaveMetadata]
