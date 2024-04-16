import solcx
from solcx import compile_standard, install_solc,compile_source

def compile_source_file(file_path):
    with open(file_path,'r') as f:
        file=f.read()
    print(file)
    compiled_file=compile_source(file)
    return compiled_file

if __name__ =="__main__":
    install_solc('0.8.9',show_progress=True)
    sol_file_path=r"D:\ml\contract\contract.sol"
    
    sol_compiled_file=compile_source_file(sol_file_path)
    
    print(sol_compiled_file)