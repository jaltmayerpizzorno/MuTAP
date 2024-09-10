#!/bin/sh

set -x

DS="HumanEval"

rm -f $DS/Testing_${DS}/mutant_type.csv
#rm -f $DS/Testing_${DS}/*/Mutants/*
#for SHOTS in normal fewshot; do
for SHOTS in fewshot; do
    rm -f $DS/Testing_${DS}/${SHOTS}_synfix.csv
    rm -f $DS/Testing_${DS}/${SHOTS}_semfix.csv
    rm -f $DS/Testing_${DS}/${SHOTS}_mutant_score.csv
#    rm -rf $DS/Testing_${DS}/*/gpt4o
done

#SHOTS="normal"
SHOTS="fewshot"

for SAMPLE in {0..163}; do
    echo ">>>>> $SAMPLE"

    python3 MuTAP/Mutants_generation.py $DS $SAMPLE script_ mutant_type.csv

    python3 MuTAP/generate_test_oracle.py $SHOTS $DS $SAMPLE script_NDS_ "${SHOTS}_synfixed_" "${SHOTS}_synfix.csv"
    python3 MuTAP/semantic_error_correction.py $DS $SAMPLE "${SHOTS}_synfixed_" "${SHOTS}_semfixed_" "${SHOTS}_semfix.csv"
    python3 MuTAP/Mutation_Score.py $DS $SAMPLE "${SHOTS}_semfixed_" "${SHOTS}_mutant_score.csv"
    python3 MuTAP/augmented_prompt.py $SHOTS $DS $SAMPLE "${SHOTS}_semfixed_" "${SHOTS}_mut_" "${SHOTS}_mutant_score.csv"
    python3 MuTAP/Merge_all_mut.py $DS $SAMPLE "${SHOTS}_semfixed_" "${SHOTS}_mut_" "${SHOTS}_full_"
done
