from core.analyzer import read_code_file
from core.requirements_generator import generate_requirements

file_path = input("Enter source code file path: ")

code = read_code_file(file_path)

print("\nGenerating requirements...\n")

requirements = generate_requirements(code)

print("\nRequirements Generated Successfully\n")

print(requirements)

# Save output
with open("outputs/requirements.md", "w") as f:
    f.write(requirements)

print("\nRequirements saved to outputs/requirements.md")