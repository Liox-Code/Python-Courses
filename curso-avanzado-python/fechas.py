from datetime import datetime
import pytz

def run():
  my_time = datetime.now()
  print(my_time)
  print(my_time.year)
  print(my_time.month)
  print(my_time.day)
  
  # Formatos
  print(my_time.strftime('Dia:%d Mes:%m Año:%Y Hora:%H Minutos:%M Segundos:%S'))
  print(my_time.strftime('%H:%M %p'))
  print(my_time.strftime('%I:%M %p'))

  #Time Zones
  #Lista de Time Zones Link: https://en.wikipedia.org/wiki/
  print("Time Zones")
  bogota_timezone = pytz.timezone("America/Bogota")
  bogota_date = datetime.now(bogota_timezone)
  print("Bogota:", bogota_date.strftime('%d/%m/%Y %H:%M:%S'))
  mexico_timezone = pytz.timezone("America/Mexico_City")
  mexico_date = datetime.now(mexico_timezone)
  print("Bogota:", mexico_date.strftime('%d/%m/%Y %H:%M:%S'))
  caracas_timezone = pytz.timezone("America/Caracas")
  caracas_date = datetime.now(caracas_timezone)
  print("Caracas:", caracas_date.strftime('%d/%m/%Y %H:%M:%S'))


if __name__ == "__main__":
  run()