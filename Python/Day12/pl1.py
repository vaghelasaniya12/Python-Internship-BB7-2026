from pathlib import Path

folder = Path("backup")

if folder.exists():
    print("Backup folder already exists")

else:
    folder.mkdir()
    print("Backup folder created successfully")