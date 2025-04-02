import argparse
import os
import shutil

def parse_arguments():
    parser = argparse.ArgumentParser(description="Compare directories and find missing files.")
    parser.add_argument('src', type=str, help='Source directory')
    parser.add_argument('dest', type=str, help='Destination directory')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output directory for missing files')
    parser.add_argument('-e', '--ext', type=str, nargs='*', help='List of file extensions to consider')
    parser.add_argument('--skip-hash', action='store_true', help='Skip hashing')
    parser.add_argument('--follow-symlinks', action='store_true', help='Follow symbolic links')
    parser.add_argument('--threads', type=int, default=1, help='Number of threads for scanning')
    parser.add_argument('--progress', type=int, help='Show progress every N files')
    parser.add_argument('--exclude', type=str, nargs='*', help='List of subdirectories to exclude')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose logging')
    
    return parser.parse_args()

def collect_file_paths(directory, extensions=None, follow_symlinks=False, exclude_dirs=None):
    file_paths = []
    for root, dirs, files in os.walk(directory, followlinks=follow_symlinks):
        if exclude_dirs:
            dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_dirs]
        for file in files:
            if not extensions or any(file.endswith(ext) for ext in extensions):
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                file_paths.append(relative_path)
    return file_paths

def get_file_size(directory, relative_path):
    return os.path.getsize(os.path.join(directory, relative_path))

def compare_files(src_files, dest_files, src_dir, dest_dir):
    src_file_set = {file: get_file_size(src_dir, file) for file in src_files}
    dest_file_set = {file: get_file_size(dest_dir, file) for file in dest_files}
    
    missing_files = {file for file in src_file_set if file not in dest_file_set or src_file_set[file] != dest_file_set[file]}
    
    return missing_files

def copy_missing_files(src_dir, output_dir, missing_files):
    os.makedirs(output_dir, exist_ok=True)
    for file in missing_files:
        src_file_path = os.path.join(src_dir, file)
        dest_file_path = os.path.join(output_dir, file)
        os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
        shutil.copy2(src_file_path, dest_file_path)

if __name__ == "__main__":
    args = parse_arguments()
    src_files = collect_file_paths(args.src, args.ext, args.follow_symlinks, args.exclude)
    dest_files = collect_file_paths(args.dest, args.ext, args.follow_symlinks, args.exclude)
    
    missing_files = compare_files(src_files, dest_files, args.src, args.dest)
    
    copy_missing_files(args.src, args.output, missing_files)
    
    print("Missing files copied to:", args.output)
