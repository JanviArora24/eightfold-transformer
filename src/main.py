import argparse

from parser import parse_csv,parse_resume
from merger import merge_candidate
from output_generator import save_output
from validator import validate
from config import load_config

parser = argparse.ArgumentParser()

parser.add_argument("--csv",required=True)

parser.add_argument("--resume",required=True)

parser.add_argument("--config",required=True)

args = parser.parse_args()

csv_data = parse_csv(args.csv)

resume_data = parse_resume(args.resume)

merged = merge_candidate(csv_data,resume_data)

validate(merged)

config = load_config(args.config)

save_output(merged,config)

print("Done")