
Draft a detailed, step-by-step blueprint for building this project. Then, once you have a solid plan, break it down into small, iterative chunks that build on each other. Look at these chunks and then go another round to break it into small steps. Review the results and make sure that the steps are small enough to be implemented safely with strong testing, but big enough to move the project forward. Iterate until you feel that the steps are right sized for this project.

From here you should have the foundation to provide a series of prompts for a code-generation LLM that will implement each step in a test-driven manner. Prioritize best practices, incremental progress, and early testing, ensuring no big jumps in complexity at any stage. Make sure that each prompt builds on the previous prompts, and ends with wiring things together. There should be no hanging or orphaned code that isn't integrated into a previous step.

Make sure and separate each prompt section. Use markdown. Each prompt should be tagged as text using code tags. The goal is to output prompts, but context, etc is important as well.


# **Directory Comparison Script Specification**

## **Overview**  
A Python script to recursively scan two directory trees (`src` and `dest`) and identify files missing from `dest`.  

## **Functionality**  
- Compares files based on **name, size, and MD5 hash** (unless `--skip-hash` is used).  
- Accepts a **list of file extensions** to filter files (e.g., `.jpg`, `.txt`).  
- Outputs missing file paths **relative to `src`** in a plain text file.  
- Supports **recursive scanning** of `src`.  
- Logs **errors to `stderr`** (e.g., unreadable files).  

## **Command-Line Arguments**  
- `src` (required): Source directory.  
- `dest` (required): Destination directory.  
- `-o, --output <file>` (required): Output file for missing file paths.  
- `-e, --ext <ext> ...`: List of file extensions to consider (e.g., `-e .jpg .txt`).  
- `--skip-hash`: Compare only filenames and sizes (faster).  
- `--follow-symlinks`: Follow symbolic links (ignored by default).  
- `--threads <N>`: Number of threads for faster scanning.  
- `--progress <N>`: Show progress every **N** files.  
- `--exclude <dir> ...`: Exclude specific subdirectories from scanning.  
- `--verbose`: Log every file comparison to `stdout`.  
- `--help`: Display usage instructions.  

## **Behavior**  
- **Error Handling:**  
  - Exits **with error (1)** if `dest` does not exist.  
  - Exits **with error (1)** if `src` or `dest` cannot be accessed.  
  - **Ignores extra files** in `dest` (only reports missing files).  
- **File Handling:**  
  - Overwrites existing output file.  
  - Includes **hidden files** (starting with `.`).  
  - **Skips empty directories** in `src`.  
- **Paths:**  
  - Uses **relative paths** for output.  
  - **Does not normalize paths** (`./`, `../`, redundant slashes).  
  - Uses **OS default path format** (`/` for Unix, `\` for Windows).  
- **Performance:**  
  - **Multi-threaded** with configurable thread count.  
  - **Periodic progress updates** (configurable).  
  - **No time estimates** provided.  

## **Output**  
- **Missing files list** (relative paths) written to the specified output file.  
- **Summary printed to `stdout`**:  
  - **Total files scanned**  
  - **Total missing files found**  

## **Exit Codes**  
- `0` → Success (even if missing files are found).  
- `1` → Errors (invalid input, permission issues, etc.).  

---

This spec is **developer-ready** and should cover all major aspects of the script. Let me know if you need any refinements! 🚀