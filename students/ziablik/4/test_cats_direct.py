# -*- coding: utf-8 -*-

import os
import shutil
import subprocess  # noqa S404
import unittest

import pytest

import cats_direct


class CatsDirectTester(unittest.TestCase):
    """Tests for cats_direct."""

    def setUp(self) -> None:
        """Set Up of test."""
        self.simple_of_cats_fact = 'cats are cats'

        if not os.path.exists('temp'):
            os.mkdir('temp')

        self.test_fact_file = 'temp/cat_1_fact.txt'
        self.test_image = 'students/ziablik/4/image.jpg'
        self.result_image = 'temp/cat_1_image.jpg'

    def tearDown(self):
        """Tear Down of test."""
        shutil.rmtree('temp')

    def test_parser(self):
        """Create_parser function test."""
        args = ['--count', '1']
        parsed = cats_direct.create_parser().parse_args(args)
        assert parsed.count == int(args[-1])

    @pytest.mark.remote_data
    def test_fetch_cat_fact(self):
        """Fetch_cat_fact function test."""
        fact = cats_direct.fetch_cat_fact()
        assert fact != ''

    @pytest.mark.remote_data
    def test_fetch_cat_image(self):
        """Fetch_cat_image function test."""
        fetched_img = cats_direct.fetch_cat_image()
        assert len(fetched_img[0]) > 2
        assert int(fetched_img[1].headers['Content-length']) != 0

    def test_save_cat(self):
        """Save_cat function test."""
        assert os.path.isfile(self.test_image)
        with open(self.test_image, 'rb') as img:
            cats_direct.save_cat(
                index=1,
                fact='cats are cats',
                image=('jpg', img),
            )

        assert os.path.isfile(self.test_fact_file)
        with open(self.test_fact_file, 'r') as fact_file:
            assert fact_file.read() == self.simple_of_cats_fact

        assert os.path.isfile(self.result_image)
        with open(self.result_image, 'rb') as image_file:
            assert image_file.read()

    def test_integration(self):
        """Integration test."""
        format_str = 'python students/ziablik/4/cats_direct.py {0}'
        arg = '--count=1'
        command_str = format_str.format(arg)
        assert subprocess.call(command_str, shell=True) == 0


if __name__ == '__main__':
    unittest.main()
