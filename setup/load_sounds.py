import csv
from pathlib import Path
from openai import OpenAI
client = OpenAI()

def vypis_simple(base,veta):
  speech_file_path = Path(__file__).parent / f'sounds/{base}_simple.mp3'
  response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    speed=0.7,
    input=veta
  )
  response.stream_to_file(speech_file_path)
  print(f'Streamed {veta} into {speech_file_path}')


def vypis_find(base,veta):
  speech_file_path = Path(__file__).parent / f'sounds/{base}_find.mp3'
  response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    speed=0.7,
    input=veta
  )
  response.stream_to_file(speech_file_path)
  print(f'Streamed {veta} into {speech_file_path}')

def vypis_wrong(base,veta):
  speech_file_path = Path(__file__).parent / f'sounds/{base}_wrong.mp3'
  response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    speed=0.7,
    input=veta
  )
  response.stream_to_file(speech_file_path)
  print(f'Streamed {veta} into {speech_file_path}')

def nacti_a_vypis_b_c(csv_soubor):
    with open(csv_soubor, 'r', encoding='utf-8') as soubor:
        ctecka = csv.reader(soubor, delimiter=';')
        for radek in ctecka:
            if len(radek) == 4:
                base, simple, find, wrong = radek
                vypis_simple(base,simple)
                vypis_find(base,find)
                vypis_wrong(base,wrong)
                

nacti_a_vypis_b_c('shapes.csv')


