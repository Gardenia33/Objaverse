"""Utility functions for the objaverse_xl package."""

import hashlib
import os
import uuid



# # 直接将这个方法改为存储所有投影模型的名称
# def get_uid_from_str(string: str) -> str:
#     """Generates a UUID from a string.
#
#     Args:
#         string (str): String to generate a UUID from.
#
#     Returns:
#         str: UUID generated from the string.
#     """
#     namespace = uuid.NAMESPACE_DNS
#     return str(uuid.uuid5(namespace, string))

def get_uid_from_str(string: str) -> str:
    """Extracts the name of the obj model from a URL string.

    Args:
        string (str): URL string to extract the obj model name from.

    Returns:
        str: Extracted obj model name.
    """
    # Split the URL by '/' and get the last part
    obj_name = string.split('/')[-1]
    # Remove the file extension if it exists
    if obj_name.endswith('.obj'):
        obj_name = obj_name[:-4]
    return obj_name

def get_file_hash(file_path: str) -> str:
    """Get the sha256 hash of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: sha256 hash of the file.
    """
    # Check if the path is a symbolic link
    if os.path.islink(file_path):
        # Resolve the symbolic link
        resolved_path = os.readlink(file_path)
        # Check if the resolved path exists
        if not os.path.exists(resolved_path):
            raise FileNotFoundError(
                f"The symbolic link points to a file that doesn't exist: {resolved_path}"
            )
    sha256 = hashlib.sha256()
    # Read the file from the path
    with open(file_path, "rb") as f:
        # Loop till the end of the file
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256.update(byte_block)
    return sha256.hexdigest()
