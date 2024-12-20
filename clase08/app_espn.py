import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
import requests


def fetch_table_with_user_agent(url: str):
    # headers dict
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    # make get request
    try:
        response = requests.get(url, headers=headers)
        tables = pd.read_html(response.text)

        if tables:
            print(f'Cantidad de tablas detectadas: {len(tables)}')
            return tables[0]
        else:
            print(f'No se encontraron tablas en {url}')
            return None
    except Exception as e:
        print(f'Error al obtener la información de la url: {url}: {e}')
        return None


def save_dataframe_to_pdf(df, pdf_filename):
    # init pdf config
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font('Arial', size=12)

    # add title
    pdf.set_font('Arial', style='B', size=16)
    pdf.cell(w=0, h=10, text='Contenido de la pagina ESPN', ln=True, align='C')
    pdf.ln(10)

    # write info
    pdf.set_font('Arial', size=10)
    for index, row in df.iterrows():
        row_text = ', '.join([f'{col}: {row[col]}' for col in df.columns])
        pdf.multi_cell(w=0, h=10, text=row_text)
        pdf.ln(2)

    # save pdf
    pdf.output(name=pdf_filename)
    print(f'Archivo "{pdf_filename}".pdf generado')


def main():
    url_deporte = 'https://www.espn.com/nba/standings'
    df_deporte = fetch_table_with_user_agent(url=url_deporte)

    if df_deporte:
        print(df_deporte.head())
        save_dataframe_to_pdf(df=df_deporte, pdf_filename='analysis_espn.pdf')


if __name__ == '__main__':
    main()
