# manufacturing_fault_detection_pipeline

## Objective
Identify plants whose average observed temperature differs
from the required temperature by at least 5 degrees.

## Inputs
- plants_required_temp.csv: one record per plant
- plants_observed_temp.csv: multiple readings per plant

## Output
plantId, temperature

The output temperature is the average observed temperature.