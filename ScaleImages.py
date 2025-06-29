import subprocess

def prints(number):
    print('Number of images done: ' + str(number))
    print('-----------------------------------------------------------------------------------------------')

class ScaleImages:

    def __init__(self, list_names_to_transform, list_names_output):
        self.list_input = list_names_to_transform
        self.list_output = list_names_output

    def execute_commands(self, waifu2x, noise_level, scale, enable_tta):
        list_command = []
        for i in range(len(self.list_input)):
            command = waifu2x + ' -i ' + self.list_input[i] + ' -o ' + self.list_output[i]
            command += ' -n ' + str(noise_level) + ' -s ' + str(scale)
            if enable_tta:
                command += ' -x'
            list_command.append(command)

        for i, command in enumerate(list_command):
            try:
                # Ejecuta el comando con shell=True pasando la cadena completa
                subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                prints(i+1)
            except subprocess.CalledProcessError as exc:
                print(f"Error al ejecutar el comando:\n{command}")
                print(exc.output.decode())
