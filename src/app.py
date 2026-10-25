from pathlib import Path
from main.job.pipeline import PySparkJob


import sys

def main(project_root: str, output_path:str) -> None:
    
    # Create paths
    data_dir = Path(project_root)/"data"
    src_dir = Path(project_root)/"src"

    # Create sparkSession
    job = PySparkJob()

    # Read files, create dataframes
    observed_df = job.read_csv(str(data_dir)+"/plants_observed_temp.csv")
    required_df = job.read_csv(str(data_dir)+"/plants_required_temp.csv")

    # Calculate average observed temperature
    observed_average_df = job.calc_average_temperature(observed_df)

    # Find faulty plants
    faulty_df = job.find_faulty_plants(observed_average_df,required_df)

    # Save results to volume
    job.save_as(faulty_df,output_path)