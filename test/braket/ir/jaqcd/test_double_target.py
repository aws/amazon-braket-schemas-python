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

from braket.ir.jaqcd.shared_models import DoubleTarget


@pytest.mark.xfail(raises=ValidationError)
def test_missing_targets():
    DoubleTarget()


@pytest.mark.xfail(raises=ValidationError)
def test_list_partial_non_int():
    DoubleTarget(targets=[0, "foo"])


@pytest.mark.xfail(raises=ValidationError)
def test_list_lt_zero():
    DoubleTarget(targets=[-1, -2])


@pytest.mark.xfail(raises=ValidationError)
def test_list_partial_lt_zero():
    DoubleTarget(targets=[0, -1])


@pytest.mark.xfail(raises=ValidationError)
def test_empty_list():
    DoubleTarget(targets=[])


@pytest.mark.xfail(raises=ValidationError)
def test_list_of_1():
    DoubleTarget(targets=[1])


@pytest.mark.xfail(raises=ValidationError)
def test_list_of_3():
    DoubleTarget(targets=[1, 2, 3])


def test_list_gte_zero():
    targets = [0, 1]
    obj = DoubleTarget(targets=targets)
    assert obj.targets == targets


def test_list_extra_params():
    DoubleTarget(targets=[0, 1], foo="bar")
