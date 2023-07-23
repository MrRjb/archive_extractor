import zipfile

def archive_extract(filepath, dest_dir):
    with zipfile.ZipFile(filepath, 'r') as archive:
        archive.extractall(dest_dir)
        
    