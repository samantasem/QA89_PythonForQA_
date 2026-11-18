from pathlib import Path

data_folder = Path("test_data")
file_path = data_folder / "user.csv"
print(file_path)

print(file_path.exists())

screenshot_folder = Path("screenshots")
screenshot_folder.mkdir(exist_ok=True)
reportsFolders = Path("reports/2027")
reportsFolders.mkdir(parents=True, exist_ok=True)

base_dir = Path(__file__).resolve().parent
folder = base_dir / "reports"

folder = Path("../lesson9")
folder.mkdir(exist_ok=True)


def create_reports_folder():
    reports_dir = Path("reports_1")
    reports_dir.mkdir(exist_ok=True)
    result_file = reports_dir / "result.txt"
    with open(result_file, "w", encoding="utf-8") as file:
        file.write("Homework completed successfully!")


create_reports_folder()



