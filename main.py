import os
import shutil
import argparse

def explore_directory(path='.'):
    """Explore and list files and directories in the specified path."""
    try:
        for entry in os.listdir(path):
            print(entry)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")

def duplicate_file(source, destination):
    """Duplicate a file from source to destination."""
    try:
        shutil.copy(source, destination)
        print(f"Duplicated {source} to {destination}")
    except FileNotFoundError:
        print(f"The file '{source}' does not exist.")

def relocate_file(source, destination):
    """Relocate a file from source to destination."""
    try:
        shutil.move(source, destination)
        print(f"Relocated {source} to {destination}")
    except FileNotFoundError:
        print(f"The file '{source}' does not exist.")

def alter_filename(source, new_name):
    """Alter the name of a file."""
    try:
        os.rename(source, new_name)
        print(f"Altered {source} to {new_name}")
    except FileNotFoundError:
        print(f"The file '{source}' does not exist.")

def remove_file(path):
    """Remove a file or directory."""
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"Removed file: {path}")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Removed directory: {path}")
        else:
            print(f"The path '{path}' does not exist.")
    except FileNotFoundError:
        print(f"The file or directory '{path}' does not exist.")

def print_file_tree(path='.', indent=''):
    """Print the directory tree structure."""
    try:
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            print(indent + '|-- ' + entry)
            if os.path.isdir(full_path):
                print_file_tree(full_path, indent + '    ')
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")

def main():
    parser = argparse.ArgumentParser(description='Customized File Manager')
    
    parser.add_argument('command', choices=['explore', 'duplicate', 'relocate', 'alter', 'remove', 'tree'], help='Command to execute')
    parser.add_argument('--path', default='.', help='Path to operate on')
    parser.add_argument('--source', help='Source file or directory')
    parser.add_argument('--destination', help='Destination file or directory')
    parser.add_argument('--new_name', help='New name for the alter operation')
    
    args = parser.parse_args()
    
    if args.command == 'explore':
        explore_directory(args.path)
    elif args.command == 'duplicate' and args.source and args.destination:
        duplicate_file(args.source, args.destination)
    elif args.command == 'relocate' and args.source and args.destination:
        relocate_file(args.source, args.destination)
    elif args.command == 'alter' and args.source and args.new_name:
        alter_filename(args.source, args.new_name)
    elif args.command == 'remove':
        remove_file(args.path)
    elif args.command == 'tree':
        print_file_tree(args.path)
    else:
        print("Invalid command or missing arguments.")
        parser.print_help()

if __name__ == "__main__":
    main()
