# Merger_Files_PDF
Este script em Python utiliza a biblioteca PyPDF2 para mesclar todos os arquivos PDF encontrados na pasta "pdfs_mesclar" em um único arquivo PDF chamado "PDF_Final.pdf".

### Pré-requisitos:

- Python 3.x;
- Biblioteca PyPDF2;

### Instalação:

- Para instalar a biblioteca PyPDF2, execute o seguinte comando:

```
pip install PyPDF2
```

## Utilização

Coloque todos os arquivos PDF a serem mesclados na pasta "pdfs_mesclar".
Execute o script executando o seguinte comando:
python
Copy code
python merge_pdfs.py
O arquivo PDF mesclado será salvo no diretório de trabalho atual como "PDF_Final.pdf".
Funções
O script é dividido em três funções:

`connection()`
Esta função cria um objeto mesclador PyPDF2.

`finding_files()`
Esta função encontra todos os arquivos PDF na pasta "pdfs_mesclar" e retorna uma lista de seus nomes de arquivos.

`merging_files(merger, lista_arquivos)`
Esta função utiliza o objeto mesclador PyPDF2 e a lista de nomes de arquivos PDF para anexar todos os arquivos PDF ao objeto mesclador e salvar o resultado em um novo arquivo.

## Conclusão
Este script em Python é uma maneira simples e eficiente de mesclar vários arquivos PDF em um único arquivo usando a biblioteca PyPDF2. Com apenas algumas linhas de código, você pode mesclar rapidamente todos os seus arquivos PDF.