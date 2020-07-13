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

from braket.ir.annealing import ProblemType
from braket.task_result.annealing_task_result import AnnealingTaskResult


@pytest.fixture
def values():
    return [0.3, 1.0]


@pytest.fixture
def solutions():
    return [[1, 0], [1, 0]]


@pytest.fixture
def solution_counts():
    return [1, 2]


@pytest.fixture
def variable_count():
    return 5


@pytest.fixture
def problem_type():
    return ProblemType.QUBO


@pytest.mark.xfail(raises=ValidationError)
def test_missing_properties(braket_schema_header):
    AnnealingTaskResult(braketSchemaHeader=braket_schema_header)


def test_correct_result(
    braket_schema_header,
    task_metadata,
    additional_metadata_annealing,
    values,
    solutions,
    solution_counts,
    variable_count,
    problem_type,
):
    result = AnnealingTaskResult(
        braketSchemaHeader=braket_schema_header,
        values=values,
        solutions=solutions,
        solutionCounts=solution_counts,
        variableCount=variable_count,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_annealing,
        problemType=problem_type,
    )
    assert result.values == values
    assert result.solutions == solutions
    assert result.solutionCounts == solution_counts
    assert result.variableCount == variable_count
    assert result.taskMetadata == task_metadata
    assert result.additionalMetadata == additional_metadata_annealing
    assert result.problemType == problem_type
    assert AnnealingTaskResult.parse_raw(result.json()) == result


@pytest.mark.parametrize("solution_counts", [([-1], 2)])
@pytest.mark.xfail(raises=ValidationError)
def test_incorrect_solution_counts(
    braket_schema_header,
    task_metadata,
    additional_metadata_annealing,
    values,
    solutions,
    solution_counts,
    variable_count,
    problem_type,
):
    AnnealingTaskResult(
        braketSchemaHeader=braket_schema_header,
        values=values,
        solutions=solutions,
        solutionCounts=solution_counts,
        variableCount=variable_count,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_annealing,
        problemType=problem_type,
    )


@pytest.mark.parametrize("solutions", [(1), ([[]]), ([[-2]]), ([[500, 299]])])
@pytest.mark.xfail(raises=ValidationError)
def test_incorrect_solutions(
    braket_schema_header,
    task_metadata,
    additional_metadata_annealing,
    values,
    solutions,
    solution_counts,
    variable_count,
    problem_type,
):
    AnnealingTaskResult(
        braketSchemaHeader=braket_schema_header,
        values=values,
        solutions=solutions,
        solutionCounts=solution_counts,
        variableCount=variable_count,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_annealing,
        problemType=problem_type,
    )


@pytest.mark.parametrize("values", [(1), ([[]])])
@pytest.mark.xfail(raises=ValidationError)
def test_incorrect_values(
    braket_schema_header,
    task_metadata,
    additional_metadata_annealing,
    values,
    solutions,
    solution_counts,
    variable_count,
    problem_type,
):
    AnnealingTaskResult(
        braketSchemaHeader=braket_schema_header,
        values=values,
        solutions=solutions,
        solutionCounts=solution_counts,
        variableCount=variable_count,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_annealing,
        problemType=problem_type,
    )


@pytest.mark.parametrize("problem_type", [(-2), ("HELLO")])
@pytest.mark.xfail(raises=ValidationError)
def test_incorrect_problem_type(
    braket_schema_header,
    task_metadata,
    additional_metadata_annealing,
    values,
    solutions,
    solution_counts,
    variable_count,
    problem_type,
):
    AnnealingTaskResult(
        braketSchemaHeader=braket_schema_header,
        values=values,
        solutions=solutions,
        solutionCounts=solution_counts,
        variableCount=variable_count,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_annealing,
        problemType=problem_type,
    )


@pytest.mark.parametrize("variable_count", [(-2), ([[]])])
@pytest.mark.xfail(raises=ValidationError)
def test_incorrect_variable_count(
    braket_schema_header,
    task_metadata,
    additional_metadata_annealing,
    values,
    solutions,
    solution_counts,
    variable_count,
    problem_type,
):
    AnnealingTaskResult(
        braketSchemaHeader=braket_schema_header,
        values=values,
        solutions=solutions,
        solutionCounts=solution_counts,
        variableCount=variable_count,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_annealing,
        problemType=problem_type,
    )
