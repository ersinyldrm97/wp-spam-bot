import keyboard

dosya_adi = "read.txt"

while True:
  try:
    with open(dosya_adi, "r", encoding = 'utf-8') as file:
      for content in file:
        keyboard.write(content.strip())
        keyboard.press_and_release("enter")
        
  except Exception as e: 
    print(f'hata: {e}')