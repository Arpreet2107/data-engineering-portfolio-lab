device_status = input("Enter the device status (ON/OFF): ").lower()
print(f"Device status: {device_status}")
temperature = float(input("Enter the current temperature: "))
print(f"Current temperature: {temperature}°C")
if device_status == "on":
    if temperature > 35:
        print("The device is ON and the temperature is above 35°C. Turning on the cooling system.")
    elif temperature < 15:
        print("The device is ON and the temperature is below 15°C. Turning on the heating system.")
    else:
        print("The device is ON and the temperature is within the comfortable range. No action needed.")
elif device_status == "off":
    print("The device is OFF. No action needed.")