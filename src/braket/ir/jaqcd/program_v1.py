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

from typing import Any, List, Optional, Union

from pydantic import Field, validator

from braket.ir.jaqcd.instructions import (
    CY,
    CZ,
    XX,
    XY,
    YY,
    ZZ,
    CCNot,
    CNot,
    CPhaseShift,
    CPhaseShift00,
    CPhaseShift01,
    CPhaseShift10,
    CSwap,
    H,
    I,
    ISwap,
    PhaseShift,
    PSwap,
    Rx,
    Ry,
    Rz,
    S,
    Si,
    Swap,
    T,
    Ti,
    Unitary,
    V,
    Vi,
    X,
    Y,
    Z,
)
from braket.ir.jaqcd.results import (
    Amplitude,
    Expectation,
    Probability,
    Sample,
    StateVector,
    Variance,
)
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader

"""
We need a constant lookup for our pydantic validator. Using a plain Union[] will result
in an O(n) lookup for arbitrary payloads, having a negative impact on model creation times.
"""
_valid_gates = {
    CCNot.Type.ccnot: CCNot,
    CNot.Type.cnot: CNot,
    CPhaseShift.Type.cphaseshift: CPhaseShift,
    CPhaseShift00.Type.cphaseshift00: CPhaseShift00,
    CPhaseShift01.Type.cphaseshift01: CPhaseShift01,
    CPhaseShift10.Type.cphaseshift10: CPhaseShift10,
    CSwap.Type.cswap: CSwap,
    CY.Type.cy: CY,
    CZ.Type.cz: CZ,
    H.Type.h: H,
    I.Type.i: I,
    ISwap.Type.iswap: ISwap,
    PhaseShift.Type.phaseshift: PhaseShift,
    PSwap.Type.pswap: PSwap,
    Rx.Type.rx: Rx,
    Ry.Type.ry: Ry,
    Rz.Type.rz: Rz,
    S.Type.s: S,
    Swap.Type.swap: Swap,
    Si.Type.si: Si,
    T.Type.t: T,
    Ti.Type.ti: Ti,
    Unitary.Type.unitary: Unitary,
    V.Type.v: V,
    Vi.Type.vi: Vi,
    X.Type.x: X,
    XX.Type.xx: XX,
    XY.Type.xy: XY,
    Y.Type.y: Y,
    YY.Type.yy: YY,
    Z.Type.z: Z,
    ZZ.Type.zz: ZZ,
}

Results = Union[Amplitude, Expectation, Probability, Sample, StateVector, Variance]


class Program(BraketSchemaBase):
    """
    Root object of the JsonAwsQuantumCircuitDescription IR.



    Attributes:
        braketSchemaHeader (BraketSchemaHeader): Schema header. Users do not need
            to set this value. Only default is allowed.
        instructions (List[GateInstructions]): List of instructions.
        basis_rotation_instructions (List[GateInstructions]): List of instructions for
            rotation to desired measurement bases. Default is None.
        results (List[Union[Amplitude, Expectation, Probability, Sample, StateVector, Variance]]):
            List of requested results. Default is None.

    Examples:
        >>> Program(instructions=[H(target=0), Rz(angle=0.15, target=1)])
        >>> Program(instructions=[H(target=0), CNot(control=0, target=1)],
        ...     results=[Expectation(targets=[0], observable=['x'])],
        ...     basis_rotation_instructions=[H(target=0)])


    Note:
        The type `GateInstructions` includes the following instructions:
        CCNot,
        CNot,
        CPhaseShift,
        CPhaseShift00,
        CPhaseShift01,
        CPhaseShift10,
        CSwap,
        CY,
        CZ,
        H,
        I,
        ISwap,
        PhaseShift,
        PSwap,
        Rx,
        Ry,
        Rz,
        S,
        Swap,
        Si,
        T,
        Ti,
        Unitary,
        V,
        Vi,
        X,
        XX,
        XY,
        Y,
        YY,
        Z,
        ZZ
    """

    _PROGRAM_HEADER = BraketSchemaHeader(name="braket.ir.jaqcd.program", version="1")
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    instructions: List[Any]
    results: Optional[List[Results]]
    basis_rotation_instructions: Optional[List[Any]]

    @validator("instructions", "basis_rotation_instructions", each_item=True, pre=True)
    def validate_instructions(cls, value, field):
        """
        Pydantic uses the validation subsystem to create objects. We use this custom validator for
        2 reasons:
        1. Implement O(1) deserialization
        2. Validate that the input instructions are supported
        """
        if value is not None and "type" in value and value["type"] not in _valid_gates:
            raise ValueError(f"Invalid gate specified: {value} for field: {field}")
        return _valid_gates[value["type"]](**value)
