from os import system, name, path

def clear():
    system('cls' if name == 'nt' else 'clear')


def set_metadata():
    print('set_metadata()')
    pass


def process_file(choice, file_path, file_strip_path, file_basename):
    clear()
    print('Process started please wait...')
    system(f'ffmpeg -loglevel quiet -stats -i {file_path} -map 0 -map -0:a:{choice} -c copy {file_strip_path}AudioRemoved-{file_basename}')


def file_input():
    FILE_PATH = input('Input file path: ')              # entire path
    FILE_BASENAME = path.basename(FILE_PATH)            # file basename fulano.txt
    FILE_STRIP_PATH = FILE_PATH.strip(FILE_BASENAME)    # half path

    # save output console result on a txt file
    system(f'ffmpeg -i {FILE_PATH} 2>console_output.txt')
    clear()

    lines = []
    list_audios_track = []
    count = 0

    with open('console_output.txt', 'rt') as myFile:
        for line in myFile:
           lines.append(line.rstrip('\n'))

    while True:
        try:
            if 'Audio:' in lines[count]:
                found = str(lines[count])
                found = found.split(' ')
                re = found[3]
                re = re.split('(')
                re1 = re[1]
                re1 = re1.replace('):', '')
                list_audios_track.append(re1)
                count += 1
        except:
            count = 0
            print('Audio tracks found:\n')

            while count < len(list_audios_track):
                print(f'[{count}] {list_audios_track[count]}')
                count += 1
            choice = int(input('\nselect which one will be removed (-1 to exit): '))
            if choice >= len(list_audios_track):
                clear()
                print('Please select a valid option !')
                break
            if choice == -1:
                clear()
                break
            else:
                process_file(choice, FILE_PATH, FILE_STRIP_PATH, FILE_BASENAME)
            break
        finally:
            count += 1

clear()
file_input()

print('\n\nScript Exiting !')