from GetImages import GetImages
from ScaleImages import ScaleImages

folder_images = '~/waifu2x-ncnn-vulkan-multiple-images/test/Input'
format_to_find = 'png'
# don't work with full path, use '~'
folder_output = '~/~/waifu2x-ncnn-vulkan-multiple-images/test/Output'
prefix_output = 'CUDA_'

# parameters
waifu2x = 'waifu2x-ncnn-vulkan'
noise_level = 3  # denoise level (-1/0/1/2/3, default=0)
scale_level = 2  # upscale ratio (1/2/4/8/16/32, default=2)
tile_size = 0  # tile size (>=32/0=auto, default=0) can be 0,0,0 for multi-gpu
model_path = 'models-cunet'  # (default=models-cunet/models-upconv_7_anime_style_art_rgb)
gpu_id = 'auto'
enable_tta = False  # TTA mode able to reduce several type of artifacts but it's 8x slower than non TTA mode.

if __name__ == '__main__':
    folder = GetImages(folder_images, format_to_find)
    list_images = folder.get_list_images()
    list_names_output = folder.get_list_name_output(prefix_output, folder_output)
    command = ScaleImages(list_images, list_names_output)
    command.execute_commands(waifu2x, noise_level, scale_level, enable_tta)
