import zlib
import os

def compute_crc(file_path):
    """Compute the CRC32 checksum of a file."""
    with open(file_path, 'rb') as f:
        data = f.read()
        return zlib.crc32(data) & 0xffffffff  # Ensure unsigned 32-bit

def compute_checksum(file_path):
    """Compute a simple checksum (sum of bytes) of a file."""
    with open(file_path, 'rb') as f:
        data = f.read()
        return sum(data) & 0xffffffff  # Ensure unsigned 32-bit

def process_file(file_path):
    """Compute and save CRC and checksum to a metadata file."""
    crc = compute_crc(file_path)
    checksum = compute_checksum(file_path)

    # Save to metadata file
    metadata_filename = f"{file_path}.meta"
    with open(metadata_filename, 'w') as meta_file:
        meta_file.write(f"CRC32: {crc:08X}\n")
        meta_file.write(f"Checksum: {checksum}\n")

    print(f"Processed {file_path} - CRC32: {crc:08X}, Checksum: {checksum}")

def validate_file(file_path):
    """Validate the file against its saved CRC and checksum."""
    metadata_filename = f"{file_path}.meta"

    if not os.path.exists(metadata_filename):
        print("No metadata found. Please process the file first.")
        return

    with open(metadata_filename, 'r') as meta_file:
        expected_crc = int(meta_file.readline().split(': ')[1], 16)
        expected_checksum = int(meta_file.readline().split(': ')[1])

    actual_crc = compute_crc(file_path)
    actual_checksum = compute_checksum(file_path)

    if actual_crc != expected_crc:
        print(f"CRC mismatch for {file_path}: expected {expected_crc:08X}, got {actual_crc:08X}")
    elif actual_checksum != expected_checksum:
        print(f"Checksum mismatch for {file_path}: expected {expected_checksum}, got {actual_checksum}")
    else:
        print("File validation successful.")

if __name__ == "__main__":
    action = input("Enter action (process/validate): ").strip().lower()
    filename = input("Enter filename: ").strip()

    if action == "process":
        process_file(filename)
    elif action == "validate":
        validate_file(filename)
    else:
        print("Invalid action. Please enter 'process' or 'validate'.")