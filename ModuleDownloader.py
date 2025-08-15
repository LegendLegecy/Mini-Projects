import os
import subprocess

def generate_requirements_file(directory="."):
    print("Generating requirements.txt using pipreqs...")
    subprocess.call(["pipreqs", directory, "--force"])

def install_requirements():
    if os.path.exists("requirements.txt"):
        print("Installing dependencies from requirements.txt...")
        subprocess.call(["pip", "install", "-r", "requirements.txt"])
    else:
        print("requirements.txt not found!")

def main():
    generate_requirements_file()
    install_requirements()
    print("Done ✅")

if __name__ == "__main__":
    main()
