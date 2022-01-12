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
