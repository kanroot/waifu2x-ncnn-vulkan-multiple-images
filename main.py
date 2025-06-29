import os
from GetImages import GetImages
from ScaleImages import ScaleImages

folder_images = '~/Imágenes/DER/'
format_to_find = 'jpg'
folder_output = '~/Imágenes/DER_OUT/'
prefix_output = 'NCNN_'

# parameters
waifu2x = 'waifu2x-ncnn-vulkan'
noise_level = 3
scale_level = 1
enable_tta = False

if __name__ == '__main__':
    folder_images_exp = os.path.expanduser(folder_images)
    folder_output_exp = os.path.expanduser(folder_output)
    folder = GetImages(folder_images_exp, format_to_find)
    list_images = folder.get_list_images()
    if not list_images:
        print("No se encontraron imágenes para procesar.")
        exit(1)
    list_names_output = folder.get_list_name_output(prefix_output, folder_output_exp)
    command = ScaleImages(list_images, list_names_output)
    command.execute_commands(waifu2x, noise_level, scale_level, enable_tta)
