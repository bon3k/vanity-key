# Vanity Key Generator (CLI)

Este es un generador de claves para Nostr en línea de comandos. Genera claves públicas (`npub`) que comiencen con un patrón personalizado.

## Características

- Genera frases mnemónicas BIP-39 de 12 palabras.
- Deriva claves privadas y públicas compatibles con Nostr.
- Permite buscar claves públicas que comiencen con un texto específico (vanity keys).
- Muestra el número de intentos y el tiempo total de búsqueda.

## Requisitos

- Python 3.8 o superior

## Instalación

Clona este repositorio y entra en la carpeta del proyecto:

```bash
git clone https://github.com/bon3k/vanity-key.git
cd vanity-key
```
Crea un entorno virtual e instala las dependencias:

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```
## Uso

Ejecuta el script desde la terminal:

```bash
python3 vanity-key.py
```

