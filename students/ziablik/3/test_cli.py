# -*- coding: utf-8 -*-

import subprocess   # noqa: S404

from cli import contains_execution, ls_execution    # noqa I001
from cli import mk_execution, rm_execution, since_execution # noqa I001


def test_ls_execution(ls_fixture):
    """Tests for ls command."""
    assert ls_execution(ls_fixture[0]) == ls_fixture[1]


def test_mk_execution(mk_fixture):
    """Tests for mk command."""
    assert mk_execution(mk_fixture[0]) == mk_fixture[1]


def test_rm_execution(rm_fixture):
    """Tests for rm command."""
    assert rm_execution(rm_fixture[0]) == rm_fixture[1]


def test_contains_execution(contains_fixture):
    """Tests for contains command."""
    assert contains_execution(contains_fixture[0]) == contains_fixture[1]


def test_since_execution(since_fixture):
    """Tests for since command."""
    assert since_execution(
        since_fixture[0],
        since_fixture[1],
    ) == since_fixture[2]


def test_integration(integration_fixture):
    """Integration Tests."""
    command, args = integration_fixture
    callable_string = 'python cli.py {0} {1}'.format(command, args)
    assert subprocess.call(callable_string) == 0    # noqa: S602
