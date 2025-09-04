import shutil
import subprocess
import os

def gerar_changelog():
    print("🔁 Gerando changelog com Commitizen...")
    subprocess.run(["cz", "changelog"], check=True)

def copiar_changelog():
    src = "CHANGELOG.md"
    dst = os.path.join("docs", "changelog.md")
    print(f"📄 Copiando {src} para {dst}...")
    shutil.copyfile(src, dst)

def main():
    gerar_changelog()
    copiar_changelog()
    print("✅ Changelog atualizado com sucesso!")

if __name__ == "__main__":
    main()
