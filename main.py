from GetImages import GetImages
from ScaleImages import ScaleImages

folder_images = '/home/kan/Imágenes/MedievalArt/'
format_to_find = 'png'
#don't work with full path, use '~'
folder_output = '~/Imágenes/'
prefix_output = 'CUDA_'

# parameters
waifu2x = 'waifu2x-ncnn-vulkan'
noise_level = 0
scale_level = 2
tile_size = 0
model_path = 'models-cunet'
gpu_id = 'auto'

if __name__ == '__main__':
    folder = GetImages(folder_images, format_to_find)
    list_images = folder.get_list_images()
    list_names_output = folder.get_list_name_output(prefix_output, folder_output)
    command = ScaleImages(list_images, list_names_output)
    command.execute_commands(waifu2x, noise_level, scale_level)

