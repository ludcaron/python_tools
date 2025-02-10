import tabula
import pandas as pd

def extract_table_from_pdf(pdf_path, csv_path, page_number=1):
    # Extraire le tableau du PDF
    tables = tabula.read_pdf(pdf_path, pages=page_number, multiple_tables=True)

    # Vérifier si des tables ont été trouvées
    if tables:
        # Sauvegarder la première table trouvée en CSV
        tables[0].to_csv(csv_path, index=False)
        print(f"Tableau extrait et sauvegardé dans {csv_path}")
    else:
        print("Aucun tableau trouvé dans le PDF.")

if __name__ == "__main__":
    pdf_path = "chemin/vers/votre_fichier.pdf"
    csv_path = "chemin/vers/votre_fichier.csv"
    extract_table_from_pdf(pdf_path, csv_path)