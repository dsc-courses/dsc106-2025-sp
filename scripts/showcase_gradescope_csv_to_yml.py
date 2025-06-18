#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pandas",
#     "pyyaml",
# ]
# ///
"""Convert Gradescope CSV to YAML for project showcase. Use with
`./standardize-thumbnails.fish` to standardize the thumbnails.

Usage:
    ./showcase_gradescope_csv_to_yml.py <csv_file> [--output=<output_file>]

Options:
    -h --help     Show this help message
    --output=<output_file>  Output YAML path [default: ../_data/projects.yml]
"""
import argparse
import pandas as pd
import yaml


# Column names from Gradescope CSV
COL_TITLE = 'Question 1 Response'
COL_PERMISSION = 'Question 5.1 Response'
COL_VIDEO_PERMISSION = 'Question 5.2 Response'
COL_PROJECT_URL = 'Question 3 Response'
COL_VIDEO_URL = 'Question 4 Response'
COL_AWARD = 'Award'
COL_SUBMISSION_ID = 'Submission ID'
COL_STUDENT_NAME = 'Name'


def convert_csv_to_yml(csv_path, yml_path):
    # Read the CSV file
    df = pd.read_csv(csv_path)

    # Group by submission ID to combine team members
    grouped_projects = {}

    for _, row in df.iterrows():
        # Skip if no permission given
        if (pd.isna(row[COL_PERMISSION]) or
                'text_file_id' not in str(row[COL_PERMISSION])):
            continue

        submission_id = int(row[COL_SUBMISSION_ID])  # type: ignore

        # Use submission ID as key for grouping
        if submission_id not in grouped_projects:
            url = row[COL_PROJECT_URL].strip()
            project = {
                'title': row[COL_TITLE].strip(),
                'submission_id': submission_id,
                'url': url,
                'team': [],
            }

            # Add video URL if permission given
            if (not pd.isna(row[COL_VIDEO_PERMISSION]) and
                    'i would like my video to be linked' in
                    str(row[COL_VIDEO_PERMISSION]).lower()):
                video_url = row.get(COL_VIDEO_URL)
                if not pd.isna(video_url):
                    project['video'] = str(video_url).strip()

            # Add award if applicable
            if not pd.isna(row[COL_AWARD]):
                project['award'] = row[COL_AWARD].strip()

            grouped_projects[submission_id] = project

        # Add team member from Name column
        if not pd.isna(row[COL_STUDENT_NAME]):
            student_name = row[COL_STUDENT_NAME].strip()
            if student_name not in grouped_projects[submission_id]['team']:
                grouped_projects[submission_id]['team'].append(student_name)

    # Convert dictionary to list and write to YAML
    projects = list(grouped_projects.values())

    # Put best project awards first, then honorable mentions, then people's
    # choice
    def get_sort_key(project):
        award = project.get('award', '').lower()
        if 'best project' in award:
            return 0
        elif 'honorable mention' in award:
            return 1
        elif "people's choice" in award:
            return 2
        else:
            return 3

    projects.sort(key=get_sort_key)

    # Write to YAML file
    with open(yml_path, 'w', encoding='utf-8') as f:
        yaml.dump(projects, f, default_flow_style=False,
                  allow_unicode=True, sort_keys=False)
    print(f"Successfully converted {len(projects)} projects to YAML.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Convert Gradescope CSV to YAML for project showcase."
    )
    parser.add_argument("csv_file", help="Path to the input CSV file.")
    parser.add_argument(
        "--output",
        default="../_data/projects.yml",
        help="Path to the output YAML file. (default: %(default)s)",
    )
    args = parser.parse_args()
    convert_csv_to_yml(args.csv_file, args.output)
