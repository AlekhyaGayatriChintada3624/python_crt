text= input('enter the string')
for ch in text:
    ascii_value=ord(ch)
    if ascii_value % 2==0:
        print(f"{ch}={ascii_value} ->even")
    else:
        print(f"{ch}={ascii_value}->odd")