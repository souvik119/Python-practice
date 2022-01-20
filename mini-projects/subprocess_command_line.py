import subprocess


def execute_command(command):
    '''
    Executes command and returns output and error
    '''
    command_list = command.split()
    output = subprocess.run(command_list, shell=True, capture_output=True)
    output_text = output.stdout.decode('utf-8')
    error_text = output.stderr.decode('utf-8')
    return error_text, output_text
    

def main():
    error, output = execute_command('ping 8.8.8.8')
    print(output)
    print(error)

if __name__ == '__main__':
    main()