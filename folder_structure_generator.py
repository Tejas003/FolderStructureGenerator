import os
from argparse import ArgumentParser
class FolderStructureGenerator:
    def __init__(self) -> None:
        pass

    def prints_formatter(self, 
                        level: int, 
                        is_last: bool, 
                        file_name: str) -> None: 
        '''
        This function will print the folder structure based on level and file_name

        '''
        beggining_string = ""
        space_within = "│    "
        if level == 0:
            beggining_string = ""
            space_within = ""
            ending_string = "├──"
            print(".")

        ending_string  = "└──"  if is_last is True else "├──"

        print(f"{beggining_string}{space_within*level}{ending_string} {file_name}")
    
    def format_folder_structure(self,
                                starting_path : str,
                                ignore_list : list,
                                ) -> None:
        '''

        This function will access the given folder and print a tree structure

        '''
        
        for root, dirs, files in os.walk(starting_path):
            file_name = os.path.basename(root)
            level = root.replace(starting_path, '').count(os.sep)
            ignore = False
            for item in ignore_list:
                if item in root:
                    ignore = True
            if ignore == False:
                self.prints_formatter(level,True,file_name)
                for f in files:
                    self.prints_formatter(level+1,True,f)
    
# Main Method
def main(starting_path : str,
        ignore_list : list) -> None:
    folder_structure_generator = FolderStructureGenerator()
    folder_structure_generator.format_folder_structure(starting_path,ignore_list)   # -> None

if __name__ == "__main__":
    # Getting arguments from Command Line and Printing the Tree Structure
    parser = ArgumentParser(description='List of arguments')
    parser.add_argument('-p','--path', help='Starting Path', required=True)
    parser.add_argument('-i','--ignore', help='List of Folders to be ignored', required=False, default="")
    args = vars(parser.parse_args())
    starting_path = str(args["path"])
    ignore_list = list(args["ignore"].split(","))
    main(starting_path,ignore_list) # -> None

