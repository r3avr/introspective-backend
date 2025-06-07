import os

IGNORED_DIRS = {'venv', '.venv', '__pycache__', '.git', '.idea', '.DS_Store', '.pytest_cache', '.mypy_cache'}
OUTPUT_FILE = 'project_structure.txt'

def build_tree(start_path='.', prefix=''):
    lines = []
    items = sorted(os.listdir(start_path))
    items = [item for item in items if item not in IGNORED_DIRS and not item.startswith('.')]

    for idx, item in enumerate(items):
        path = os.path.join(start_path, item)
        is_last = idx == len(items) - 1
        branch = '└── ' if is_last else '├── '
        lines.append(prefix + branch + item)

        if os.path.isdir(path):
            extension = '    ' if is_last else '│   '
            lines.extend(build_tree(path, prefix + extension))

    return lines

if __name__ == '__main__':
    tree_output = ["Project structure:\n"]
    tree_output.extend(build_tree())

    full_output = '\n'.join(tree_output)
    print(full_output)

    with open(OUTPUT_FILE, 'w') as f:
        f.write(full_output + '\n')
