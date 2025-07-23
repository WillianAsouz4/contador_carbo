import sqlite3
import os

DB_PATH = os.path.join('data', 'carboidratos.db')

def conectar():
    return sqlite3.connect(DB_PATH)

def inserir_refeicao(alimento, carboidratos, data_hora):
    with conectar() as conn:
        cursor = conn.cursor()
        query = "INSERT INTO refeicoes (alimento, carboidratos, data_hora) VALUES (?, ?, ?)"
        cursor.execute(query, (alimento, carboidratos, data_hora))
        conn.commit()

def buscar_refeicoes_por_dia(data_str):
    with conectar() as conn:
        query = "SELECT alimento, carboidratos, strftime('%H:%M:%S', data_hora) as hora FROM refeicoes WHERE date(data_hora) = ?"
        cursor = conn.cursor()
        cursor.execute(query, (data_str,))
        return cursor.fetchall()