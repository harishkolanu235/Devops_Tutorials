from subprocess import Popen, PIPE, run
import sys



git_successful_commit = sys.argv[1]
git_latest_commit = sys.argv[2]


black = '\033[1;30m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
no_color = '\033[0m'


def cmd_execute(cmd):
    cmd_result = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    cmd_output, cmd_error = cmd_result.communicate()
    returnCode = cmd_result.returncode
    cmd_output = cmd_output.decode('utf8')
    cmd_error = cmd_error.decode('utf8')
    return returnCode, cmd_output, cmd_error


# get the latest changes on this build
all_changes_files = []
changes_cmd = f'git diff {git_successful_commit}..{git_latest_commit} --name-only'
print("Executing git diff command...........")
returnCode, changes_output, changes_error = cmd_execute(changes_cmd)
if returnCode == 0:
    if changes_output:
        print(f"\n{black}--------- This build contains below Changes ---------{no_color}\n")
        print(changes_output)
        all_changes_files = changes_output.splitlines()
        
    else:
        print(f"\n{yellow}WARNING: This build has no Changes{no_color}\n")
        sys.exit()
else:
    print(changes_error)
    sys.exit(returnCode)



## get the C files 
all_c_files = []
if all_changes_files:
    for each_file in all_changes_files:
        if each_file.endswith('.c'):
            all_c_files.append(each_file)


## Compiling C Files
for each_c_file in all_c_files:
    print(f"\n{blue}Compiling {each_file}.........{no_color}")
    compile_cmd=f"smake ${each_c_file}"
    print(compile_cmd)
    returnCode, compile_cmd_output, compile_cmd_error = cmd_execute(compile_cmd)
    if returnCode == 0:
        print(f"{green}Successfully Compiled {each_file} file.{no_color}\n")
    else:
        if compile_cmd_error:
            print(f"\n{red}{compile_cmd_error}{no_color}\n")
        if compile_cmd_output:
            print(f"\n{red}{compile_cmd_output}{no_color}\n")
        sys.exit(compile_cmd_error)
                








