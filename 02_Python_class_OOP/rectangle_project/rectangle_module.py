from loguru import logger
from pathlib import Path
from argparse import ArgumentParser, HelpFormatter
import json, re, os, shutil
from termcolor import colored
import multiprocessing


#-----------------------------------------------------------------------------------------------------------#
#--------------------------------- Define Class and its methods --------------------------------------------#
#-----------------------------------------------------------------------------------------------------------#

class RectangleCalculator:
    '''
    This class will takes the length and width of a rectangle as inputs, 
    then return the corresponding perimeter and area as outputs.

    It can also read inputs from multiple JSON files.
    The results can be returned in a specified JSON file.
    The class supports multicore computing.
    '''


    def __init__(self, input = '', output = '', length = None, width = None, cores = 2):
        '''
        input: the path leading to an input directory containing JSON files, or directly to a specified JSON file
        output: the path leading to on output directory to store the results in JSON files, or directly to a specified JSON file
        length: the length of the rectangle (for inplace calculating)
        width: the width of the rectangle (for inplace calculating)
        cores: the number of CPU cores using for parallel computing
        '''
        self.input = input
        self.output = output
        self.__length = length
        self.__width = width
        self.cores = cores
        self._single_output_path = None


    def __validate_output_directory(self):
        match str(self.output):
            case "":
                pass
            case _:
                if (len(str(self.output).split(os.path.sep)) == 1) or (not (Path(self.output).parent.is_dir())):
                    logger.warning(
                        "The output path's parent directory was not specified!"
                        f"\nThe current directory {Path.cwd()} will be set as its parent directory"
                    )
                    self.output = Path.cwd() / Path(self.output).name
                
                if (Path(self.output).suffix != ""):
                    self.output = Path(self.output)
                    self.output = self.output.parent / self.output.stem # Create a new path without the suffix
                    logger.warning(f"You have passed inputs from multiple files, so the ouput path should be a directory, automatically set as {self.output}")
                
                else:
                    self.output = Path(self.output)
                
                if (self.output.is_dir()) and (self.output != Path.cwd()):
                    shutil.rmtree(self.output)
                
                self.output.mkdir(exist_ok = True)
        
        return self.output


    def __validate_output_file(self, json_output_file):
        if str(json_output_file) == "":
            return None
        
        elif Path(self.input).is_dir():
            json_output_file = Path(self.output).joinpath(json_output_file)
            
            if (len(str(json_output_file).split(os.path.sep)) == 1) or (not (Path(json_output_file).parent.is_dir())):
                logger.warning(
                    "The output path's parent directory was not specified!"
                    f"\nThe current directory {Path.cwd()} will be set as its parent directory"
                )
                json_output_file = Path.cwd().joinpath(json_output_file.name)

        elif str(self.output) == "":
                return ""
        else:
            json_output_file = Path(self.output)
            if not json_output_file.name.endswith(".json"):
                json_output_file = json_output_file.parent / Path(json_output_file.stem+".json")
                logger.warning(f"The output file name does not end with '.json', automatically set as {json_output_file}")
        
        return json_output_file


    @staticmethod
    def __valiate_input_number(*numbers): # Internal use only, cannot call out when the module is being imported
        numeric_pattern = r"^\d+\.?\d*$"
        numbers = list(numbers)
        for idx, number in enumerate(numbers):
            if re.match(numeric_pattern, str(number)):
                numbers[idx] = float(number)
            else:
                numbers[idx] = None
        
        return numbers


    def load_rectangle_inputs(self, json_rectangle_file):
        if len(Path(json_rectangle_file).parts) > 1:
            json_file_path = json_rectangle_file
        else:
            json_file_path = self.input.joinpath(json_rectangle_file)
        
        with open(json_file_path, "r") as json_pointer:
            length, width = json.load(json_pointer).values()
            length, width = RectangleCalculator.__valiate_input_number(length, width)
        
        if None in [length, width]:
            logger.error(f"CORRUPTED inputs are detected in {json_rectangle_file}! They are expected to be POSITIVE NUMBERS (greater than zero)\n")
        
        return length, width
    

    @property
    def perimeter(self):
        self.length, self.width = self.__valiate_input_number(self.length, self.width)
        
        if None in [self.length, self.width]:
            self.__perimeter = None
        else:
            self.__perimeter = 2 * (self.length + self.width) # Name it as "self.__perimeter" to prevent user from changing its value 
       
        return self.__perimeter


    @property
    def area(self):
        self.length, self.width = self.__valiate_input_number(self.length, self.width)
        
        if None in [self.length, self.width]:
            self.__area = None
        else:
            self.__area = self.length * self.width # Name it as "self.__area" to prevent user from changing its value
        return self.__area

    
    def save_output_file(self, json_rectangle_file):
        result_dict = {
            "length": self.length,
            "width": self.width,
            "perimeter": self.perimeter,
            "area": self.area
        }

        if None in [self.__perimeter, self.__area]:
            return None # Don't save the file if its outputs are corrupted
        
        if self._single_output_path is None:
            self._single_output_path = self.__validate_output_file(json_rectangle_file)
       
        with open(self._single_output_path, "w") as json_pointer:
            json.dump(result_dict, json_pointer, indent = 4)

    
    def summary(self, json_output_file = "nameless.json"):
        
        match str(self.output):
            case "":
                if json_output_file == "nameless.json":
                    rectangle_name = colored(str(json_output_file).replace(".json", ""), "magenta", attrs=["bold"])
                else:
                    rectangle_name = colored(str(json_output_file), "magenta", attrs=["bold"])

                perimeter_result = colored(f"++ Perimeter = 2 * ({self.length} + {self.width}) = {self.perimeter}", "cyan", attrs=["bold"])
                area_result = colored(f"++ Area = {self.length} * {self.width} = {self.area}", "cyan", attrs=["bold"])

                out_message = (
                    f"\n\nResult of the {rectangle_name} rectangle:\n"
                    f"++ Length = {self.length}\n"
                    f"++ Width = {self.width}\n"
                    f"{perimeter_result}\n"
                    f"{area_result}\n"
                )    
                
                if (str(self.input) == "")  and (None in [self.__perimeter, self.__area]):
                    logger.critical("The given inputs are CORRUPTED! They are expected to be POSITIVE NUMBERS (greater than zero)")
                else:
                    logger.info(out_message)
            
            case _:
                if json_output_file == "nameless.json":
                    logger.warning("The output file name was not specified, automatically set as 'nameless.json'")
                self.save_output_file(json_output_file)


    def _single_workflow(self, json_rectangle_file):
        if json_rectangle_file != '':
            self.length, self.width = self.load_rectangle_inputs(json_rectangle_file)
            
            if (None not in [self.__length, self.__width]):
                logger.warning(f"Detected valid inputs in {json_rectangle_file}, prioritize them for calculation.")

            self._single_output_path = self.__validate_output_file(json_rectangle_file)
            self.summary(self._single_output_path)
        
        elif None in [self.__length, self.__width]:
            logger.critical("No valid inputs were given")
        
        else:
            self.length, self.width = self.__length, self.__width
            self._single_output_path = self.__validate_output_file(self.output)

            if self._single_output_path is None:
                self.summary()
            else:
                self.summary(self._single_output_path)
                logger.info(f"The result is saved in {self._single_output_path}")

            

#------------------------------------------------------------------------------------------------------------#
#------------------------------------------ Define log_file() function --------------------------------------#
#------------------------------------------------------------------------------------------------------------#

def config_log_file(project_dir):
    logger_path = Path(project_dir).joinpath("rectangle_logs.txt")
    if logger_path.exists():
        logger_path.unlink() # Delete the rectangle_logs.txt of the previous run if existed

    logger.add(sink = logger_path, # The path to the .txt file that saves logs
            rotation="1 MB",  # Rotate when file reaches 1MB
            retention="10 days",  # Keep logs for 10 days
            level="WARNING") # Only save the WARNING level and above


#------------------------------------------------------------------------------------------------------------#
#------------------------------------------ Define main() function ------------------------------------------#
#------------------------------------------------------------------------------------------------------------#

def main():
    try:
        calculator = RectangleCalculator(
            input = "02_Python_class_OOP/rectangle_project/data/rectangle_1.json",
            output = "02_Python_class_OOP/rectangle_project/result",
            #length = 100,
            #width = 3,
            cores = 4
        )

        if (calculator.input != "") and Path(calculator.input).exists():
            calculator.input = Path(calculator.input)

            if calculator.input.suffix == ".json":
                calculator._single_workflow(calculator.input)
                match str(calculator.output):
                    case "":
                        pass
                    case _:
                        logger.info(f"The result is saved in {calculator._single_output_path}")

            
            elif (calculator.input.is_dir()):
                input_files = [(entry.name,) for entry in calculator.input.glob("*.json")]
                
                calculator.output = calculator._RectangleCalculator__validate_output_directory()

                match str(calculator.output):
                    case "":
                        logger.warning(
                            (   
                                "\nYou are passing multiple input files but no valid ouput directory path was given!!!"
                                "\nIf you procced, all results will be displayed here WITHOUT being saved!!!"
                            )
                        )
                        
                        answer = input(colored("Would you like to proceed? [y/n]: ", "blue", attrs = ["bold"]))
                        
                        if answer.lower() == "y":

                            with multiprocessing.Pool(processes = calculator.cores) as pool:
                                pool.starmap(func = calculator._single_workflow, iterable = input_files)
                        else:
                            return None # stop the program
                        
                    case _:
                        config_log_file(calculator.input.parent) # Only produce rectangle_logs.txt if the input and output directories or files are given           
                        
                        with multiprocessing.Pool(processes = calculator.cores) as pool:
                             pool.starmap(func = calculator._single_workflow, iterable = input_files)
                        # for entry in calculator.input.glob("*.json"):
                        #     calculator._single_workflow(entry.name)
                        
                        logger.info(f"All result files are saved in {calculator.output}")

            else:
                logger.error("There are multiple input files, but the output directory path was not correctly specified")                          

        else:
            calculator._single_workflow('')
    
    except Exception as e:
        logger.critical(e)


#---------------------------------------------------------------------------------------------------------#
#------------------------------------------ Run main() function ------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
    logger.info("Program ended! Thank you!")