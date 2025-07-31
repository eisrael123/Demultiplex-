#!/usr/bin/env python
import unittest
import os

class TestFastqFiles(unittest.TestCase):
    def setUp(self):
        self.output_dir = '/projects/bgmp/ewi/bioinfo/Bi621/PS/Demultiplex-/output_demultiplex'
        self.expected_dir = '/projects/bgmp/ewi/bioinfo/Bi621/PS/Demultiplex-/TEST-output_FASTQ'

    def test_fastq_files_match(self):
        # Gather only .fastq files in expected directory
        expected_files = [f for f in os.listdir(self.expected_dir) if f.endswith('.fastq')]

        # Check all expected .fastq files exist and match content
        for filename in expected_files:
            expected_path = os.path.join(self.expected_dir, filename)
            output_path = os.path.join(self.output_dir, filename)

            # Assert output file exists
            self.assertTrue(os.path.exists(output_path), f"Missing output file: {filename}")

            # Compare file content
            with open(expected_path, 'rb') as f_exp, open(output_path, 'rb') as f_out:
                expected_data = f_exp.read()
                output_data = f_out.read()
                self.assertEqual(expected_data, output_data,
                                 f"Contents differ in file: {filename}")

        # Optional: Check output directory does not contain unexpected .fastq files
        output_files = [f for f in os.listdir(self.output_dir) if f.endswith('.fastq')]
        unexpected_files = set(output_files) - set(expected_files)
        if unexpected_files:
            self.fail(f"Output directory contains unexpected .fastq files: {unexpected_files}")

if __name__ == '__main__':
    unittest.main()