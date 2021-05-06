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

from typing import Optional, Union

from pydantic import BaseModel, confloat, conint, conlist, constr


class SingleTarget(BaseModel):
    """
    Single target index.

    Attributes:
        target (int): The target index. This is an int >= 0.

    Examples:
        >>> SingleTarget(target=0)
    """

    target: conint(ge=0)


class DoubleTarget(BaseModel):
    """
    Target indices of length 2.

    Attributes:
        targets (List[int]): A list with two items and all items are int >= 0.

    Examples:
        >>> DoubleTarget(targets=[0, 1])
    """

    targets: conlist(conint(ge=0), min_items=2, max_items=2)


class MultiTarget(BaseModel):
    """
    Variable length target indices.

    Attributes:
        targets (List[int]): A list with items that are all int >= 0.

    Examples:
        >>> MultiTarget(targets=[0, 1])
    """

    targets: conlist(conint(ge=0), min_items=1)


class OptionalMultiTarget(BaseModel):
    """
    Optional variable length target indices

    Attributes:
        targets (Optional[List[int]]): A list with items that are all int >= 0.

    Examples:
        >>> OptionalMultiTarget(targets=[0, 1])
    """

    targets: Optional[conlist(conint(ge=0), min_items=1)]


class MultiControl(BaseModel):
    """
    Variable length control indices.

    Attributes:
        controls (List[int]): A list with at least two items and all items are int >= 0.

    Examples:
        >>> MultiControl(controls=[0, 1])
    """

    controls: conlist(conint(ge=0), min_items=1)


class DoubleControl(BaseModel):
    """
    Control indices of length 2.

    Attributes:
        controls (List[int]): A list with two items and all items are int >= 0.

    Examples:
        >>> DoubleControl(targets=[0, 1])
    """

    controls: conlist(conint(ge=0), min_items=2, max_items=2)


class SingleControl(BaseModel):
    """
    Single control index.

    Attributes:
        control (int): The control index. This is an int >= 0.

    Examples:
        >>> SingleControl(control=0)
    """

    control: conint(ge=0)


class Angle(BaseModel):
    """
    Single angle in radians (floating point).

    Attributes:
        angle (float): The angle in radians.
            inf, -inf, and NaN are not allowable inputs.

    Examples:
        >>> Angle(angle=0.15)
    """

    angle: confloat(gt=float("-inf"), lt=float("inf"))


class SingleProbability(BaseModel):
    """
    A single probability parameter for a general noise channel.

    Attributes:
        probability (float): The probability for noise channel.
            NaN is not an allowable input.

    Examples:
        >>> SingleProbability(probability=0.9)
    """

    probability: confloat(ge=float("0.0"), le=float("1.0"))


class DampingProbability(BaseModel):
    """
    The parameter for the amplitude/phase damping channel

    Attributes:
        gamma (float): The probability of damping

    Examples:
        >>> DampingProbability(gamma=0.1)
    """

    gamma: confloat(ge=float("0.0"), le=float("1.0"))


class TripleProbability(BaseModel):
    """
    A triple-probability parameter set for the general Pauli noise channel.

    Attributes:
        probX (float), probY (float), probZ (float): The coefficients of the
        general Pauli channel

    Examples:
        >>> TripleProbability(probX=0.1, probY=0.2, probZ=0.3)
    """

    probX: confloat(ge=float("0.0"), le=float("1.0"))
    probY: confloat(ge=float("0.0"), le=float("1.0"))
    probZ: confloat(ge=float("0.0"), le=float("1.0"))


class TwoDimensionalMatrix(BaseModel):
    """
    Two-dimensional non-empty matrix.

    Attributes:
        matrix (List[List[List[float]]]): Two-dimensional matrix with complex entries.
            Each complex number is represented using a List[float] of size 2, with
            element[0] being the real part and element[1] imaginary.
            inf, -inf, and NaN are not allowable inputs for the element.

    Examples:
        >>> TwoDimensionalMatrix(matrix=[[[0, 0], [1, 0]], [[1, 0], [0, 0]]])
    """

    matrix: conlist(
        conlist(
            conlist(confloat(gt=float("-inf"), lt=float("inf")), min_items=2, max_items=2),
            min_items=1,
        ),
        min_items=1,
    )


class TwoDimensionalMatrixList(BaseModel):
    """
    List of two-dimensional non-empty matrices.

    Attributes:
        matrix (List[List[List[List[float]]]]): Two-dimensional matrix with complex entries.
            Each complex number is represented using a List[float] of size 2, with
            element[0] being the real part and element[1] imaginary.
            inf, -inf, and NaN are not allowable inputs for the element.
            The number of matrices is limited to 16 and the size of each matrix is limited to 4*4.

    Examples:
        >>> TwoDimensionalMatrixList(matrices=[[[[1, 0], [0, 0]], [[0, 0], [1, 0]]],
                                               [[[0, 0], [1, 0]], [[1, 0], [0, 0]]]
                                              ]
                                    )
    """

    matrices: conlist(
        conlist(
            conlist(
                conlist(confloat(gt=float("-inf"), lt=float("inf")), min_items=2, max_items=2),
                min_items=1,
                max_items=4,
            ),
            min_items=1,
            max_items=4,
        ),
        min_items=1,
        max_items=16,
    )


class Observable(BaseModel):
    """
    An observable. If given list is more than one element, this is the tensor product
    of each operator in the list.

    Attributes:
        observable (List[Union[str, List[List[List[float]]]]): A list with at least
            one item and items are strings matching the observable regex
            or a two-dimensional hermitian matrix with complex entries.
            Each complex number is represented using a List[float] of size 2, with
            element[0] being the real part and element[1] imaginary.
            inf, -inf, and NaN are not allowable inputs for the element.

    Examples:
        >>> Observable(observable=["x"])
        >>> Observable(observable=[[[0, 0], [1, 0]], [[1, 0], [0, 0]]])
    """

    observable: conlist(
        Union[
            constr(regex="(x|y|z|h|i)"),
            conlist(
                conlist(
                    conlist(confloat(gt=float("-inf"), lt=float("inf")), min_items=2, max_items=2),
                    min_items=2,
                ),
                min_items=2,
            ),
        ],
        min_items=1,
    )


class MultiState(BaseModel):
    """
    A list of states in bitstring form.

    Attributes:
        states (List[string]): Variable length list with all strings matching the
            state regex

    Examples:
        >>> lMultiState(states=["10", "10"])
    """

    states: conlist(constr(regex="^[01]+$", min_length=1), min_items=1)
