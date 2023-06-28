import glob


class GetImages:
    def __init__(self, folder, format_to_find):
        self.folder = folder
        self.format_to_find = format_to_find
        self.list_images = []

    def get_list_images(self):
        for filename in glob.iglob(self.folder + '*.' + self.format_to_find, recursive=True):
            filename = "\'" + filename + "\'"
            self.list_images.append(filename)
        if len(self.list_images) > 0:
            return self.list_images
        else:
            print("Check the folder's path")

    def get_list_name_output(self, prefix, folder):
        list_output = []
        for name_original in self.list_images:
            last_slash = name_original.rfind("/") + 1
            name_with_prefix = prefix + name_original[last_slash:]
            print("Image to transform: " + name_original[last_slash:])
            print('--------------------------------------------------------------------------------------------------')
            path = "\'" + folder + name_with_prefix
            list_output.append(path)
        return list_output
