# TODO Checklist: Directory Comparison Script

## Phase 1: Core Infrastructure

- [ ] **Argument Parsing**
  - [ ] Implement `argparse` for command-line arguments
  - [ ] Support `src`, `dest`, and `-o, --output`
  - [ ] Implement `--help` with usage instructions
  - [ ] Add `-e, --ext` for file extension filtering
  - [ ] Implement `--skip-hash` flag
  - [ ] Add `--follow-symlinks` flag
  - [ ] Implement `--threads <N>` for parallel processing
  - [ ] Add `--progress <N>` for progress updates
  - [ ] Support `--exclude <dir>` for excluding directories
  - [ ] Implement `--verbose` for logging
  - [ ] Write unit tests for argument parsing

- [ ] **Directory Scanning**
  - [ ] Implement recursive scanning using `os.walk()`
  - [ ] Collect file paths and store them in a structured format
  - [ ] Ensure relative paths are used for output
  - [ ] Write unit tests for directory traversal

- [ ] **File Comparison (Name & Size)**
  - [ ] Implement comparison logic based on filename and size
  - [ ] Store results in an efficient data structure
  - [ ] Identify missing files in `dest`
  - [ ] Add unit tests for missing file detection

## Phase 2: Feature Expansion

- [ ] **MD5 Hashing Support**
  - [ ] Implement MD5 checksum calculation
  - [ ] Optimize hashing by reading files in chunks
  - [ ] Ensure `--skip-hash` disables hashing
  - [ ] Write unit tests for MD5 hashing

- [ ] **File Extension Filtering**
  - [ ] Implement filtering logic for `-e, --ext`
  - [ ] Ensure case-insensitive matching
  - [ ] Add unit tests for extension filtering

- [ ] **Output File Handling**
  - [ ] Write missing file paths to the output file
  - [ ] Ensure paths are relative to `src`
  - [ ] Overwrite existing output file if present
  - [ ] Add unit tests for correct output formatting

## Phase 3: Optimization and Robustness

- [ ] **Multithreading for Performance**
  - [ ] Implement a multi-threaded scanner
  - [ ] Ensure `--threads` controls thread count
  - [ ] Test performance on large directories
  
- [ ] **Error Handling & Logging**
  - [ ] Handle missing directories gracefully
  - [ ] Handle permission errors
  - [ ] Handle unreadable files
  - [ ] Implement structured logging to `stderr`
  - [ ] Support `--verbose` logging for debugging
  - [ ] Write unit tests for error scenarios

- [ ] **Progress Reporting**
  - [ ] Implement `--progress <N>` updates
  - [ ] Ensure updates do not interfere with output
  - [ ] Write unit tests for progress updates

## Phase 4: Final Refinements

- [ ] **Excluding Directories**
  - [ ] Implement `--exclude <dir>` to skip specified directories
  - [ ] Validate proper exclusion logic
  - [ ] Add unit tests for exclusion handling

- [ ] **Symbolic Links Support**
  - [ ] Implement `--follow-symlinks` behavior
  - [ ] Ensure no infinite loops occur
  - [ ] Write unit tests for symlink handling

- [ ] **Final Testing & Integration**
  - [ ] Perform full integration testing
  - [ ] Verify performance and robustness
  - [ ] Test on large and nested directory structures
  - [ ] Ensure proper exit codes (`0` for success, `1` for errors)
  - [ ] Validate correct handling of edge cases
  - [ ] Final review and documentation update

### **Project Completion**
✅ **Ready for Deployment & Use** 🚀

