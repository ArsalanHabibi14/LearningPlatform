import os


def get_file_path(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext


def file_upload(instance, filename):
    name, ext = get_file_path(filename)
    final_name = f"video/{instance.title}{ext}"
    return final_name
