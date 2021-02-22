#!/usr/bin/env python
# -*- coding: utf-8 -*-
from openpyxl import load_workbook
import json
wb = load_workbook("base.xlsx")
ws = wb.active

jbase = []
for i, row in enumerate(ws.values):
	aluno = row[0].split("'")
	aluno = "".join(aluno)
	jbase.append({'aluno':f'{aluno}', 'matricula':row[1], 'cpf_mae':row[2] if row[2] else 0, 'cpf_pai':row[3] if row[3] else 0})

with open('base.json', 'w') as out:
	out.write(f"{jbase}")

print("Finalizado")