import re

changelog_path = "CHANGELOG.md"
index_path = "docs/index.md"

def extract_sections(text):
    sections = {"Novidades": [], "Correções": [], "Melhorias": []}
    current_type = None

    for line in text.splitlines():
        if line.startswith("### "):  # padrão cz
            current_type = line[4:].strip().lower()
        elif line.startswith("- ") or line.startswith("* "):
            if current_type == "feat":
                sections["Novidades"].append(line)
            elif current_type == "fix":
                sections["Correções"].append(line)
            elif current_type == "perf":
                sections["Melhorias"].append(line)

    return sections

def build_index_md(sections):
    content = "# Histórico de Mudanças\n\n"

    for titulo, items in sections.items():
        if items:
            content += f"## {titulo}\n\n"
            content += "\n".join(items) + "\n\n"

    return content

def update_index():
    with open(changelog_path, encoding="utf-8") as f:
        changelog = f.read()

    sections = extract_sections(changelog)
    new_index = build_index_md(sections)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_index)

if __name__ == "__main__":
    update_index()
