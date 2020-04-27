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
from braket.ir.jaqcd import CNot, Expectation, H, Program
from pydantic import ValidationError


@pytest.mark.xfail(raises=ValidationError)
def test_missing_instructions_property():
    Program()


@pytest.mark.xfail(raises=ValidationError)
def test_non_instruction():
    Program(instructions=["foo"])


@pytest.mark.xfail(raises=ValidationError)
def test_partial_non_instruction():
    Program(instructions=[CNot(control=0, target=1), "foo"])


@pytest.mark.xfail(raises=ValidationError)
def test_partial_non_result():
    Program(
        instructions=[CNot(control=0, target=1)],
        results=[Expectation(targets=[1], observable=["x"]), CNot(control=0, target=1)],
    )


def test_instruction_no_results():
    Program(instructions=[CNot(control=0, target=1)])


def test_instruction_with_results():
    Program(
        instructions=[CNot(control=0, target=1)],
        results=[Expectation(targets=[1], observable=["x"])],
    )


@pytest.mark.xfail(raises=ValidationError)
def test_partial_non_rotation_basis_instruction():
    Program(
        instructions=[CNot(control=0, target=1)],
        basis_rotation_instructions=[Expectation(targets=[1], observable=["x"]), H(target=1)],
    )


def test_no_rotation_basis_instruction():
    Program(instructions=[CNot(control=0, target=1)],)


def test_rotation_basis_instruction():
    Program(instructions=[CNot(control=0, target=1)], basis_rotation_instructions=[H(target=1)])