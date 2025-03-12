import unittest
import os
from photos import collect_file_paths, compare_files, write_missing_files

class TestCollectFilePaths(unittest.TestCase):
    def setUp(self):
        os.makedirs('test_src/dir1', exist_ok=True)
        os.makedirs('test_src/dir2', exist_ok=True)
        os.makedirs('test_src/.hidden', exist_ok=True)
        with open('test_src/file1.txt', 'w') as f:
            f.write('test')
        with open('test_src/dir1/file2.txt', 'w') as f:
            f.write('test')
        with open('test_src/dir2/file3.txt', 'w') as f:
            f.write('test')
        with open('test_src/.hidden/file4.txt', 'w') as f:
            f.write('test')

        os.makedirs('test_dest/dir1', exist_ok=True)
        os.makedirs('test_dest/dir2', exist_ok=True)
        with open('test_dest/file1.txt', 'w') as f:
            f.write('test')
        with open('test_dest/dir1/file2.txt', 'w') as f:
            f.write('test')
        with open('test_dest/dir2/file3.txt', 'w') as f:
            f.write('test')

    def tearDown(self):
        for root, dirs, files in os.walk('test_src', topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir('test_src')

        for root, dirs, files in os.walk('test_dest', topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir('test_dest')

    def test_collect_file_paths(self):
        expected_files = [
            'file1.txt',
            'dir1/file2.txt',
            'dir2/file3.txt',
            '.hidden/file4.txt'
        ]
        collected_files = collect_file_paths('test_src')
        self.assertCountEqual(collected_files, expected_files)

    def test_collect_file_paths_with_extensions(self):
        expected_files = [
            'file1.txt',
            'dir1/file2.txt',
            'dir2/file3.txt'
        ]
        collected_files = collect_file_paths('test_src', extensions=['.txt'])
        self.assertCountEqual(collected_files, expected_files)

    def test_collect_file_paths_exclude_dirs(self):
        expected_files = [
            'file1.txt',
            'dir1/file2.txt'
        ]
        collected_files = collect_file_paths('test_src', exclude_dirs=['test_src/dir2'])
        self.assertCountEqual(collected_files, expected_files)

    def test_compare_files(self):
        src_files = collect_file_paths('test_src')
        dest_files = collect_file_paths('test_dest')
        missing_files = compare_files(src_files, dest_files, 'test_src', 'test_dest')
        expected_missing_files = {'.hidden/file4.txt'}
        self.assertEqual(missing_files, expected_missing_files)

    def test_write_missing_files(self):
        missing_files = {'.hidden/file4.txt'}
        output_file = 'test_output.txt'
        write_missing_files(output_file, missing_files)
        with open(output_file, 'r') as f:
            lines = f.readlines()
        expected_lines = ['.hidden/file4.txt\n']
        self.assertEqual(lines, expected_lines)
        os.remove(output_file)

    def test_write_missing_files_empty(self):
        missing_files = set()
        output_file = 'test_output.txt'
        write_missing_files(output_file, missing_files)
        with open(output_file, 'r') as f:
            lines = f.readlines()
        expected_lines = []
        self.assertEqual(lines, expected_lines)
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()