 

def write_to_file(content: str) -> str:
    """Writes the given content to a file in JSON format."""
    try:
        file_name = "output.txt"  # Default file name
        content = content
        
        # Write content to the file
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
            
        return f"[+] Successfully written to '{file_name}'."
    except Exception as e:
        return f"[!] Error writing to file: {e}"

def read_file(file_name: str) -> str:
    """Reads the content of the specified file."""
    try:
        # Read content from the file
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            
        return content
    except FileNotFoundError:
        return f"[!] File '{file_name}' not found."
    except Exception as e:
        return f"[!] Error reading file: {e}"