from GetImages import GetImages

folder_images = '/home/kan/Imágenes/MedievalArt'
format_to_find = 'png'
folder_output = ''
prefix_output = 'CUDA_'

# parameters
noise_level = 0
scale_level = 2
tile_size = 0
model_path = 'models-cunet'
gpu_id = 'auto'

if __name__ == '__main__':
    folder = GetImages(folder_images, format_to_find)
    list_images = folder.get_list_images()
    print(list_images)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
