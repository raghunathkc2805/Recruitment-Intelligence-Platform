import json
from pathlib import Path

output_file = Path("jd_parser/output/GRC -Talent Approval Request Form for Deltapro.json")
if output_file.exists():
    with open(output_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("JSON Output:")
    print(json.dumps(data, indent=2, ensure_ascii=False))
    print("\n" + "=" * 80)
    print("Employment Type and Work Mode:")
    print(f"employment_type: '{data['employment_type']}'")
    print(f"work_mode: '{data['work_mode']}'")
else:
    print("Output file not found")
