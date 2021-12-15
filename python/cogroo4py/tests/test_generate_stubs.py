import unittest
import os
from cogroo4py import generate_stubs
import shutil


class TestGenerateStubs(unittest.TestCase):
    output_dir = generate_stubs.current_path + '/tests/stub-generation-tests'

    def setUp(self) -> None:
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)

    def test_stub_generation(self):
        generate_stubs.generate_stubs(output_dir=self.output_dir)
        self.assertTrue(os.path.exists(self.output_dir + '/java-stubs'))
        self.assertTrue(os.path.exists(self.output_dir + '/jpype-stubs'))
        self.assertTrue(os.path.exists(self.output_dir + '/org-stubs'))

    def tearDown(self) -> None:
        shutil.rmtree(self.output_dir)


if __name__ == '__main__':
    unittest.main()
