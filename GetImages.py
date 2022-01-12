import glob


class GetImages:
    def __init__(self, folder, format_to_find):
        self.folder = folder
        self.format_to_find = format_to_find
        self.list_images = []

    def get_list_images(self):
        for filename in glob.iglob(self.folder + '**/*.' + self.format_to_find, recursive=True):
            self.list_images.append(filename)
        return self.list_images

    def get_list_name_output(self, prefix):
        list_output = []
        for name_original in self.list_images:
            last_slash = name_original.rfind("/") + 1
            list_output.append(name_original[:last_slash] + prefix + name_original[last_slash:])
        return list_output
