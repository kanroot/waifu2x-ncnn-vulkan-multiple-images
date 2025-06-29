import os
import glob

class GetImages:
    def __init__(self, folder, format_to_find):
        self.folder = folder
        self.format_to_find = format_to_find
        self.list_images = []

    def get_list_images(self):
        pattern = os.path.join(self.folder, f'*.{self.format_to_find}')
        for filename in glob.iglob(pattern, recursive=True):
            self.list_images.append(filename)  # Sin comillas extras
        if len(self.list_images) > 0:
            return self.list_images
        else:
            print("Check the folder's path")
            return []

    def get_list_name_output(self, prefix, folder):
        list_output = []
        for name_original in self.list_images:
            base_name = os.path.basename(name_original)
            name_with_prefix = prefix + base_name
            print("Image to transform: " + base_name)
            print('--------------------------------------------------------------------------------------------------')
            path = os.path.join(folder, name_with_prefix)
            list_output.append(path)
        return list_output